import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot


def main():
    #initialize pygame
    pygame.init() 
    
    font = pygame.font.Font()

    #create Clock object that tracks time
    clock = pygame.time.Clock()

    #groups of objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #adds objects groups with class variable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    #variable for change in time
    dt = 0

    #starting message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #creates screen in pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #spawns player in middle of screen when game started
    player =Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2,)

    asteroid_field = AsteroidField()

    score = 0

    Alive = True

    #infinite loop
    while True:
        
        #allows use of X button on window to close screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        #updates player position before rendering
        updatable.update(dt)

        #every loop fills screen in pygame with black colour
        screen.fill("black")


        #exit game if asteroid collides with player
        for asteroid in asteroids:
            if asteroid.collision(player):
                Alive = False
                

        #destoy asteroid if bullet hits
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score +=100

        #draws player every frame, after its filled but before its refreshed

        for object in drawable:
            object.draw(screen)

        #renders score in top right of screen
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10)), 100

        if Alive != True:
            player.kill()
            screen.fill("black")
            score_text = font.render(f'Score: {score}', True, (255, 255, 255))
            score_text_scaled = pygame.transform.scale_by(score_text, 3)
            screen.blit(score_text_scaled, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))



        #refreshes screen
        pygame.display.flip()

        #updates clock every loop, sets to 60fps
        #returns amount of time since last called, converted to seconds, stored in dt
        dt = (clock.tick(60) /1000)
        
        


if __name__ == "__main__":
    main()
