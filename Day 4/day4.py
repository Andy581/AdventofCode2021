

def part1() -> int: 
    boards = []
    matrix = []
    hitZero = False
    with open("day4.txt", 'r') as f:
        line = f.readline()[0:-1]
        numbers = line.split(",")
        numbers = [int(x) for x in numbers]
        for line in f:
            if not line.strip():
                continue
            line = line[0:-1]
            row = line.split(' ')
            row = list(filter(None, row))  
            row = [int(x) for x in row] 
            matrix.append(row)
            if len(matrix) == 5:
                boards.append(matrix)
                matrix = [] 
        for num in numbers:
            if num == 0:
                hitZero = True
            for board in boards:
                for row in board:
                    if num in row:
                        row[row.index(num)] = -num
                if(checkBingo(board, hitZero)):
                    return sumOfBoard(board) * num
        
def checkBingo(board, hasZero)->bool:
    # Check if there are any horizontal bingos
    for row in board:
        if len([x for x in row if x < 0 or (x == 0 and hasZero)]) == 5:
            return True
    # Check if there are any vertical bingos
    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        if len([x for x in col if x < 0 or (x == 0 and hasZero)]) == 5:
            return True
    return False

def sumOfBoard(board) -> int:
    res = 0
    for row in board:
        for num in row:
            res += num if num >= 0 else 0
    return res


def boardPrint(board):
    for row in board:
        print(row)
    print("new board")

print(part1())


# PART 2 ############################################################

def part2() -> int: 
    boards = []
    matrix = []
    hitZero = False
    with open("day4.txt", 'r') as f:
        line = f.readline()[0:-1]
        numbers = line.split(",")
        numbers = [int(x) for x in numbers]
        for line in f:
            if not line.strip():
                continue
            line = line[0:-1]
            row = line.split(' ')
            row = list(filter(None, row))  
            row = [int(x) for x in row] 
            matrix.append(row)
            if len(matrix) == 5:
                boards.append(matrix)
                matrix = [] 
        for num in numbers:
            if num == 0:
                hitZero = True
            for board in boards:
                for row in board:
                    if num in row:
                        row[row.index(num)] = -num
                if(checkBingo(board, hitZero)):
                    if(len(boards) != 1):
                        boards = [x for x in boards if x != board] 
                    else:
                        return sumOfBoard(boards[0]) * num
                        
print(part2())