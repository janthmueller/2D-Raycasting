import numpy as np
import pygame
from utils.math import *


class Ray:
    def __init__(self, ray_origin, ray_direction):
        self.ray_origin = ray_origin
        self.ray_direction = ray_direction

    def __get_ray_lineseg_intersection_point(self, line_segment):
        ray_origin = np.array(self.ray_origin)
        ray_direction = np.array(self.ray_direction)
        lineseg_p1 = np.array(line_segment[0])
        lineseg_p2 = np.array(line_segment[1])

        v1 = ray_origin - lineseg_p1
        v2 = lineseg_p2 - lineseg_p1
        v3 = np.array([-ray_direction[1], ray_direction[0]])
        t1 = np.cross(v2, v1) / np.dot(v2, v3)
        t2 = np.dot(v1, v3) / np.dot(v2, v3)

        if t1 >= 0.0 and t2 >= 0.0 and t2 <= 1.0:
            return tuple(ray_origin + t1 * ray_direction)
        return ()

    def __get_nearest_ray_lineseg_intersection_point(self, line_segments):
        min_dist = np.inf
        nearest_intersection_point = ()
        for line_segment in line_segments:
            intersection_point = self.__get_ray_lineseg_intersection_point(line_segment)
            if len(intersection_point) == 2:
                dist = distance(self.ray_origin, intersection_point)
                if dist < min_dist:
                    min_dist = dist
                    nearest_intersection_point = intersection_point
        return nearest_intersection_point

    def draw(self, screen, line_segments):
        nearest_intersection_point = self.__get_nearest_ray_lineseg_intersection_point(
            line_segments
        )
        if len(nearest_intersection_point) == 2:
            pygame.draw.line(
                screen, (255, 255, 255), self.ray_origin, nearest_intersection_point, 1
            )
