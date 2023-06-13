# Platformer Game Portfolio Project by Ibrahim Ismayilov

# IMPORTING MODULES 
# Import pygame
import pygame

# Import "join" method from os to help with saving images in variables
from os.path import join, isfile
from pygame._sdl2 import Window


# INTIALIZE MODULES OR DIRECTORIES
# Intialize pygame module
pygame.init()


# SET UP PYGAME WINDOW FOR DISPLAY 
# Change pygame window title
pygame.display.set_caption("Platformer Game by Ibrahim Ismayilov")

# Width and height of pygame window stored in variables
WIDTH, HEIGHT = 1500, 800

# Intialize the pygame window for display
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Create FPS variable to set max FPS of the game to be 60 when run
FPS = 150

# Main function to contain event handlers and run non-stop while program is open
# Why pass the window parameter?
def main(window):
    image = pygame.image.load("RunningGuy.png")
    image_rect = pygame.Rect(50, 50, image.get_width(), image.get_height())

    offset_x = 0
    scroll_area_width = 200

    clock = pygame.time.Clock() 

    # Constant, infinitely running loop
    run = True
    while run:

        # A method to run every frame and make the game run at max 60 FPS on all machines
        clock.tick(150)
        print(clock.get_fps())


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image_rect.x += -3
        if keys[pygame.K_RIGHT]:
            image_rect.x += 3

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user closes the program, exit the while loop and quit pygame
                run = False
                break
        
        window.blit(image, (image_rect.x, image_rect.y))
        pygame.display.update()
        
    
    # Quit pygame if the while loop has been broken
    pygame.quit()
    quit()


# Call main function to start the game
main(window)