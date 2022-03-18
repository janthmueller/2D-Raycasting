import numpy as np


def magnitude(vector):
    return np.sqrt(np.dot(np.array(vector), np.array(vector)))


def norm(vector):
    return np.array(vector) / magnitude(np.array(vector))


def distance(vector1, vector2):
    return magnitude(np.array(vector1) - np.array(vector2))
