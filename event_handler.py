import pygame
from manager.input_manager import InputManager
from manager.source_manager import SourceManager
from manager.bound_manager import BoundManager
from manager.option_manager import OptionManager

class EventHandler:
    targets = {}

    def register(type):
        def decorator(fn):
            EventHandler.targets.setdefault(type, []).append(fn)
        return decorator

    def notify(event):
        fnl = EventHandler.targets[event.type] if event.type in EventHandler.targets else []
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
        SourceManager.source = ()
    if event.button == 4: 
        OptionManager.ray_num += 2
        OptionManager.ray_num = min(OptionManager.ray_num, OptionManager.max_ray_num)
    if event.button == 5: 
        OptionManager.ray_num -= 2
        OptionManager.ray_num = max(OptionManager.ray_num, OptionManager.min_ray_num)




@EventHandler.register(pygame.MOUSEBUTTONUP)
def on_mouse_button_up(event):
    if event.button == 1: 
        InputManager.left_up = pygame.mouse.get_pos()
        BoundManager.bound_lines.append((InputManager.left_down, InputManager.left_up)) 
    if event.button == 3:
        InputManager.right_up = pygame.mouse.get_pos()
        SourceManager.source = InputManager.right_up
        SourceManager.ghost_source = ()


@EventHandler.register(pygame.MOUSEMOTION)
def on_mouse_motion(event):
    if left_key_down(event):
        InputManager.left_last = pygame.mouse.get_pos()
        BoundManager.ghost_line = [InputManager.left_down, InputManager.left_last]
    else:
        BoundManager.ghost_line = []
    
    if right_key_down(event):
        InputManager.right_last = pygame.mouse.get_pos()
        SourceManager.ghost_source = InputManager.right_last
    else:
        SourceManager.ghost_source = ()

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
            BoundManager.outer_bound_lines = []
        else:
            InputManager.b_key = True
            BoundManager.outer_bound_lines = [((0,0),(OptionManager.screen_width,0)),
            ((0,0),(0,OptionManager.screen_height)),
            ((0,OptionManager.screen_height),(OptionManager.screen_width,OptionManager.screen_height)),
            ((OptionManager.screen_width,0),(OptionManager.screen_width,OptionManager.screen_height))]
    if event.key ==pygame.K_z:
        BoundManager.bound_lines = BoundManager.bound_lines[:-1]


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



