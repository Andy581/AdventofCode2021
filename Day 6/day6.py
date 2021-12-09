def part1() -> int:
    with open("input.txt", 'r') as f:
        line = f.readline()
        line = line[0:-1]
        fishList = line.split(",")
        fishList = [int(x) for x in fishList]
        for i in range(80):
            for j in range(len(fishList)):
                fishList[j] -= 1
                if fishList[j] < 0:
                    fishList.append(8)
                    fishList[j] = 6
        return len(fishList)
print(part1())

# PART 2

def part2() -> int:
    with open("input.txt", 'r') as f:
        line = f.readline()
        line = line[0:-1]
        fishList = line.split(",")
        fishList = [int(x) for x in fishList]
        for i in range(256):
            for j in range(len(fishList)):
                fishList[j] -= 1
                if fishList[j] < 0:
                    fishList.append(8)
                    fishList[j] = 6
            print(i)
        return len(fishList)
print(part2())