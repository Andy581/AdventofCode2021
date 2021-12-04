# Find depth and pos of submarine
def part1() -> int:
    pos, depth = 0,0
    with open("day2.txt", 'r') as f:
        for line in f:
            arr = line.split(" ")
            if arr[0] == "forward":
                pos += int(arr[1])
            elif arr[0] == "down":
                depth += int(arr[1])
            else:
                depth -= int(arr[1])
    return pos * depth

print(part1())

# Find depth and pos of submarine
def part2() -> int:
    pos, aim, depth = 0,0,0
    with open("day2.txt", 'r') as f:
        for line in f:
            arr = line.split(" ")
            if arr[0] == "forward":
                pos += int(arr[1])
                depth += aim * int(arr[1])
            elif arr[0] == "up":
                aim -= int(arr[1])
            else:
                aim += int(arr[1])
    return pos * depth
    
print(part2())