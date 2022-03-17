from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from event_handler import EventHandler
from manager.input_manager import init_input_manager, InputManager
from manager.source_manager import init_source_manager
from manager.bound_manager import init_bound_manager
from manager.option_manager import init_option_manager, OptionManager
from draw import *



def main():
    init_input_manager()
    init_option_manager()
    init_source_manager()
    init_bound_manager()
    pygame.display.set_caption('2D Raycasting')
    screen = pygame.display.set_mode((OptionManager.screen_width, OptionManager.screen_height))
    while True:
        screen.fill((0, 0, 0))
        draw_ghost_line(screen)
        if not InputManager.h_key:
            draw_bound_lines(screen)
        draw_ghost_source(screen)
        draw_source(screen)
        draw_rays(screen)
        for event in pygame.event.get():
            EventHandler.notify(event)
        pygame.display.update()
if __name__ == "__main__":
    main()