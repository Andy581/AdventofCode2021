
def part1() -> int:
    with open("input.txt", 'r') as f:
        res = 0
        grid = [[0 for i in range(1000)] for j in range(1000)]
        for line in f:
            line = line.replace("-> ", '')
            line = line[0:-1] 
            list1 = line.split(" ") 
            sourcePair = list1[0].split(",") 
            sourcePair = [int(x) for x in sourcePair]
            destPair = list1[1].split(",")
            destPair = [int(x) for x in destPair]
            # skip non-horizontal and non-vertical lines
            if(sourcePair[0] == destPair[0] or sourcePair[1] == destPair[1]):
                if sourcePair[0] == destPair[0]: # vertical line
                    # gets top point
                    start = sourcePair[1] if sourcePair[1] <= destPair[1] else destPair[1]
                    # gets bottom point
                    end = sourcePair[1] if start != sourcePair[1] else destPair[1]
                    for i in range(start, end+1):
                        grid[int(sourcePair[0])][i] += 1

                else: # horizontal line
                    # gets left point
                    start = sourcePair[0] if sourcePair[0] <= destPair[0] else destPair[0]
                    # gets right point
                    end = sourcePair[0] if start != sourcePair[0] else destPair[0]
                    for i in range(start, end+1):
                        grid[i][sourcePair[1]] += 1
        # finds all occurences where the element is >= 2
        for row in grid:
            for col in row:
                if col >= 2:
                    res += 1
    return res
print(part1())

def part2() -> int:
    with open("input.txt", 'r') as f:
        res = 0
        grid = [[0 for i in range(1000)] for j in range(1000)]
        for line in f:
            line = line.replace("-> ", '')
            line = line[0:-1] 
            list1 = line.split(" ") 
            sourcePair = list1[0].split(",") 
            sourcePair = [int(x) for x in sourcePair]
            destPair = list1[1].split(",")
            destPair = [int(x) for x in destPair]
            # checks for horizontal or vertical line ( reuse code from part1 )
            if(sourcePair[0] == destPair[0] or sourcePair[1] == destPair[1]):
                if sourcePair[0] == destPair[0]: # vertical line
                    start = sourcePair[1] if sourcePair[1] <= destPair[1] else destPair[1]
                    end = sourcePair[1] if start != sourcePair[1] else destPair[1]
                    for i in range(start, end+1):
                        grid[int(sourcePair[0])][i] += 1

                else: # horizontal line
                    start = sourcePair[0] if sourcePair[0] <= destPair[0] else destPair[0]
                    end = sourcePair[0] if start != sourcePair[0] else destPair[0]
                    for i in range(start, end+1):
                        grid[i][sourcePair[1]] += 1
            # increasing diagonal line
            elif((sourcePair[0] < destPair[0] and sourcePair[1] > destPair[1]) or (sourcePair[0] > destPair[0] and sourcePair[1] < destPair[1])):
                # leftmost point
                start = sourcePair if sourcePair[0] < destPair[0] else destPair
                # rightmost point
                end = destPair if sourcePair[0] < destPair[0] else sourcePair
                j = 0
                for i in range(start[1], end[1] - 1, -1):
                    grid[start[0]+j][i] += 1
                    j += 1
            # decreasing diagonal line
            elif((sourcePair[0] < destPair[0] and sourcePair[1] < destPair[1]) or (sourcePair[0] > destPair[0] and sourcePair[1] > destPair[1])):
                # leftmost point
                start = sourcePair if sourcePair[0] < destPair[0] else destPair
                # rightmost point
                end = destPair if sourcePair[0] < destPair[0] else sourcePair
                j = 0
                for i in range(start[0], end[0] + 1):
                    grid[i][start[1] + j] += 1
                    j += 1
        for row in grid:
            for col in row:
                if col >= 2:
                    res += 1
        return res
print(part2())


