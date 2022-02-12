from random import randint


#determine play parts 
#player1-black
q = "queen"
#player2-white
r = "rook"
b = "bishop"

#initialize chessboard 2D 8x8
chessboard = []
for i in range(8):
    row = []
    for j in range(8):
        row.append(" ")
    chessboard.append(row)

player1 = 0
player2 = 0 

#play_track = [
#             0 [ 0,  1,  2,  3,  4,  5,  6,  7],
#             1 [ 8,  9, 10, 11, 12, 13, 14, 15],
#             2 [16, 17, 18, 19, 20, 21, 22, 23],
#             3 [24, 25, 26, 27, 28, 29, 30, 31],
#             4 [32, 33, 34, 35, 36, 37, 38, 39],
#             5 [40, 41, 42, 43, 44, 45, 46, 47],
#             6 [48, 49, 50, 51, 52, 53, 54, 55],
#             7 [56, 57, 58, 59, 60, 61, 62, 63]
#                 0   1   2   3   4   5   6   7 ]

for i in range(100):
    active = True 
    tmp1 = False
    tmp2 = False
    check_d1 = False
    check_d2 =  False

    while active == True:
        chessboard = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(" ")
            chessboard.append(row)

        #generate random positions
        row_q = randint(0,7)
        column_q = randint(0,7)
        row_r = randint(0,7)
        column_r = randint(0,7)
        while row_r == row_q and column_r == column_q:
            row_r = randint(0,7)
            column_r = randint(0,7)
        row_b = randint(0,7)
        column_b = randint(0,7)
        while (row_b == row_q and column_b == column_q) or (row_b == row_r and column_b == column_r):
            row_b = randint(0,7)
            column_b = randint(0,7)

        #insert pieces into chessboard
        chessboard[row_q].pop(column_q)
        chessboard[row_q].insert(column_q,q)
        chessboard[row_r].pop(column_r)
        chessboard[row_r].insert(column_r,r)
        chessboard[row_b].pop(column_b)
        chessboard[row_b].insert(column_b,b)

        #check
        #queen
        #rows
        if row_q == row_b and row_q == row_r:
            player1 +=2
        elif row_q == row_b:
            player1 +=1
        elif row_q == row_r:
            player1 +=1 
        #columns
        if column_q == column_b and column_q == column_r:
            player1 +=2
        elif column_q == column_b:
            player1 +=1 
        elif column_q == column_r:
            player1 +=1
        #diagonals
        if (row_b - row_q == column_b - column_q) or (row_r - row_q == column_r - column_q):
            check_d1 = True
        if (-row_b + row_q == -column_b + column_q) or (-row_r + row_q == -column_r - column_q):
            check_d2 = True

        if check_d1 == True and check_d2 == True:
            player1 +=2
        elif check_d1 == True:
            player1 +=1
        elif check_d2 == True:
            player1 +=1


        #rook
        #rows
        if row_r == row_q:
            tmp1 = True
        #columns
        if column_r == column_q:
            tmp1 = True
        
        #bishop
        if (row_q - row_b == column_q - column_b):
            tmp1 = True
        elif (-row_q + row_b == column_q + column_b):
            tmp1 = True

        if (tmp1 == True) and (tmp2 == True):
            player2 +=2 
        elif tmp1 == True:
            player2 +=1
        elif tmp2 == True:
            player2 +=1 

        active = False

print("player1 score: " + str(player1))
print("player2 score: " + str(player2))

    





