
fname = "input01.txt"

# Part 1
with open(fname) as f:
    lines = f.readlines()
    current_depth = 0
    num_increases = -1

    for line in lines:
        depth = int(line)
        if depth > current_depth:
            num_increases += 1
        current_depth = depth

print(f"Part 1: {num_increases}")

# Part 2
with open(fname) as f:
    lines = f.readlines()
    current_depth = 0
    num_increases = -1

    nums = [int(line) for line in lines]
    for i in range(len(nums)):
        if i < len(nums)-2:
            depth = sum(nums[i:i+3])
            if depth > current_depth:
                num_increases += 1
            current_depth = depth

print(f"Part 2: {num_increases}")