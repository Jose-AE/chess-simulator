
king_pos = {"x":4, "y":4}##{"x":7, "y":0}##

for row in range(-1,2):
    for col in range(-1,2):
        x = row + king_pos["x"]
        y = col + king_pos["y"]
        
        if (x,y) == (king_pos["x"],king_pos["y"]): 
            continue
        
        if (x>7 or x<0) or (y>7 or y<0):
            continue


        print(x,y)

