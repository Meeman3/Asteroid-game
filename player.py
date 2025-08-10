import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    # in the player class
    def triangle(self):
        #vector of 0,1 rotated by current rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        #perpendicular vector, smaller to make isoceles
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        #draws polygon on screen in white using points from self.triangle with width 2
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt):
        #rotates player
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        #gives pygame acces to key presses
        keys = pygame.key.get_pressed()

        #if a is pressed rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)

        #if d is pressed rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        #finds a unit vector in our direction then adds the forward distance
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt