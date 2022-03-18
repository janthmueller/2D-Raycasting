from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import numpy as np
from event_handler import EventHandler
from manager import *
from light_source import LightSource


def draw_temp_line(screen):
    if len(LineSegmentManager.temp_line) != 0:
        pygame.draw.line(
            screen,
            (255, 255, 255),
            LineSegmentManager.temp_line[0],
            LineSegmentManager.temp_line[1],
            2,
        )


def draw_settled_lines(screen):
    for b_line in LineSegmentManager.settled_lines:
        pygame.draw.line(screen, (255, 255, 255), b_line[0], b_line[1], 2)


def main():
    init_manager()
    pygame.display.set_caption("2D Raycasting")
    screen = pygame.display.set_mode(
        (ScreenManager.screen_width, ScreenManager.screen_height)
    )
    light_source = LightSource(10, (0, 2 * np.pi), 100)
    while True:
        screen.fill((0, 0, 0))
        draw_temp_line(screen)
        if not InputManager.h_key:
            draw_settled_lines(screen)
        if len(LightSourceManager.light_source_pos) == 2:
            light_source.position = LightSourceManager.light_source_pos
            light_source.num_rays = LightSourceManager.ray_num
            light_source.draw_light_source(screen)
            light_source.draw_rays(
                screen,
                LineSegmentManager.settled_lines + LineSegmentManager.outer_bound_lines,
            )
        for event in pygame.event.get():
            EventHandler.notify(event)
        pygame.display.update()


if __name__ == "__main__":
    main()
