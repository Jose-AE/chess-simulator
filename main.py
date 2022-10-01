import pygame
import random
import generator

pygame.init()
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("Ajedrez")

clock = pygame.time.Clock()
font = pygame.font.SysFont("segoeuisymbol", 40)
font_moves = pygame.font.SysFont("segoeuisymbol", 10)


def DrawBoard():
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
       
    

def DrawPiece(piece, x, y, color):
    

    #draw moves 
    screen.blit(font.render(piece, True, color),(x*50+100 +5, y*50+100 -5))

    if piece == "♛":
        for move in game_info["queen_moves"]:
            pygame.draw.circle(screen, color, (move["x"]*50 +125, move["y"]*50 +125), 10)


def drawMovesText():
 

 
    #display queen info 
    queen_moves = ""
    for move in game_info["queen_moves"]:
        queen_moves += f'[{move["Cell"]}] '
    screen.blit(font.render("Queen-["+game_info["q_cell"] + "]", True, "Black"),(10, 550+50))
    screen.blit(font_moves.render(queen_moves, True, "Black"),(10, 600+50))
    

    king_moves = ""
    for move in game_info["king_moves"]:
        king_moves += f'[{move["Cell"]}] '
    screen.blit(font.render("King-["+game_info["k_cell"] + "]", True, "Black"),(10, 550+100))
    screen.blit(font_moves.render(queen_moves, True, "Black"),(10, 600+100))

    extra_moves = ""
    for move in game_info["extra_moves"]:
        extra_moves += f'[{move["Cell"]}] '
    screen.blit(font.render("Extra-["+game_info["e_cell"] + "]", True, "Black"),(10, 550+150))
    screen.blit(font_moves.render(queen_moves, True, "Black"),(10, 600+150))
    


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

    
    DrawBoard()
    DrawPiece("♛", game_info["qpx"],game_info["qpy"], "Red")
    DrawPiece("♚", game_info["kpx"],game_info["kpy"], "Blue")
    DrawPiece("♜", game_info["epx"],game_info["epy"], "Blue")
    drawMovesText()


    pygame.display.update() 
    clock.tick(60)