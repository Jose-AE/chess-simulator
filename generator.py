#importar el modulo random 
import random

#definir una matriz con las cordenadas del ajedrez para convertir cordenadas (x,y) a el numero y letra que le coresponde 
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

#definir la variable de si el rey esta en jaque 
en_jaque = False


#funcion que genera el juego y regresa un diccionario con toda la informacion sobre el juego que se genero
def generateGame():

    #definir que en en_jaque es la variable que esta afuera de la funcion
    global en_jaque 
    #reiniciar la variable de _en_jaque a false cada ves que se genere un juego nuevo 
    en_jaque = False


    #generar posiciones aleatorias para cada pieza sin que se repitan
    rng_pos = []
    while len(rng_pos) < 3:
        point = (random.randrange(8), random.randrange(8))
        if point not in rng_pos:
            rng_pos.append(point)
    
    queen_pos = {"x":rng_pos[0][1], "y":rng_pos[0][0]}##  {"x":1, "y":6}##
    queen_pos["Cell"] = chess_coordinates[queen_pos['y']][queen_pos['x']]

    king_pos = {"x":rng_pos[1][1], "y":rng_pos[1][0]}##{"x":3, "y":5}##
    king_pos["Cell"] = chess_coordinates[king_pos['y']][king_pos['x']]
    
    extra_pos =  {"x":rng_pos[2][1], "y":rng_pos[2][0]}##{"x":2, "y":5}##
    extra_pos["Cell"] = chess_coordinates[extra_pos['y']][extra_pos['x']]

    #debug para imprimir las posiciones de las piezas
    if False: 
        print(f"Queen pos: {queen_pos['Cell']} ({queen_pos['x']},{queen_pos['y']})")
        print(f"King pos: {king_pos['Cell']} ({king_pos['x']},{king_pos['y']})")
        print(f"Extra pos: {extra_pos['Cell']} ({extra_pos['x']},{extra_pos['y']})")
    

    #funcion que genera todas las posiciones possibles de la reina sin tomar en cuenta al rey
    def calculateQueenPositionsExcludingKing():
        #crear lista en donde se van a ir agregando cada una de las posiciones a las que la reina se puede mover
        positions = [] 

        #agregar celdas que esten arriba de la reina
        for y in range(queen_pos["y"]-1,-1,-1):
            cur_pos = (queen_pos["x"],y)
            positions.append( {"x":queen_pos["x"],"y":y,"Cell":chess_coordinates[y][queen_pos["x"]] }  ) 
            #revisar si hay colisiones con la torre, si si romper el ciclo   
            if cur_pos == (extra_pos["x"],extra_pos["y"]):
                break

        #agregar celdas que esten abajo de la reina
        for y in range(queen_pos["y"]+1,8):
            cur_pos = (queen_pos["x"],y)
            positions.append( {"x":queen_pos["x"],"y":y,"Cell":chess_coordinates[y][queen_pos["x"]] }  ) 
            #revisar si hay colisiones con la torre, si si romper el ciclo   
            if cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break

        #agregar celdas que esten a la derecha de la reina
        for x in range(queen_pos["x"]+1,8):
            cur_pos = (x,queen_pos["y"])
            positions.append( {"x":x,"y":queen_pos["y"],"Cell":chess_coordinates[queen_pos['y']][x] }  ) 
            #revisar si hay colisiones con la torre, si si romper el ciclo  
            if cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break
        
        #agregar celdas que esten a la izquierda de la reina
        for x in range(queen_pos["x"]-1,-1,-1):
            cur_pos = (x,queen_pos["y"])
            positions.append( {"x":x,"y":queen_pos["y"],"Cell":chess_coordinates[queen_pos['y']][x] }  ) 
            #revisar si hay colisiones con la torre, si si romper el ciclo
            if cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break

        #agregar celdas que esten arriba a la derecha de la reina
        def checkTopRight(x,y):
            if not (x+1 > 8 or y-1 < -1):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                #revisar si hay colisiones con la torre, si si salir de la recursion
                if (x,y) != (extra_pos["x"], extra_pos["y"]):
                    checkTopRight(x+1 , y-1)

        checkTopRight(queen_pos["x"]+1,queen_pos["y"]-1)

        #agregar celdas que esten arriba a la izquierda de la reina
        def checkTopLeft(x,y):
            if not (x-1 < -1 or y-1 < -1):  # x-1 > 8 or y-1 < -1
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                #revisar si hay colisiones con la torre, si si salir de la recursion
                if (x,y) != (extra_pos["x"], extra_pos["y"] ):
                    checkTopLeft(x-1 , y-1)

        checkTopLeft(queen_pos["x"]-1,queen_pos["y"]-1)
        
        
        #agregar celdas que esten abajo a la izquierda de la reina
        def checkBottomLeft(x,y):
            if not (x-1 < -1 or y+1 > 8):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                #revisar si hay colisiones con la torre, si si salir de la recursion
                if (x,y) != (extra_pos["x"],extra_pos["y"] ):
                    checkBottomLeft(x-1 , y+1)

        checkBottomLeft(queen_pos["x"]-1,queen_pos["y"]+1)

        #agregar celdas que esten abajo a la derecha de la reina
        def checkBottomLeft(x,y):
            if not (x+1 > 8 or y +1 > 8):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                #revisar si hay colisiones con la torre, si si salir de la recursion
                if (x,y) != (extra_pos["x"],extra_pos["y"] ):
                    checkBottomLeft(x+1 , y+1)

        checkBottomLeft(queen_pos["x"]+1,queen_pos["y"]+1)

        #regresar las posiciones a las que la reina se puede mover
        return positions

    #funcion que genera todas las posiciones possibles de la reina 
    def calculateQueenPositions():
        #crear lista en donde se van a ir agregando cada una de las posiciones a las que la reina se puede mover
        positions = []

        #agregar celdas que esten arriba de la reina
        for y in range(queen_pos["y"]-1,-1,-1):
            cur_pos = (queen_pos["x"],y)
            positions.append( {"x":queen_pos["x"],"y":y,"Cell":chess_coordinates[y][queen_pos["x"]] }  ) 
            #revisar si hay colisiones con la torre o el rey, si si romper el ciclo
            if cur_pos == (king_pos["x"],king_pos["y"]) or cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break

        #agregar celdas que esten abajo de la reina
        for y in range(queen_pos["y"]+1,8):
            cur_pos = (queen_pos["x"],y)
            positions.append( {"x":queen_pos["x"],"y":y,"Cell":chess_coordinates[y][queen_pos["x"]] }  ) 
            #revisar si hay colisiones con la torre o el rey, si si romper el ciclo
            if cur_pos == (king_pos["x"],king_pos["y"]) or cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break

        #agregar celdas que esten a la derecha de la reina
        for x in range(queen_pos["x"]+1,8):
            cur_pos = (x,queen_pos["y"])
            positions.append( {"x":x,"y":queen_pos["y"],"Cell":chess_coordinates[queen_pos['y']][x] }  ) 
            #revisar si hay colisiones con la torre o el rey, si si romper el ciclo
            if cur_pos == (king_pos["x"],king_pos["y"]) or cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break
        
        #agregar celdas que esten a la izquierda de la reina
        for x in range(queen_pos["x"]-1,-1,-1):
            #continue
            cur_pos = (x,queen_pos["y"])
            positions.append( {"x":x,"y":queen_pos["y"],"Cell":chess_coordinates[queen_pos['y']][x] }  ) 
            #revisar si hay colisiones con la torre o el rey, si si romper el ciclo
            if cur_pos == (king_pos["x"],king_pos["y"]) or cur_pos == (extra_pos["x"],extra_pos["y"] ):
                break

        #agregar celdas que esten arriba a la derecha de la reina
        def checkTopRight(x,y):
            if not (x+1 > 8 or y-1 < -1):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                #revisar si hay colisiones con la torre o el rey, si si salir de la recursion
                if (x,y) != (king_pos["x"],king_pos["y"]) and (x,y) != (extra_pos["x"], extra_pos["y"]):
                    checkTopRight(x+1 , y-1)

        checkTopRight(queen_pos["x"]+1,queen_pos["y"]-1)

        #agregar celdas que esten arriba a la izquierda de la reina
        def checkTopLeft(x,y):
            if not (x-1 < -1 or y-1 < -1):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                #revisar si hay colisiones con la torre o el rey, si si salir de la recursion
                if (x,y) != (king_pos["x"],king_pos["y"]) and (x,y) != (extra_pos["x"], extra_pos["y"] ):
                    checkTopLeft(x-1 , y-1)

        checkTopLeft(queen_pos["x"]-1,queen_pos["y"]-1)
        
        #agregar celdas que esten abajo a la izquierda de la reina
        def checkBottomLeft(x,y):
            #return
            if not (x-1 < -1 or y+1 > 8):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                #revisar si hay colisiones con la torre o el rey, si si salir de la recursion
                if (x,y) != (king_pos["x"],king_pos["y"]) and (x,y) != (extra_pos["x"],extra_pos["y"] ):
                    checkBottomLeft(x-1 , y+1)


        checkBottomLeft(queen_pos["x"]-1,queen_pos["y"]+1)

        #agregar celdas que esten abajo a la derecha de la reina
        def checkBottomLeft(x,y):
            #return
            if not (x+1 > 8 or y +1 > 8):
                positions.append({"x":x,"y":y,"Cell":chess_coordinates[y][x] })
                #revisar si hay colisiones con la torre, si si salir de la recursion
                if (x,y) != (king_pos["x"],king_pos["y"]) and (x,y) != (extra_pos["x"],extra_pos["y"] ):
                    checkBottomLeft(x+1 , y+1)

        checkBottomLeft(queen_pos["x"]+1,queen_pos["y"]+1)

        #regresar las posiciones a las que la reina se puede mover
        return positions

    #funcion que genera todas las posiciones possibles de el rey
    def calculateKingPositions():
        #crear lista en donde se van a ir agregando cada una de las posiciones a las que el rey se puede mover
        positions = []
        
        #generar una lista de todas las posiciones a donde la reina se puede mover excluyendo al rey
        queen_positions = [pos["Cell"] for pos in calculateQueenPositionsExcludingKing() ]

        #ver si el rey esta en jaque (si la pos del rey esta en la lista de posisciones que la reina )
        global en_jaque
        if chess_coordinates[king_pos["y"]][king_pos["x"]] in queen_positions:
            en_jaque = True

        #agregar celdas adyacentes al rey 
        for row in range(-1,2):
            for col in range(-1,2):
                x = row + king_pos["x"]
                y = col + king_pos["y"]

                #no incluir la pos del rey
                if (x,y) == (king_pos["x"],king_pos["y"]): 
                    continue
                
                #poner limites para que no agregue celdas fuera del tablero 
                if (x>7 or x<0) or (y>7 or y<0):
                    continue
                
                #si se fuera a agregar una celda donde la reina se puede mover, que no lo haga
                cur_cell = chess_coordinates[y][x]
                if cur_cell in queen_positions:
                    continue
                #si la torre esta alado no agregar esa celda 
                if (x,y) == (extra_pos["x"],extra_pos["y"]):
                    continue

                #agergar posicion a la lista de posiciones
                positions.append( {"x":x,"y":y,"Cell":cur_cell }  ) 
                
        #regresar las posiciones a las que el rey se puede mover
        return positions

    #funcion que genera todas las posiciones possibles de la torre
    def calculateExtraPositions():
        #crear lista en donde se van a ir agregando cada una de las posiciones a las que la torre se puede mover
        positions = []

        #agregar celdas que esten arriba de la torre
        for y in range(extra_pos["y"]-1,-1,-1):
            cur_pos = (extra_pos["x"],y)
            #si se fuera a agregar la celda donde el rey esta romper el ciclo
            if cur_pos == (king_pos["x"],king_pos["y"]):
                break
            positions.append( {"x":extra_pos["x"],"y":y,"Cell":chess_coordinates[y][extra_pos["x"]] }  ) 
            #si se agrega la posicion donde la reina esta romper el ciclo
            if cur_pos == (queen_pos["x"],queen_pos["y"]):
                break


        #agregar celdas que esten abajo de la torre
        for y in range(extra_pos["y"]+1,8):
            cur_pos = (extra_pos["x"],y)
            #si se fuera a agregar la celda donde el rey esta romper el ciclo
            if cur_pos == (king_pos["x"],king_pos["y"]):
                break
            positions.append( {"x":extra_pos["x"],"y":y,"Cell":chess_coordinates[y][extra_pos["x"]] }  ) 
            #si se agrega la posicion donde la reina esta romper el ciclo
            if cur_pos == (queen_pos["x"],queen_pos["y"]):
                break#check king and extra collision 
            

        #agregar celdas que esten a la derecha de la torre
        for x in range(extra_pos["x"]+1,8):
            cur_pos = (x,extra_pos["y"])
            #si se fuera a agregar la celda donde el rey esta romper el ciclo
            if cur_pos == (king_pos["x"],king_pos["y"]):
                break
            positions.append( {"x":x,"y":extra_pos["y"],"Cell":chess_coordinates[extra_pos['y']][x] }  ) 
            #si se agrega la posicion donde la reina esta romper el ciclo
            if cur_pos == (queen_pos["x"],queen_pos["y"]):
                break
        
        #agregar celdas que esten a la izquierda de la torre
        for x in range(extra_pos["x"]-1,-1,-1):
            cur_pos = (x,extra_pos["y"])
            #si se fuera a agregar la celda donde el rey esta romper el ciclo
            if cur_pos == (king_pos["x"],king_pos["y"]):
                break
            positions.append( {"x":x,"y":extra_pos["y"],"Cell":chess_coordinates[extra_pos['y']][x] }  ) 
            #si se agrega la posicion donde la reina esta romper el ciclo
            if cur_pos == (queen_pos["x"],queen_pos["y"]):
                break
        

        #regresar las posiciones a las que la torre se puede mover
        return positions


    #regresar toda la informacion sobre el juego que se genero 
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
        "extra_moves": calculateExtraPositions(),
        "en_jaque": en_jaque
        }







