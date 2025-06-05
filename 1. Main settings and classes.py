import pygame
import random
import os
import sys
from pygame.locals import *

# Константы
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 182, 193)
GOLD = (255, 215, 0)
DARK_GREEN = (0, 100, 0)
DARK_BLUE = (0, 0, 100)
DARK_RED = (100, 0, 0)

class Cowboy:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.speed = 5
        self.width = img.get_width()
        self.height = img.get_height()

class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.speed = 10
        self.width = img.get_width()
        self.height = img.get_height()

class Enemy:
    def __init__(self, x, y, img, enemy_type, points):
        self.x = x
        self.y = y
        self.img = img
        self.type = enemy_type
        self.points = points
        self.speed = random.uniform(1.0, 3.0)
        self.width = img.get_width()
        self.height = img.get_height()