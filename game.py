import pygame
from settings import *
from player import Player
from map import world_map
from ray_casting import ray_casting


class Game:
    def __init__(self):
        pygame.init()
        flags = pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT], flags, 16)
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = FPS

        self.player = Player()

        # pygame.mouse.set_visible(False)

        self.font = pygame.font.SysFont("Arial", 18)

    def update_fps(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.font.render(fps, True, pygame.Color("coral"))
        return fps_text

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def run(self):
        while self.running:
            self.on_event()
            if not pygame.mouse.get_focused():
                continue

            self.player.movement()

            self.screen.fill((50, 50, 50))
            ray_casting(self.screen, self.player.pos, self.player.angle)
            self.player.draw(self.screen)

            for x, y in world_map:
                pygame.draw.rect(self.screen, (200, 200, 200), (x, y, TILE, TILE), 3)

            self.screen.blit(self.update_fps(), (10, 0))
            pygame.display.flip()
            self.clock.tick(self.fps)
        pygame.quit()
