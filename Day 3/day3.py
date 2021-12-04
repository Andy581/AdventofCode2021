import copy

# Find gamma rate and epsilon rate
def part1() -> int:
    with open("day3.txt", 'r') as f:
        gamma = ""
        # Put each line as an element in a list
        # An example of an element would be "111111111111\n"
        # len of an element is always 13
        lines = f.readlines()
        for i in range(12):
            zero, one = 0, 0
            # array of all the bits in the ith place of each string
            arr = [int(x[i]) for x in lines]
            for x in arr:
                if x == 0:
                    zero += 1
                else:
                    one += 1
            # Get highest frequency and append to the gamma string
            gamma += "0" if zero > one else "1"
        # epsilon is the XOR or opposite of gamma
        epsilon = int(gamma, 2) ^ int("111111111111", 2)
        # convert gamma to a base 10 integer and multiply by epsilon
        return int(gamma, 2) * epsilon

def part2():
    with open("day3.txt", 'r') as f:
        oxy = ""
        co2 = ""
        # lines is for oxygen and lines2 will be used to find co2
        lines = f.readlines()
        lines2 = copy.deepcopy(lines)
        for i in range(12):
            zero, one = 0,0
            # array of all the bits in the ith place of each string
            arr = [int(x[i]) for x in lines]
            for x in arr:
                if x == 0:
                    zero += 1
                else:
                    one += 1
            # find highest frequency of the bits in the ith place of each string
            bitCrit = '1' if one >= zero else '0'
            # filter out the strings that does not match the criteria
            lines = [x for x in lines if x[i] == bitCrit]
            if len(lines) == 1:
                oxy = lines[0]
                break
            
        for i in range(12):
            zero, one = 0,0
            # array of all the bits in the ith place of each string
            arr = [int(x[i]) for x in lines2]
            for x in arr:
                if x == 0:
                    zero += 1
                else:
                    one += 1
            # find highest frequency of the bits in the ith place of each string
            bitCrit = '1' if one >= zero else '0'
            # filter out the strings that does  match the criteria
            lines2 = [x for x in lines2 if x[i] != bitCrit]
            if len(lines2) == 1:
                co2 = lines2[0]
        # convert to base 10 integers and multiply
        return int(oxy, 2) * int(co2, 2)
print(part2())

