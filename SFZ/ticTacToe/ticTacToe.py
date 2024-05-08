def getvalidInput():
    while True:
        space = input("Where do you want to space your mark (1;9)")
        try:
            space = int(space)
        except ValueError:
            print("That was not a number!")
            continue
        for x in range(1, 10):
            if space == x:
                return space - 1
            
        print("This number was not between 1 and 9")
        continue


def new_board():
    board = []
    for i in range(9):
        board.append(" ")
    return board


def print_board(board):
    print(board[0], " | ", board[1], " | ", board[2])
    print(13*"-")
    print(board[3], " | ", board[4], " | ", board[5])
    print(13*"-")
    print(board[6], " | ", board[7], " | ", board[8])


def row(n):
    if n == 0:
        return [0,1,2]
    if n == 1:
        return [3,4,5]
    if n == 2:
        return [6,7,8]


def column(n):
    if n == 0:
        return [0,3,6]
    if n == 1:
        return [1,4,7]
    if n == 2:
        return [2,5,8]


def diagonal(n):
    if n == 0:
        return [0,4,8]
    if n == 1:
        return [2,4,6]


def alllines():
    lines = []
    for x in range(3):
        lines.append(row(x))
    for x in range(3):
        lines.append(column(x))
    for x in range(2):
        lines.append(diagonal(x))
    return lines


def check_win(board):
    lines = alllines()
    for x in lines:
        if board[x[0]] == "X":
            if board[x[1]] == "X":
                if board[x[2]] == "X":
                    print("Player1 won!")
                    exit()
        elif board[x[0]] == "O":
            if board[x[1]] == "O":
                if board[x[2]] == "O":
                    print("Player2 won!")
                    exit()


def check_draw(board):
    lines = alllines()
    i = 0
    for x in lines:
        if ((board[x[0]]  == "X") or (board[x[1]]  == "X") or (board[x[2]]  == "X")) and ((board[x[0]]  == "O") or (board[x[1]]  == "O") or (board[x[2]]  == "O")):
            i += 1
    if i == 8:
        print("draw!")
        exit()


def set_space(board, space, turn):
    if turn == 1:
        board[space] = "X"
    elif turn == 2:
        board[space] = "O"
    else:
        print(turn)
    return board


board = new_board()
turn = 1
print_board(board)
while True:
    print("Player"+  str(turn) +"´s turn")
    while True:
        space = getvalidInput()
        if board[space] == " ":
            board = set_space(board, space, turn)
            break
        else:
            print("This Space is already obtained!")
    print_board(board)
    check_win(board)
    check_draw(board)
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1