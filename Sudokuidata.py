#backtracking

board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
  
]

def solve(bo):
    #anroppar funktionen 
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,5):
        #anroppar den valid funktioner flera gånger tills det inte blir samma siffra på rad och kolum
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # kollar raden
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # kollar kolumn
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # kollar boxen, alltså 2*2
    box_x = pos[1] // 2
    box_y = pos[0] // 2
    # här kollar den om boxen har en siffra som inte borde finnas där
    for i in range(box_y*2, box_y*2 + 2):
        for j in range(box_x * 2, box_x*2 + 2):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

#design på sudoku 4X4
def print_sudoku(bo):
    for i in range(len(bo)):
        if i % 2 == 0 and i != 0:
            print("- - - - - - -  ")

        for j in range(len(bo[0])):
            if j % 2 == 0 and j != 0:
                print(" | ", end="")
            #den översiger inte 4 rader
            if j == 3:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    #kollar om siffran är noll på listan.
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # rad, kolum
          


    return None
#printar ut den första listan
print_sudoku(board)
solve(board)
print("____________")
l=1
board1 = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
  
]
i=1
#ändra värden på i för att få olika sudoku
for i in range(17):
    if i == 3:
        #kopierar över värdet till en ny lista
        board1[i] = board[i]
    

print_sudoku(board1)
#printar ut den andra listan med nya värden
