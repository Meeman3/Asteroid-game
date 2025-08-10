import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

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