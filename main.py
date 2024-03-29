import generator

#set to False si quiere que el trablero y movimientos se muestren en la consola en vez de en un GUI
USE_UI = True 


#generar el estado del juego usando el modulo "generator" que cree y salvarlo en una variable (la funcion regresa un diccionario com toda la info del juego)
game_info = generator.generateGame()


if USE_UI:

    import pygame 
    #iniciar pygame 
    pygame.init()

    #definir el tamaño de la pantalla
    screen = pygame.display.set_mode((600,800))
    #ponerle nombre a la pantalla
    pygame.display.set_caption("Simulador Ajedrez")


    #crear clock para limitar el framerate del juego 
    clock = pygame.time.Clock()

    #crear fonts para los textos que se van a mostrar en la pantalla
    font = pygame.font.SysFont("segoeuisymbol", 40)
    font_moves = pygame.font.SysFont("segoeuisymbol", 10)
    font_titles = pygame.font.SysFont("segoeuisymbol", 30)


    #funcion que dibuja el tablero cada frame
    def drawBoard():

        #dibujar tablero 
        i = 0
        for x in range(8):
            for y in range(8):

                if i%2 == 0:
                    pygame.draw.rect(screen, "White", pygame.Rect(x*50+100, y*50+100, 50, 50))
                else:
                    pygame.draw.rect(screen, "Black", pygame.Rect(x*50+100, y*50+100, 50, 50))
                i +=1
            i -=1


        #dibujar numeros 
        for i, x in enumerate(reversed(range(8))):
            screen.blit(font.render(str(x+1), True, "Black"),(60, i*50+100 -5))
            screen.blit(font.render(str(x+1), True, "Black"),(520, i*50+100 -5))


        #dibujar letras
        letters = ["A","B","C","D","E","F","G","H"]
        for y in range(8):
            screen.blit(font.render(letters[y], True, "Black"),(y*50+100+10, 40))
            screen.blit(font.render(letters[y], True, "Black"),(y*50+100+10, 500))


        #hacer parte de abajo blanca (donde van los movimientos de las piezas )
        pygame.draw.rect(screen, "White", pygame.Rect(0, 550, 600, 300))
        

    #funcion que dibuja los movimientos possibles de cada pieza cada frame 
    def drawMoves():

        #dibujar movimientos de reina 
        for move in game_info["queen_moves"]:
            pygame.draw.circle(screen, "Red", (move["x"]*50 +125, move["y"]*50 +125), 8)
        
        #dibujar movimientos de rey 
        for move in game_info["king_moves"]:
            pygame.draw.circle(screen, "Blue", (move["x"]*50 +125, move["y"]*50 +125), 8)
        
        #dibujar movimientos de torre 
        for move in game_info["extra_moves"]:
            pygame.draw.circle(screen, "Blue", (move["x"]*50 +125, move["y"]*50 +125), 12, 2)


    #funcion que dibuja las piezas en el tablero cada frame 
    def drawPieces():
        
        #dibujar reina 
        screen.blit(font.render("♛", True, "Red"),(game_info["qpx"]*50+100 +5, game_info["qpy"]*50+100 -5))
        #dibujar rey
        screen.blit(font.render("♚", True, "Blue"),(game_info["kpx"]*50+100 +5, game_info["kpy"]*50+100 -5))
        #dibujar torre
        screen.blit(font.render("♜", True, "Blue"),(game_info["epx"]*50+100 +5, game_info["epy"]*50+100 -5))


    #funcion que dibuja el texto de los movimientos posibles de cada pieza 
    def drawMovesText():
    
        #mostrar que ENTER genera nuevas posiciones
        screen.blit(font_titles.render("[Pulsa ENTER para generar un juego nuevo]" , True, "Black"),(10, 0))

        #mostrar texto que dice si el rey esta en jaque
        jaque = "[El Rey esta en jaque]" if game_info["en_jaque"] else "[El Rey no esta en jaque]"
        screen.blit(font_titles.render(jaque , True, "Black"),(10, 550))

        #mostrar texto que dice si la torre puede hacer una jugada
        jugada = "[La Torre no puede hacer una jugada]" if game_info["extra_jugada"] == False else f'[La Torre puede hacer una jugada-({game_info["q_cell"]})]'
        screen.blit(font_titles.render(jugada , True, "Black"),(10, 580))


        #mostrar info de la reina 
        queen_moves = ""
        for move in game_info["queen_moves"]:
            queen_moves += f'[{move["Cell"]}] '
        screen.blit(font.render("Reina-["+game_info["q_cell"] + "]", True, "Black"),(10, 550+60))
        screen.blit(font_moves.render(queen_moves, True, "Black"),(10, 600+60))

        #mostrar info del rey 
        king_moves = ""
        for move in game_info["king_moves"]:
            king_moves += f'[{move["Cell"]}] '
        screen.blit(font.render("Rey-["+game_info["k_cell"] + "]", True, "Black"),(10, 550+120))
        screen.blit(font_moves.render(king_moves, True, "Black"),(10, 600+122))

        #mostrar info de la torre  
        extra_moves = ""
        for move in game_info["extra_moves"]:
            extra_moves += f'[{move["Cell"]}] '
        screen.blit(font.render("Torre-["+game_info["e_cell"] + "]", True, "Black"),(10, 550+180))
        screen.blit(font_moves.render(extra_moves, True, "Black"),(10, 600+180))
        

    #-------------------------------------------------------------------------------------

    #loop en donde se dibujan las cosas en pygame 
    while True:

        #llenar el fondo de color gris
        screen.fill("Grey")


        for event in pygame.event.get():
            #detectar si el usuario le pico al botton de cerrar pantalla 
            if event.type == pygame.QUIT:
                #cerrar pantalla 
                pygame.quit()
                exit()
            #detectar si se pulso la tecla ENTER
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #si se pulso la teca ENTER generar otra vez el juego y salvarlo en la variable de game_info
                    game_info = generator.generateGame()
                    


        #llamar a la funcion que dibuja el tablero
        drawBoard()

        #llamar a la funcion que dibuja las piezas en el tablero 
        drawPieces()

        #llamar a la funcion que dibuja los movimientos possibles de las piezas
        drawMoves()

        #llamar a la funcion que muestra el texto de los possibles movimientos
        drawMovesText()
        

        #actualizar pantalla con todo lo que se dibujo
        pygame.display.update() 

        #limitar a que el loop solo pueda correr 60 veces por segundo
        clock.tick(60)

else:
    while True:
        
        #mostrar posiciones inicales
        print("\n\n\n-----------Posiciones iniciales-----------")
        print(f"Reina-[{game_info['q_cell']}]")
        print(f"Rey---[{game_info['k_cell']}]")
        print(f"Torre-[{game_info['e_cell']}]")

        #crear matriz del tablero 
        tablero = [
            ["⬜","⬛","⬜","⬛","⬜","⬛","⬜","⬛"],
            ["⬛","⬜","⬛","⬜","⬛","⬜","⬛","⬜"],
            ["⬜","⬛","⬜","⬛","⬜","⬛","⬜","⬛"],
            ["⬛","⬜","⬛","⬜","⬛","⬜","⬛","⬜"],
            ["⬜","⬛","⬜","⬛","⬜","⬛","⬜","⬛"],
            ["⬛","⬜","⬛","⬜","⬛","⬜","⬛","⬜"],
            ["⬜","⬛","⬜","⬛","⬜","⬛","⬜","⬛"],
            ["⬛","⬜","⬛","⬜","⬛","⬜","⬛","⬜"],
        ]
        
        #actulizar la matriz del tablero para poner las piezas (0,5)
        for x in range(8):
            for y in range(8):

                if (x,y) == (game_info["qpx"],game_info["qpy"]):
                    tablero[y][x] = "♕ "
                elif (x,y) == (game_info["kpx"],game_info["kpy"]):
                    tablero[y][x] = "♚ "
                elif (x,y) == (game_info["epx"],game_info["epy"]):
                    tablero[y][x] = "♜ "
                    
        
        #imprimir matriz de tablero 
        print("\n-----------------Tablero------------------")
        print("   A B C D E F G H")
        for i, line in enumerate(tablero):
            print(f"{9-(i+1)} {''.join(line)} {9-(i+1)}")
        print("   A B C D E F G H")

        #imprimir movimientos
        print("\n-----------Posibles Movimientos------------")
        print("[Reina]-"+",".join(list(move["Cell"] for move in game_info["queen_moves"])))
        print("[Rey]-"+",".join(list(move["Cell"] for move in game_info["king_moves"])))
        print("[Torre]-"+",".join(list(move["Cell"] for move in game_info["extra_moves"])))

        #imprimir estatus del juego 
        print("\n------------Estatus del juego--------------")
        print("[El Rey esta en jaque]" if game_info["en_jaque"] else "[El Rey no esta en jaque]")
        print("[La Torre no puede hacer una jugada]" if game_info["extra_jugada"] == False else f'[La Torre puede hacer una jugada-({game_info["q_cell"]})]')
        print("-------------------------------------------")

        print("\n\n")
        input("--[Pulse ENTER para generar un juego nuevo]--")
        game_info = generator.generateGame()
