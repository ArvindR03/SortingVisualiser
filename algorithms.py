import pygame

def BubbleSort(height, win, show, height_color, number_toggle, title, ops, header_font, WHITE, BLACK, GREEN, RED):
    for i in range(len(height) - 1):
        for j in range(len(height) - i - 1):
            height_color[j] = RED
            height_color[j + 1] = RED
            show(height, win, height_color, number_toggle)
            win.blit(title, (20, 460))
            pygame.display.update()
            pygame.time.delay(20)

            if height[j] > height[j + 1]:
                height[j], height[j + 1] = height[j + 1], height[j]
                ops += 1
            win.fill(WHITE)

            ops_text = header_font.render(f'Ω = {ops}', 30, BLACK)
            height_color[j] = BLACK
            height_color[j + 1] = BLACK
            show(height, win, height_color, number_toggle)
            win.blit(title, (20, 460))
            win.blit(ops_text, (470, 460))
            pygame.time.delay(20)
            pygame.display.update()

    return ops