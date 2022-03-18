import pygame
from manager.input_manager import InputManager
from manager.light_source_manager import LightSourceManager
from manager.line_segment_manager import LineSegmentManager
from manager.screen_manager import ScreenManager


class EventHandler:
    targets = {}

    def register(type):
        def decorator(fn):
            EventHandler.targets.setdefault(type, []).append(fn)

        return decorator

    def notify(event):
        fnl = (
            EventHandler.targets[event.type]
            if event.type in EventHandler.targets
            else []
        )
        for fn in fnl:
            fn(event)


@EventHandler.register(pygame.QUIT)
def on_exit(event):
    pygame.quit()
    quit(0)


@EventHandler.register(pygame.MOUSEBUTTONDOWN)
def on_mouse_button_down(event):
    if event.button == 1:
        InputManager.left_down = pygame.mouse.get_pos()
    if event.button == 3:
        InputManager.right_down = pygame.mouse.get_pos()
        LightSourceManager.source = ()
    if event.button == 4:
        LightSourceManager.ray_num += 2
        LightSourceManager.ray_num = min(
            LightSourceManager.ray_num, LightSourceManager.max_ray_num
        )
    if event.button == 5:
        LightSourceManager.ray_num -= 2
        LightSourceManager.ray_num = max(
            LightSourceManager.ray_num, LightSourceManager.min_ray_num
        )


@EventHandler.register(pygame.MOUSEBUTTONUP)
def on_mouse_button_up(event):
    if event.button == 1:
        InputManager.left_up = pygame.mouse.get_pos()
        LineSegmentManager.bound_lines.append(
            (InputManager.left_down, InputManager.left_up)
        )
    if event.button == 3:
        InputManager.right_up = pygame.mouse.get_pos()
        LightSourceManager.source = InputManager.right_up


@EventHandler.register(pygame.MOUSEMOTION)
def on_mouse_motion(event):
    if left_key_down(event):
        InputManager.left_last = pygame.mouse.get_pos()
        LineSegmentManager.ghost_line = [InputManager.left_down, InputManager.left_last]
    else:
        LineSegmentManager.ghost_line = []

    if right_key_down(event):
        InputManager.right_last = pygame.mouse.get_pos()
        LightSourceManager.source = InputManager.right_last


@EventHandler.register(pygame.KEYDOWN)
def on_key_down(event):
    if event.key == pygame.K_h:
        if InputManager.h_key:
            InputManager.h_key = False
        else:
            InputManager.h_key = True
    if event.key == pygame.K_b:
        if InputManager.b_key:
            InputManager.b_key = False
            LineSegmentManager.outer_bound_lines = []
        else:
            InputManager.b_key = True
            LineSegmentManager.outer_bound_lines = [
                ((0, 0), (ScreenManager.screen_width, 0)),
                ((0, 0), (0, ScreenManager.screen_height)),
                (
                    (0, ScreenManager.screen_height),
                    (ScreenManager.screen_width, ScreenManager.screen_height),
                ),
                (
                    (ScreenManager.screen_width, 0),
                    (ScreenManager.screen_width, ScreenManager.screen_height),
                ),
            ]
    if event.key == pygame.K_z:
        LineSegmentManager.bound_lines = LineSegmentManager.bound_lines[:-1]


def left_key_down(event):
    if event.buttons[0]:
        return True
    else:
        return False


def right_key_down(event):
    if event.buttons[2]:
        return True
    else:
        return False
