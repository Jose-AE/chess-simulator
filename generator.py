
import random



chess_coordinates = (
    ("A8","B8","C8","D8","E8","F8","G8","H8"),
    ("A7","B7","C7","D7","E7","F7","G7","H7"),
    ("A6","B6","C6","D6","E6","F6","G6","H6"),
    ("A5","B5","C5","D5","E5","F5","G5","H5"),
    ("A4","B4","C4","D4","E4","F4","G4","H4"),
    ("A3","B3","C3","D3","E3","F3","G3","H3"),
    ("A2","B2","C2","D2","E2","F2","G2","H2"),
    ("A1","B1","C1","D1","E1","F1","G1","H1")
)

en_jaque = False

def generateGame():

    global en_jaque 

    en_jaque = False

    #generate random positions for the 3 peices without repeating same coords 
    rng_pos = []
    while len(rng_pos) < 3:
        point = (random.randrange(8), random.randrange(8))
        if point not in rng_pos:
            rng_pos.append(point)
    
    queen_pos = {"x":rng_pos[0][1], "y":rng_pos[0][0]} ##  {"x":0, "y":0}##
    queen_pos["Cell"] = chess_coordinates[queen_pos['y']][queen_pos['x']]

    king_pos = {"x":rng_pos[1][1], "y":rng_pos[1][0]}##{"x":7, "y":0}##
    king_pos["Cell"] = chess_coordinates[king_pos['y']][king_pos['x']]
    
    extra_pos = {"x":rng_pos[2][1], "y":rng_pos[2][0]}
    extra_pos["Cell"] = chess_coordinates[extra_pos['y']][extra_pos['x']]

    if False: #debug 
        print(f"Queen pos: {queen_pos['Cell']} ({queen_pos['x']},{queen_pos['y']})")
        print(f"King pos: {king_pos['Cell']} ({king_pos['x']},{king_pos['y']})")
        print(f"Extra pos: {extra_pos['Cell']} ({extra_pos['x']},{extra_pos['y']})")
    
    #--------------------------------------------------------------------


    

    def calculateQueenPositions():
        positions = []

        #check top
        for y in range(queen_pos["y"]-1,-1,-1):
            #continue
            cur_pos = (queen_pos["x"],y)
            positions.append( {"x":queen_pos["x"],"y":y,"Cell":chess_coordinates[y][queen_pos["x"]] }  ) 
            #check king and extra collision  
            if cur_pos == (king_pos["x"],king_pos["y"]) or cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break

        #check bottom
        for y in range(queen_pos["y"]+1,8):
            #continue
            cur_pos = (queen_pos["x"],y)
            positions.append( {"x":queen_pos["x"],"y":y,"Cell":chess_coordinates[y][queen_pos["x"]] }  ) 
            #check king and extra collision 
            if cur_pos == (king_pos["x"],king_pos["y"]) or cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break

        #check right
        for x in range(queen_pos["x"]+1,8):
            #continue
            cur_pos = (x,queen_pos["y"])
            positions.append( {"x":x,"y":queen_pos["y"],"Cell":chess_coordinates[queen_pos['y']][x] }  ) 
            #check king and extra collision 
            if cur_pos == (king_pos["x"],king_pos["y"]) or cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break
        
        #check left 
        for x in range(queen_pos["x"]-1,-1,-1):
            #continue
            cur_pos = (x,queen_pos["y"])
            positions.append( {"x":x,"y":queen_pos["y"],"Cell":chess_coordinates[queen_pos['y']][x] }  ) 
            #check king and extra collision 
            if cur_pos == (king_pos["x"],king_pos["y"]) or cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break

        #check top right 
        def checkTopRight(x,y):
            #return
            if not (x+1 > 8 or y-1 < -1):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                if (x,y) != (king_pos["x"],king_pos["y"]) and (x,y) != (extra_pos["x"], extra_pos["y"]):
                    checkTopRight(x+1 , y-1)

        checkTopRight(queen_pos["x"]+1,queen_pos["y"]-1)

        
        #check top left 
        def checkTopLeft(x,y):
            #return
            #-1, -1
            if not (x-1 < -1 or y-1 < -1):  # x-1 > 8 or y-1 < -1
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                if (x,y) != (king_pos["x"],king_pos["y"]) and (x,y) != (extra_pos["x"], extra_pos["y"] ):
                    checkTopLeft(x-1 , y-1)

        checkTopLeft(queen_pos["x"]-1,queen_pos["y"]-1)
        
        

        #check bottom left 
        def checkBottomLeft(x,y):
            #return
            if not (x-1 < -1 or y+1 > 8):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                if (x,y) != (king_pos["x"],king_pos["y"]) and (x,y) != (extra_pos["x"],extra_pos["y"] ):
                    checkBottomLeft(x-1 , y+1)


        checkBottomLeft(queen_pos["x"]-1,queen_pos["y"]+1)

        #check bottom Right 
        def checkBottomLeft(x,y):
            #return
            if not (x+1 > 8 or y +1 > 8):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                if (x,y) != (king_pos["x"],king_pos["y"]) and (x,y) != (extra_pos["x"],extra_pos["y"] ):
                    checkBottomLeft(x+1 , y+1)

        checkBottomLeft(queen_pos["x"]+1,queen_pos["y"]+1)

        return positions

    def calculateKingPositions():
        
        positions = []
        
        #get queen positions 
        queen_positions = [pos["Cell"] for pos in calculateQueenPositions() ]

        #check if king is in jaque 
        global en_jaque
        if chess_coordinates[king_pos["y"]][king_pos["x"]] in queen_positions:
            en_jaque = True

        
        for row in range(-1,2):
            for col in range(-1,2):
                x = row + king_pos["x"]
                y = col + king_pos["y"]

                if (x,y) == (king_pos["x"],king_pos["y"]): 
                    continue
                
                if (x>7 or x<0) or (y>7 or y<0):
                    continue
                
                #if were to move to queen pos: dont
                cur_cell = chess_coordinates[y][x]
                if cur_cell in queen_positions:
                    continue


                positions.append( {"x":x,"y":y,"Cell":cur_cell }  ) 
                

        return positions
        


    return {
        "qpx":queen_pos["x"], 
        "qpy":queen_pos["y"],
        "q_cell":chess_coordinates[queen_pos['y']][queen_pos["x"]],
        "kpx":king_pos["x"], 
        "kpy":king_pos["y"],
        "k_cell":chess_coordinates[king_pos['y']][king_pos["x"]],
        "epx":extra_pos["x"], 
        "epy":extra_pos["y"],
        "e_cell":chess_coordinates[extra_pos['y']][extra_pos["x"]],
        "queen_moves": calculateQueenPositions(),
        "king_moves": calculateKingPositions(),
        "extra_moves": calculateKingPositions(),
        "en_jaque": en_jaque
        }


    
#generateGame()




