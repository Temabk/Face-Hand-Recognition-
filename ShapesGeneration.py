import cv2
import mediapipe as mp
import numpy as np
from random import randint, choice
import time

num_shapes = 5
shapes = []
shape_size = 50
colors = [
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (0, 0, 0)
]

def generate_random_shapes(num_shapes: int, image_shape: tuple) -> list:
    '''
    Генерация рандомных фигур

    :param num_shapes: число генерируемых фигур
    :type num_shapes: int
    :param image_shape: размер изображения
    :type image_shape: tuple
    :returns: возвращает список сгенерированных фигур
    :rtype: list
    :raises TypeError: Если `num_shapes` не является целым числом, или `image_shape` не является кортежем с тремя целыми числами
    '''
    shapes = []
    height, width, _ = image_shape
    if isinstance(num_shapes, int) and isinstance(image_shape, tuple):
        for _ in range(num_shapes):
            while True:
                x = randint(30, width - 30)  
                y = randint(30, height - 30)
                if not is_inside_small_window((x, y)):
                    shape_type = choice(['circle', 'square', 'triangle'])
                    color = choice(colors)  
                    shapes.append({'position': (x, y), 'type': shape_type, 'color': color})
                    break
        return shapes
    else:
        raise TypeError
    
shapes = generate_random_shapes(num_shapes, (480, 640, 3))
small_window_shape = choice(shapes)