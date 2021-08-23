import pygame
from settings import *
from map import world_map


def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    x0, y0 = player_pos

    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        x, y = x0, y0
        for depth in range(MAX_DEPTH):
            x = x0 + depth * cos_a
            y = y0 + depth * sin_a
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth if depth else 0
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        # pygame.draw.line(sc, (255, 0, 0), player_pos, (x, y), 2)
        cur_angle += DELTA_ANGLE
