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


class Board:
    def __init__(self):
        self.state = []
        for i in range(9):
            self.state.append(" ")


    def print_board(self):
        print(self.state[0], " | ", self.state[1], " | ", self.state[2])
        print(13*"-")
        print(self.state[3], " | ", self.state[4], " | ", self.state[5])
        print(13*"-")
        print(self.state[6], " | ", self.state[7], " | ", self.state[8])


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
        for x in lines:
            if board[x[0]] or board[x[1]] or board[x[2]]  == " ":
                return
            else:
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
    check_draw(board)
    check_win(board)
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1