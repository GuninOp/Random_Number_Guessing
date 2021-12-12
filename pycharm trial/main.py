import pygame
import time

print("Press from a to k to change colors.")
print("Press l, n or p to get hollow square, rectangle or circle respectively and Press m, o or q to "
      "get filled square, rectangle or circle respectively.")
print("Press 1 to get Eraser.")
print("Press 2 to make pen size bigger and 3 to make pen size smaller.")
print("Press 4 to get dark theme and 5 to get light theme.")
print("Press 6 to save the drawing you have made.")
print("Press 7 to get User Manual.")

pygame.init()

# Variables
window_width = 1000
window_height = 600
game_over = False
dragging = False
rect_size = 15
circle_size = rect_size
theme = "light"
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
violet = (102, 0, 204)
purple = (255, 0, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
pink = (255, 0, 127)
grey = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
color = black
# Window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Drawing Pad")
window.fill(white)

while not game_over:
    # Variable for while loop to be updated every while
    x, y = pygame.mouse.get_pos()
    circle_size = rect_size
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                color = red
            if event.key == pygame.K_b:
                color = green
            if event.key == pygame.K_c:
                color = blue
            if event.key == pygame.K_d:
                color = cyan
            if event.key == pygame.K_e:
                color = violet
            if event.key == pygame.K_f:
                color = purple
            if event.key == pygame.K_g:
                color = yellow
            if event.key == pygame.K_h:
                color = orange
            if event.key == pygame.K_i:
                color = pink
            if event.key == pygame.K_j:
                color = grey
            if theme == "dark":
                if event.key == pygame.K_k:
                    color = white
            else:
                if event.key == pygame.K_k:
                    color = black
            if event.key == pygame.K_l:
                pygame.draw.rect(window, color, (x, y, rect_size, rect_size), 2, border_radius=1)
            if event.key == pygame.K_m:
                pygame.draw.rect(window, color, (x, y, rect_size, rect_size))
            if event.key == pygame.K_n:
                pygame.draw.rect(window, color, (x, y, rect_size + 5, rect_size), 2, border_radius=1)
            if event.key == pygame.K_o:
                pygame.draw.rect(window, color, (x, y, rect_size + 5, rect_size))
            if event.key == pygame.K_p:
                pygame.draw.circle(window, color, (x, y), circle_size, 1)
            if event.key == pygame.K_q:
                pygame.draw.circle(window, color, (x, y), circle_size)
            if event.key == pygame.K_1:
                if theme == "dark":
                    color = black
                if theme == "light":
                    color = white
            if event.key == pygame.K_2:
                rect_size += 1
                print(rect_size)
            if event.key == pygame.K_3:
                rect_size -= 1
                print(rect_size)
            if event.key == pygame.K_4:
                window.fill(black)
                theme = "dark"
            if event.key == pygame.K_5:
                window.fill(white)
                theme = "light"
            if event.key == pygame.K_6:
                time_taken = time.asctime(time.localtime(time.time()))
                time_taken = time_taken.replace(" ", "_")
                time_taken = time_taken.replace(":", ".")
                pygame.image.save(window, "screenshot" + time_taken + ".png")
                print("Screenshot taken.")
            if event.key == pygame.K_7:
                print("Press from a to k to change colors.")
                print("Press l, n or p to get hollow square, rectangle or circle respectively and Press m, o or q to "
                      "get filled square, rectangle or circle respectively.")
                print("Press 1 to get Eraser.")
                print("Press 2 to make pen size bigger and 3 to make pen size smaller.")
                print("Press 4 to get dark theme and 5 to get light theme.")
                print("Press 6 to save the drawing you have made.")
                print("Press 7 to get User Manual.")

        if event.type == pygame.MOUSEMOTION and dragging:
            pygame.draw.rect(window, color, (x, y, rect_size, rect_size))
    pygame.display.update()

pygame.quit()
quit()
