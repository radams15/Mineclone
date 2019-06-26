import json
from Texture import Texture
from shared import TEXTURE_CONFIG_FILE

class Textures:
    def __init__(self, texture_path):
        self.texture_path = texture_path

        self.texture_size = 16 # 16*16 texture size

        self.textures = {}

        for texture in json.load(open(TEXTURE_CONFIG_FILE)).items():
            name = texture[0]
            texture_coords = texture[1]["texture_coords"]
            top,bottom,side = texture_coords
            self.textures[name] = Texture(self.get_texture_coordinates(top, bottom, side))

        self.world_resources = list(self.textures.values())#[self.textures["sand"], self.textures["brick"], self.textures["stone"]]

        self.resource_levels = [self.textures["dirt"], self.textures["stone"]]

        self.wall_resource = self.textures["stone"]

        self.indestructible_resources = []

        self.inventory = [self.textures["sand"], self.textures["stone"], self.textures["brick"]]

        self.faces = [
            (0, 1, 0),
            (0, -1, 0),
            (-1, 0, 0),
            (1, 0, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]


    def get_cube_vertices(self, x, y, z, n):
        return [
            x - n, y + n, z - n, x - n, y + n, z + n, x + n, y + n, z + n, x + n, y + n, z - n,  # top
            x - n, y - n, z - n, x + n, y - n, z - n, x + n, y - n, z + n, x - n, y - n, z + n,  # bottom
            x - n, y - n, z - n, x - n, y - n, z + n, x - n, y + n, z + n, x - n, y + n, z - n,  # left
            x + n, y - n, z + n, x + n, y - n, z - n, x + n, y + n, z - n, x + n, y + n, z + n,  # right
            x - n, y - n, z + n, x + n, y - n, z + n, x + n, y + n, z + n, x - n, y + n, z + n,  # front
            x + n, y - n, z - n, x - n, y - n, z - n, x - n, y + n, z - n, x + n, y + n, z - n,  # back
        ]

    def get_texture_bounding_vertices(self, x, y):
        m = 1 / self.texture_size
        dx = x * m
        dy = y * m
        return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m

    def get_texture_coordinates(self, top, bottom, side):
        top = self.get_texture_bounding_vertices(*top)
        bottom = self.get_texture_bounding_vertices(*bottom)
        side = self.get_texture_bounding_vertices(*side)
        result = []
        result.extend(top)
        result.extend(bottom)
        result.extend(side * 4)
        return result
