#!/usr/bin/env python3
"""
Script to read and parse YAML files
"""

import yaml
import sys
from pathlib import Path

def read_yaml_file(file_path):
    """
    Read and parse a YAML file
    
    Args:
        file_path (str): Path to the YAML file
        
    Returns:
        dict: Parsed YAML content
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def print_yaml_content(data, indent=0):
    """
    Pretty print YAML content
    
    Args:
        data: The data to print
        indent (int): Current indentation level
    """
    spaces = "  " * indent
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{spaces}{key}:")
                print_yaml_content(value, indent + 1)
            else:
                print(f"{spaces}{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                print(f"{spaces}-")
                print_yaml_content(item, indent + 1)
            else:
                print(f"{spaces}- {item}")
    else:
        print(f"{spaces}{data}")

def main():
    """Main function"""
    # Check if filename was provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python yaml_reader.py <yaml_file>")
        print("Example: python yaml_reader.py config.yml")
        sys.exit(1)
    
    yaml_file = sys.argv[1]
    
    # Check if file exists
    if not Path(yaml_file).exists():
        print(f"Error: File '{yaml_file}' does not exist.")
        sys.exit(1)
    
    # Read the YAML file
    print(f"Reading YAML file: {yaml_file}")
    print("-" * 50)
    
    data = read_yaml_file(yaml_file)
    
    if data is not None:
        print("YAML Content:")
        print_yaml_content(data)
        
        # Example: Access specific values
        print("\n" + "-" * 50)
        print("Example - Accessing specific values:")
        
        # If it's a dictionary, show how to access values
        if isinstance(data, dict):
            for key in list(data.keys())[:3]:  # Show first 3 keys
                print(f"data['{key}'] = {data[key]}")
    else:
        print("Failed to read YAML file.")
        sys.exit(1)

if __name__ == "__main__":
    main()