import pygame
import generator

pygame.init()
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("Ajedrez")

clock = pygame.time.Clock()
font = pygame.font.SysFont("segoeuisymbol", 40)
font_moves = pygame.font.SysFont("segoeuisymbol", 10)
font_titles = pygame.font.SysFont("segoeuisymbol", 30)



def drawBoard():
    i = 0
    for x in range(8):
        for y in range(8):

            if i%2 == 0:
                pygame.draw.rect(screen, "White", pygame.Rect(x*50+100, y*50+100, 50, 50))
            else:
                pygame.draw.rect(screen, "Black", pygame.Rect(x*50+100, y*50+100, 50, 50))
            i +=1
        i -=1


    for i, x in enumerate(reversed(range(8))):
        screen.blit(font.render(str(x+1), True, "Black"),(60, i*50+100 -5))
        screen.blit(font.render(str(x+1), True, "Black"),(520, i*50+100 -5))


    letters = ["A","B","C","D","E","F","G","H"]
    for y in range(8):
        screen.blit(font.render(letters[y], True, "Black"),(y*50+100+10, 40))
        screen.blit(font.render(letters[y], True, "Black"),(y*50+100+10, 500))


    #info box
    pygame.draw.rect(screen, "White", pygame.Rect(0, 550, 600, 300))
       
    
def drawMoves():
    #draw moves 

    for move in game_info["queen_moves"]:
        pygame.draw.circle(screen, "Red", (move["x"]*50 +125, move["y"]*50 +125), 10)
    
    for move in game_info["king_moves"]:
        pygame.draw.circle(screen, "Blue", (move["x"]*50 +125, move["y"]*50 +125), 8)
    

    for move in game_info["extra_moves"]:
        pygame.draw.circle(screen, "Blue", (move["x"]*50 +125, move["y"]*50 +125), 8)



def drawPieces():
    
    #draw queen
    screen.blit(font.render("♛", True, "Red"),(game_info["qpx"]*50+100 +5, game_info["qpy"]*50+100 -5))
    #draw king
    screen.blit(font.render("♚", True, "Blue"),(game_info["kpx"]*50+100 +5, game_info["kpy"]*50+100 -5))
    #draw extra
    screen.blit(font.render("♜", True, "Blue"),(game_info["epx"]*50+100 +5, game_info["epy"]*50+100 -5))



def drawMovesText():
 
    #display game reset info
    screen.blit(font_titles.render("[Pulsa ENTER para generar un juego nuevo]" , True, "Black"),(10, 0))


    
    #display if king is en jaque 
    jaque = "[EL REY ESTA EN JAQUE]" if game_info["en_jaque"] else "[EL REY NO ESTA EN JAQUE]"
    screen.blit(font.render(jaque , True, "Black"),(10, 550))


    #display queen info 
    queen_moves = ""
    for move in game_info["queen_moves"]:
        queen_moves += f'[{move["Cell"]}] '
    screen.blit(font.render("Reina-["+game_info["q_cell"] + "]", True, "Black"),(10, 550+50))
    screen.blit(font_moves.render(queen_moves, True, "Black"),(10, 600+50))
    
    #display king info
    king_moves = ""
    for move in game_info["king_moves"]:
        king_moves += f'[{move["Cell"]}] '
    screen.blit(font.render("Rey-["+game_info["k_cell"] + "]", True, "Black"),(10, 550+110))
    screen.blit(font_moves.render(king_moves, True, "Black"),(10, 600+111))

    #display estra moves
    extra_moves = ""
    for move in game_info["extra_moves"]:
        extra_moves += f'[{move["Cell"]}] '
    screen.blit(font.render("Torre-["+game_info["e_cell"] + "]", True, "Black"),(10, 550+170))
    screen.blit(font_moves.render(extra_moves, True, "Black"),(10, 600+170))
    


game_info = generator.generateGame()



while True:

    screen.fill("Grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_info = generator.generateGame()
                


    
    drawBoard()
    drawPieces()
    drawMoves()
    drawMovesText()
    


    pygame.display.update() 
    clock.tick(60)