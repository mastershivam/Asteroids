import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ran_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(ran_angle)
            v2 = self.velocity.rotate(-ran_angle)
            Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = v1*1.2
            Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = v2*1.2
            