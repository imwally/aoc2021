
from typing import ForwardRef


fname = "input02.txt"

# Part 1
with open(fname) as f:
    lines = f.readlines()
    depth = 0
    horizontal = 0
    
    for line in lines:
        command, units = line.split(" ")
        units = int(units)
        if command == "up":
            depth -= units
        if command == "down":
            depth += units
        if command == "forward":
            horizontal += units

print(f"Part 1: {depth * horizontal}")
        
# Part 2
with open(fname) as f:
    lines = f.readlines()
    aim = 0
    depth = 0
    horizontal = 0
    
    for line in lines:
        command, units = line.split(" ")
        units = int(units)
        if command == "up":
            aim -= units
        if command == "down":
            aim += units
        if command == "forward":
            horizontal += units
            depth += aim*units

print(f"Part 2: {depth * horizontal}")