from ray import Ray
import numpy as np
from utils.math import *
import pygame


class LightSource:
    def __init__(self, radius, fov, num_rays):
        self.radius = radius
        self.fov = fov
        self.num_rays = num_rays
        self.position = ()

    def append_rays(self):
        angles = np.arange(
            self.fov[0], self.fov[1], (self.fov[0] + self.fov[1]) / self.num_rays
        )
        self.rays = []
        for angle in angles:
            ray_origin = (
                self.position[0] + (self.radius * np.sin(angle)),
                self.position[1] + (self.radius * np.cos(angle)),
            )
            ray_direction = norm(np.array(ray_origin) - np.array(self.position))
            ray = Ray(ray_origin, ray_direction)
            self.rays += [ray]

    def draw_light_source(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def draw_rays(self, screen, line_segments):
        self.append_rays()
        for ray in self.rays:
            ray.draw(screen, line_segments)
