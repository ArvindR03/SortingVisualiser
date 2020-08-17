import pygame
import random
import algorithms

pygame.init()
DIM = (605, 500)
WIN = pygame.display.set_mode(DIM)
pygame.display.set_caption("Sorting Visualiser")
font = pygame.font.SysFont('Calibri', 14, bold=True)
header_font = pygame.font.SysFont('Calibri', 30, bold=True)

BAR_WIDTH = 25
INITX = 5
INITY = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (40, 255, 40)
RED = (255, 40, 40)

def to_height(values):
    height = []
    for i in values:
        height.append(i * 4)
    return height

def show(height, win, height_color, toggle):
    if toggle:
        toggle_number(height, win)

    for i in range(len(height)):
        if height_color[i] == BLACK:
            pygame.draw.rect(win, BLACK, (INITX + i * 30, INITY, BAR_WIDTH, height[i]))
        elif height_color[i] == GREEN:
            pygame.draw.rect(win, GREEN, (INITX + i * 30, INITY, BAR_WIDTH, height[i]))
        elif height_color[i] == RED:
            pygame.draw.rect(win, RED, (INITX + i * 30, INITY, BAR_WIDTH, height[i]))

def toggle_number(height, win):
    for i in range(len(height)):
        number = font.render(str(height[i] // 4), True, BLACK)
        win.blit(number, (INITX + i * 30 + 5, height[i] + INITY + 7))

def gen(i):
    arr = []
    for x in range(i):
        arr.append(random.randint(1, 100))
    return arr

def main(win):
    height_init = gen(20)
    height = to_height(height_init)
    height_color = [BLACK for i in range(len(height))]
    run = True
    executing = False
    number_toggle = True

    while run:
        pygame.time.delay(10)

        if executing == False:
            win.fill(WHITE)
            show(height, win, height_color, number_toggle)
            toggle_number(height, win)
            pygame.display.update()
        else:
            algorithms.BubbleSort(height, win, show, height_color, number_toggle, WHITE, BLACK, GREEN, RED)
            executing = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    executing = True

if __name__ == "__main__":
    main(WIN)