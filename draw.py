import pygame
import numpy as np
from manager.source_manager import SourceManager
from manager.bound_manager import BoundManager
from manager.option_manager import OptionManager


def draw_ghost_line(screen):
    if len(BoundManager.ghost_line) != 0:
        pygame.draw.line(screen, (255,255,255), BoundManager.ghost_line[0], BoundManager.ghost_line[1], 2)
    else:
        pass

def draw_ghost_source(screen):
    if len(SourceManager.ghost_source) != 0:
        pygame.draw.circle(screen, (255,255,255), SourceManager.ghost_source, 10)
    else:
        pass

def draw_bound_lines(screen):
        for b_line in BoundManager.bound_lines:
            pygame.draw.line(screen, (255,255,255), b_line[0], b_line[1], 2)

def draw_source(screen):
    if len(SourceManager.source) != 0:
        pygame.draw.circle(screen, (255,255,255), SourceManager.source, 10)
    else:
        pass

def draw_rays(screen):

    if len(SourceManager.source) != 0 or len(SourceManager.ghost_source) != 0:
        if len(SourceManager.source) != 0:
            s_pos = SourceManager.source
        else:
            s_pos = SourceManager.ghost_source

        init_e_point = (OptionManager.screen_height + OptionManager.screen_width, OptionManager.screen_height + OptionManager.screen_width)
        theta_list = np.arange(0,2 * np.pi,step=2*np.pi/OptionManager.ray_num)

        for i in theta_list:
            min_dist = OptionManager.screen_height + OptionManager.screen_width
            min_i_point = ()
            e_pos = (np.cos(i) * (init_e_point[0] - s_pos[0]) - np.sin(i) * (init_e_point[1] - s_pos[1]) + s_pos[0],
                    np.sin(i) * (init_e_point[0] - s_pos[0]) + np.cos(i) * (init_e_point[1] - s_pos[1]) + s_pos[1])
            for b_line in BoundManager.bound_lines+BoundManager.outer_bound_lines:
                x1, y1 = s_pos
                x2, y2 = e_pos
                x3, y3 = b_line[0]
                x4, y4 = b_line[1]
                denominator = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
                i_point = (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4 - y3*x4))/denominator, 
                            ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4 - y3*x4))/denominator)

                if is_between(b_line[0], b_line[1],i_point) and is_between(s_pos, e_pos, i_point):
                    dist = np.sqrt((i_point[0] - s_pos[0]) ** 2 + (i_point[1]-s_pos[1]) ** 2)
                    if dist < min_dist:
                        min_dist = dist
                        min_i_point = i_point
            if len(min_i_point) != 0:
                pygame.draw.line(screen, (255, 255, 255), s_pos, min_i_point)        
    else:
        pass

def is_between(a, b, c):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    threshold = 0.5
    if abs(crossproduct) > threshold:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True