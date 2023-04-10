from random import randint, shuffle, random, randrange

#ring size
l = "large" 
m = "medium"  
s = "small"  
ms = s + " " + m   #small medium
ls = s + " " + l   #small large
lm = l + " " + m   #large medium
msl = ms + " " + l #medium small large

#initialize rings
rings = []
for i in range(9):
    rings.append(l)
    rings.append(m)
    rings.append(s)

counter = 0
active = True
previous_ring = " "
previous_column = -1
previous_row = -1
previous_location = " "

#3x3 2D list representing the play area
play_track = []  
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    play_track.append(row)

#play_track = [
#              [0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8]
#                       ]

for game in range(100):
    rings = []
    for i in range(9):
        rings.append(l)
        rings.append(m)
        rings.append(s)
    shuffle(rings)
    play_track = []  
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        play_track.append(row)
    previous_ring = " "
    previous_column = -1
    previous_row = -1
    previous_location = " "
    large_h = 0
    large_d1 = 0
    large_d2 = 0
    large_v = 0
    medium_h = 0
    medium_d1 = 0
    medium_d2 = 0
    medium_v = 0
    small_h = 0
    small_d1 = 0
    small_d2 = 0
    small_v = 0
    active = True
    while active == True:
        for player in range(len(rings)):
            counter +=1
            #generate random ring from rings & random location on play area
            if len(rings) == 1:
                place = 0
            else:
                place = randint(0,len(rings)-1)
            current_ring = rings[place]
            row = randint(0,2)
            column = randint(0,2)
            location = play_track[row][column]
            previous_ring = current_ring
            previous_row = row
            previous_column = column
            previous_location = location
            
            #insert current ring into the play area & delete used ring
            rings.pop(place)
            if location == " ": #remove spaces from list
                play_track[row].pop(column)
                play_track[row].insert(column,current_ring)
                previous_row = row
                previous_column = column
            elif (current_ring == previous_ring) and (previous_row == row) and (previous_column == column): #check if a ring is going to be put in the same location with one of the same size
                row = randint(0,2)
                column = randint(0,2)
                location = play_track[row][column]
                #put different sizes in same location
                if (previous_location == s and location == m) or (previous_location == m and location == s):
                    previous_location = ms  
                    play_track[row].pop(column) 
                    play_track[row].insert(column,ms)   
                if (previous_location == s and location == l) or (previous_location == l and location == s):
                    previous_location = ls
                    play_track[row].pop(column)     
                    play_track[row].insert(column,ls)   
                if (previous_location == m and location == l) or (previous_location == l and location == m):
                    previous_location = lm  
                    play_track[row].pop(column)  
                    play_track[row].insert(column,lm)   
                if (previous_location == ms and location == l) or (previous_location == ls and location == m) or (previous_location == lm and location == s):
                    previous_location = msl
                    play_track[row].pop(column) 
                    play_track[row].insert(column,msl)
                previous_ring = current_ring
                previous_row = row
                previous_column = column
            else:
                if (previous_location == s and location == m) or (previous_location == m and location == s):
                    previous_location = ms   
                    play_track[row].pop(column) 
                    play_track[row].insert(column,ms)      
                if (previous_location == s and location == l) or (previous_location == l and location == s):
                    previous_location = ls    
                    play_track[row].pop(column) 
                    play_track[row].insert(column,ls)  
                if (previous_location == m and location == l) or (previous_location == l and location == m):
                    previous_location = lm   
                    play_track[row].pop(column) 
                    play_track[row].insert(column,lm) 
                if (previous_location == ms and location == l) or (previous_location == ls and location == m) or (previous_location == lm and location == s):
                    previous_location = msl
                    play_track[row].pop(column) 
                    play_track[row].insert(column,msl)      
                previous_row = row
                previous_column = column
                previous_ring = current_ring

            #check if game is over
            #check horizontally
            for i in range(3):
                for j in range(3):
                    large_h = play_track[i][j].split().count("large")
                    if large_h == 3:
                        active = False
                        break
                    medium_h = play_track[i][j].split().count("medium")
                    if medium_h == 3:
                        active = False
                        break
                    small_h = play_track[i][j].split().count("small")
                    if small_h == 3:
                        active = False
                        break
                if active == False:
                    break              

            #check vertically
            for i in range(3):
                for j in range(3):
                    large_v = play_track[j][i].split().count("large")
                    if large_v == 3:
                        active = False
                        break
                    medium_v = play_track[j][i].split().count("medium")
                    if medium_v == 3:
                        active = False
                        break
                    small_v = play_track[j][i].split().count("small") 
                    if small_v == 3:
                        active = False
                        break
                if active == False:
                    break

            #check diagonally
            for i in range(3):
                large_d1 = large_d1 + play_track[i][i].split().count("large")
                medium_d1 = medium_d1 + play_track[i][i].split().count("medium")
                small_d1 = small_d1 + play_track[i][i].split().count("small")
                large_d2 = large_d2 + play_track[i][3 - 1 - i].split().count("large")
                medium_d2 = medium_d2 + play_track[i][3 - 1 - i].split().count("medium")
                small_d2 = small_d2 + play_track[i][3 - 1 - i].split().count("small") 
                if large_d1 == 3 or large_d2 == 3:
                    active = False
                    break
                elif medium_d1 == 3 or medium_d1 == 3:
                    active = False
                    break
                elif small_d1 or small_d2 == 3:
                    active = False
                    break
        
           # for i in range(3):
               # for j in range(3):
            while i == 0 and j == 0:
                        a = play_track[i][j].split().count("small")
                        b = play_track[i][j + 1].split().count("medium")
                        c = play_track[i][j + 2].split().count("large")
                        d = play_track[i][j].split().count("large")
                        e = play_track[i][j + 2].split().count("small")

                        f = play_track[j][i].split().count("small")
                        g = play_track[j][i + 1].split().count("medium")
                        h = play_track[j][i + 2].split().count("large")
                        i = play_track[j][i].split().count("large")
                        j = play_track[j][i + 2].split().count("small")

                        k = play_track[i][i].split().count("small")
                        l = play_track[i + 1][3 - 2 - i].split().count("medium")
                        m = play_track[i + 2][3 - 1 - i].split().count("large")
                        n = play_track[i][i].split().count("large")
                        o = play_track[i + 2][3 - 1 - i].split().count("small")
                        if (a + b + c == 3) or (b + d + e == 3) or (f + g + h == 3) or (i + j + g == 3) or (k + l + m == 3) or (n + o + l == 3):
                            active = False
                            break

            while i == 1 and j == 1:
                        a = play_track[i][j - 1].split().count("small")
                        b = play_track[i][j].split().count("medium")
                        c = play_track[i][j + 1].split().count("large")
                        d = play_track[i][j - 1].split().count("large")
                        e = play_track[i][j + 1].split().count("small")

                        f = play_track[j][i - 1].split().count("small")
                        g = play_track[j][i].split().count("medium")
                        h = play_track[j][i + 1].split().count("large")
                        i = play_track[j][i - 1].split().count("large")
                        j = play_track[j][i + 1].split().count("small")

                        k = play_track[i - 1][i + 1].split().count("small")
                        l = play_track[i][3 - 1 - i].split().count("medium")
                        m = play_track[i + 1][3 - i].split().count("large")
                        n = play_track[i - 1][i + 1].split().count("large")
                        o = play_track[i + 1][3 - i].split().count("small")
                        if (a + b + c == 3) or (b + d + e == 3) or (f + g + h == 3) or (i + j + g == 3) or (k + l + m == 3) or (n + o + l == 3):
                            active = False
                            break

            while i == 2 and j == 2:
                        a = play_track[i][j - 2].split().count("small")
                        b = play_track[i][j - 1].split().count("medium")
                        c = play_track[i][j].split().count("large")
                        d = play_track[i][j - 2].split().count("large")
                        e = play_track[i][j].split().count("small")

                        f = play_track[j][i - 2].split().count("small")
                        g = play_track[j][i - 1].split().count("medium")
                        h = play_track[j][i].split().count("large")
                        i = play_track[j][i - 2].split().count("large")
                        j = play_track[j][i].split().count("small")
                        if (a + b + c == 3) or (b + d + e == 3) or (f + g + h == 3) or (i + j + g == 3):
                            active = False
                            break

            if active == False:
                break


average = counter/100
print("Over with an aevrage pace of: " + str(average))    

    

