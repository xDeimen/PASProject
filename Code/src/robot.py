from __future__ import annotations
from robodk import robolink
from dataclasses import dataclass
from typing import Any, List, Dict, Optional
import asyncio
import threading
import time

class Robot:
    def __init__(self, RDK, name):
        self.RDK = RDK
        self.name = name
        self.robot = self._init_robot()
        self.tool = self._set_tool()
        self.attached_object = None
        self.home = self._set_home()
        self.sequence = {}  # Initialize as empty dict
    
        
    def _init_robot(self):
        robot = self.RDK.Item(self.name)
        if not robot.Valid():
            raise ValueError(f"Robot '{self.name}' not found in RoboDK station")
        return robot
        
    def _set_tool(self):
        tool = self.RDK.Item(f"{self.name}Tool")
        if tool.Valid():
            self.robot.setTool(tool)
        return tool
    
    def _set_home(self):
        home_point = self.RDK.Item(f'{self.name}Home')
        base = self.RDK.Item(f'{self.name}Base')
        if not home_point.Valid():
            print(f"Warning: {self.name}Home not found")
        return Target(point=home_point, base=base)
    
    def set_sequence(self, move_list: list):
        """Set the movement sequence for this robot"""
        self.sequence = {}
        for i, move in enumerate(move_list):
            if isinstance(move, dict):
                move_type = list(move.values())[0]  # "J" or "L"
                target_info = list(move.keys())[0]  # (point_name, base_name)
                
                if move_type == "J":
                    target = Target(
                        point=self.RDK.Item(target_info[0]), 
                        base=self.RDK.Item(target_info[1])
                    )
                    self.sequence[i] = (self._J, target)
                elif move_type == "L":
                    target = Target(
                        point=self.RDK.Item(target_info[0]), 
                        base=self.RDK.Item(target_info[1])
                    )
                    self.sequence[i] = (self._L, target)
    
    def _pick(self, object_to):
        to_pick = self.RDK.Item(object_to)
        if to_pick.Valid():
            to_pick.setParent(self.robot)
            self.attached_object = to_pick
    
    def _drop(self, where_to):
        if self.attached_object:
            place_frame = self.RDK.Item(where_to)
            if place_frame.Valid():
                self.attached_object.setParent(place_frame)
                self.attached_object = None
    
    def _J(self, target):
        """Joint movement - non-blocking"""
        if target.base.Valid():
            self.robot.setPoseFrame(target.base)
        self.robot.MoveJ(target.point, blocking=False)
    
    def _L(self, target):
        """Linear movement - non-blocking"""
        if target.base.Valid():
            self.robot.setPoseFrame(target.base)
        self.robot.MoveL(target.point, blocking=False)  # Fixed: was MoveLAsync
    
    def _move_home(self):
        """Move to home position - non-blocking"""
        self._J(self.home)
    
    def wait_move(self):
        """Wait for current movement to complete"""
        while self.robot.Busy():
            time.sleep(0.01)
    
    async def async_move_home(self):
        """Async version of move home"""
        self._move_home()
        await self._async_wait_move()
    
    async def _async_wait_move(self):
        """Async wait for movement completion"""
        while self.robot.Busy():
            await asyncio.sleep(0.01)
    
    def run_sequence(self):
        """Run the movement sequence synchronously"""
        for i in sorted(self.sequence.keys()):
            func, param = self.sequence[i]
            func(param)
            self.wait_move()  # Wait for each move to complete
    
    async def async_run_sequence(self):
        """Run the movement sequence asynchronously"""
        for i in sorted(self.sequence.keys()):
            func, param = self.sequence[i]
            func(param)
            await self._async_wait_move()  # Async wait for each move
    
    def run_sequence_parallel(self):
        """Start sequence without waiting - for true parallel execution"""
        for i in sorted(self.sequence.keys()):
            func, param = self.sequence[i]
            func(param)
            # Don't wait - let all moves happen in parallel
    
    def is_busy(self):
        """Check if robot is currently moving"""
        return self.robot.Busy()

@dataclass
class Target:
    point: Any
    base: Any

@dataclass 
class Sequence:
    moves: List[Dict[callable, Any]]

# Async Robot Manager for coordinating multiple robots
class AsyncRobotManager:
    def __init__(self, RDK, robot_names: List[str]):
        self.RDK = RDK
        self.robots = [Robot(RDK, name) for name in robot_names]
    
    async def move_all_home(self):
        """Move all robots home simultaneously"""
        # Start all movements
        for robot in self.robots:
            robot._move_home()
        
        # Wait for all to complete
        await self._wait_all_complete()
    
    async def _wait_all_complete(self):
        """Wait for all robots to complete their movements"""
        while any(robot.is_busy() for robot in self.robots):
            await asyncio.sleep(0.01)
    
    async def run_all_sequences(self):
        """Run all robot sequences simultaneously"""
        # Start all sequences
        for robot in self.robots:
            robot.run_sequence_parallel()
        
        # Wait for all to complete
        await self._wait_all_complete()
    
    def move_all_home_sync(self):
        """Synchronous version - all robots move simultaneously"""
        # Start all movements
        for robot in self.robots:
            robot._move_home()
        
        # Wait for all to complete
        while any(robot.is_busy() for robot in self.robots):
            time.sleep(0.01)
        
        print("All robots reached home!")