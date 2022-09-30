import random
from turtle import pos

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

def Main():

    #generate random positions for the 3 peices without repeating same coords 
    rng_pos = []
    while len(rng_pos) < 3:
        point = (random.randrange(8), random.randrange(8))
        if point not in rng_pos:
            rng_pos.append(point)
    
    queen_pos = {"x":rng_pos[0][1], "y":rng_pos[0][0]}
    queen_pos["Cell"] = chess_coordinates[queen_pos['y']][queen_pos['x']]

    king_pos = {"x":rng_pos[1][1], "y":rng_pos[1][0]}
    king_pos["Cell"] = chess_coordinates[king_pos['y']][king_pos['x']]
    
    extra_pos = {"x":rng_pos[2][1], "y":rng_pos[2][0]}
    extra_pos["Cell"] = chess_coordinates[extra_pos['y']][extra_pos['x']]

    if True: #debug 
        print(f"Queen pos: {queen_pos['Cell']} ({queen_pos['x']},{queen_pos['y']})")
        print(f"King pos: {king_pos['Cell']} ({king_pos['x']},{king_pos['y']})")
        print(f"Extra pos: {extra_pos['Cell']} ({extra_pos['x']},{extra_pos['y']})")
    
    #--------------------------------------------------------------------


    

    def CalculateQueenPositions():
        positions = []

        #check vertical
        for y in range(8):
            #cur_pos = (y,queen_pos["x"])
            if queen_pos["y"] != y:
                positions.append(chess_coordinates[y][queen_pos["x"]])
                if chess_coordinates[y][queen_pos["x"]] == king_pos["Cell"]:
                    print("coll")
                    break
                
        #check horizontal  
        for x in range(8):
            if queen_pos["x"] != x:
                positions.append(chess_coordinates[queen_pos["y"]][x])
            
       
        
        
        
        return positions

    print(CalculateQueenPositions())


    
for i in range(1):
    Main()




