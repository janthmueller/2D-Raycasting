from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import numpy as np
from event_handler import EventHandler
from manager import *
from light_source import LightSource


def draw_ghost_line(screen):
    if len(LineSegmentManager.ghost_line) != 0:
        pygame.draw.line(
            screen,
            (255, 255, 255),
            LineSegmentManager.ghost_line[0],
            LineSegmentManager.ghost_line[1],
            2,
        )
    else:
        pass


def draw_bound_lines(screen):
    for b_line in LineSegmentManager.bound_lines:
        pygame.draw.line(screen, (255, 255, 255), b_line[0], b_line[1], 2)


def main():
    init_input_manager()
    init_screen_manager()
    init_light_source_manager()
    init_line_segment_manager()
    pygame.display.set_caption("2D Raycasting")
    screen = pygame.display.set_mode(
        (ScreenManager.screen_width, ScreenManager.screen_height)
    )
    light_source = LightSource(10, (0, 2 * np.pi), 100)
    while True:
        screen.fill((0, 0, 0))
        draw_ghost_line(screen)
        if not InputManager.h_key:
            draw_bound_lines(screen)
        if len(LightSourceManager.source) == 2:
            light_source.position = LightSourceManager.source
            light_source.num_rays = LightSourceManager.ray_num
            light_source.draw_light_source(screen)
            light_source.draw_rays(
                screen,
                LineSegmentManager.bound_lines + LineSegmentManager.outer_bound_lines,
            )
        for event in pygame.event.get():
            EventHandler.notify(event)
        pygame.display.update()


if __name__ == "__main__":
    main()
