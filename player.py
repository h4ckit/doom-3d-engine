from settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = HALF_WIDTH, HALF_HEIGHT
        self.angle = 0
        self.speed = 200

    @property
    def pos(self):
        return self.x, self.y

    @property
    def speed_fps(self):
        return self.speed / FPS

    def movement(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        delta_x, delta_y = mouse_x - HALF_WIDTH, mouse_y - HALF_HEIGHT
        # self.angle = math.atan2(mouse_y - self.y, mouse_x - self.x)
        self.angle += delta_x / 400
        pygame.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += self.speed_fps * math.cos(self.angle)
            self.y += self.speed_fps * math.sin(self.angle)
        if keys[pygame.K_s]:
            self.x -= self.speed_fps * math.cos(self.angle)
            self.y -= self.speed_fps * math.sin(self.angle)
        if keys[pygame.K_a]:
            self.x += self.speed_fps * math.sin(self.angle)
            self.y -= self.speed_fps * math.cos(self.angle)
        if keys[pygame.K_d]:
            self.x -= self.speed_fps * math.sin(self.angle)
            self.y += self.speed_fps * math.cos(self.angle)

    def draw(self, sc):
        pygame.draw.circle(sc, (0, 0, 255), self.pos, 15)
        pygame.draw.line(sc, (0, 255, 0), self.pos,
                         (self.x + WIDTH * math.cos(self.angle),
                          self.y + WIDTH * math.sin(self.angle)))
