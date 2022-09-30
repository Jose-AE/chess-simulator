#
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("Ajedrez")

clock = pygame.time.Clock()
font = pygame.font.SysFont("segoeuisymbol", 40)



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
       
    

def DrawPiece(piece, x, y):
    screen.blit(font.render(piece, True, "Red"),(x*50+100 +5, y*50+100 -5))


def NewGame():
    global queen_pos
    global king_pos
    global extra_pos


    queen_pos = (random.randrange(8),random.randrange(8))
    queen_pos = (random.randrange(8),random.randrange(8))
    queen_pos = (random.randrange(8),random.randrange(8))

    
queen_pos = [0,0]
king_pos = [0,0]
extra_pos = [0,0]
NewGame()


while True:

    screen.fill("Grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                NewGame()



    
    
    


    DrawBoard()
    DrawPiece("♔",queen_pos[0],queen_pos[1])
    
    

    pygame.display.update() 
    clock.tick(60)