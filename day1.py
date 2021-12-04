import collections

# Find the amount of times the next value increased
def part1() -> int:
    counter = 0
    with open("day1.txt", 'r') as f:
        # Get the first value
        prev_val = next(f)
        # Update every time the next value is bigger than previous value
        for line in f:
            if int(line) > int(prev_val):
                counter += 1
            prev_val = line
    return counter

print(part1())

# Find the amount of times the sliding window increased
def part2() -> int:
    counter = 0
    with open("day1.txt", 'r') as f:
        arr = collections.deque()
        # build sliding window
        arr.append(int(next(f)))
        arr.append(int(next(f)))
        arr.append(int(next(f)))
        oldSum = sum(arr)
        newSum = sum(arr)
        for line in f:
            # find new sum and compare to old sum
            newSum += int(line) - arr[0]
            if oldSum < newSum:
                counter += 1
            oldSum = newSum
            # update sliding window
            arr.rotate(-1)
            arr[2] = int(line)
    return counter
    
print(part2())
            

        


