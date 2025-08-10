from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        #moves forward coonstant speed
        self.position += self.velocity * dt

    def split(self):
        #delete mother asteroid
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            #if the asteroid is too small, destroy
            return
        else:
            #if big enough, split into 2 smaller asteroids
            angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(angle)
            velocity_2 = self.velocity.rotate(-angle)

            small_radius = self.radius - ASTEROID_MIN_RADIUS

            small_ast_1 = Asteroid(self.position[0], self.position[1], small_radius)
            small_ast_1.velocity = velocity_1 * 1.2

            small_ast_2 = Asteroid(self.position[0], self.position[1], small_radius)
            small_ast_2.velocity = velocity_2 * 1.2
