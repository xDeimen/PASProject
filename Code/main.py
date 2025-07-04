import asyncio
from robodk import robolink
from src.robot import AsyncRobotManager

RDK = robolink.Robolink()

# Option 1: Async approach
async def main():
    manager = AsyncRobotManager(RDK, ["R1", "R2", "R3", "R4"])
    await manager.move_all_home()

asyncio.run(main())

# Option 2: Sync but simultaneous (recommended)
manager = AsyncRobotManager(RDK, ["R1", "R2", "R3", "R4"])
manager.move_all_home_sync()