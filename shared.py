import random
import time

from collections import deque
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse
import sys
import os
import math
import Texture

TICKS_PER_SEC = 60

# Size of sectors used to ease block loading.
SECTOR_SIZE = 16

WALKING_SPEED = 5
FLYING_SPEED = 15

MAX_HP = 20

GRAVITY = 9.81
MAX_JUMP_HEIGHT = 1.0 # About the height of a block.
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = 50

FOG_AREA = [100,110]#[20, 60] # start, ewwnd

WORLD_SIZE = 160

HILL_DISPERSION = 90 # up to 100, %

DAMAGE_SLEEP = 1.0 # seconds

HIT_DISTANCE = 8

TEXTURE_CONFIG_FILE = "resources.json"

PLAYER_HEIGHT = 2

TEXTURES_FOLDER = "textures/"

TEXTURE = 'vanilla.jpg'