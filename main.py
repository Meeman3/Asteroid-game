import pygame
from constants import *
from player import Player

def main():
    #initialize pygame
    pygame.init() 

    #create Clock object that tracks time
    clock = pygame.time.Clock()

    #groups of objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #adds Player to bth groups with class variable
    Player.containers = (updatable, drawable)

    #variable for change in time
    dt = 0

    #starting message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #creates screen in pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #spawns player in middle of screen when game started
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2,)

    #infinite loop
    while True:
        
        #allows use of X button on window to close screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #every loop fills screen in pygame with black colour
        screen.fill("black")

        #updates player position before rendering
        updatable.update(dt)

        #draws player every frame, after its filled but before its refreshed
        for object in drawable:
            object.draw(screen)


        #refreshes screen
        pygame.display.flip()

        #updates clock every loop, sets to 60fps
        #returns amount of time since last called, converted to seconds, stored in dt
        dt = (clock.tick(60) /1000)
        
        


if __name__ == "__main__":
    main()
