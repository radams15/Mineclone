
class Textures:
    def __init__(self, texture_path):
        self.texture_path = texture_path
        self.grass = self.get_texture_coordinates((1, 0), (0, 1), (0, 0))
        self.sand = self.get_texture_coordinates((1, 1), (1, 1), (1, 1))
        self.brick = self.get_texture_coordinates((2, 0), (2, 0), (2, 0))
        self.stone = self.get_texture_coordinates((2, 1), (2, 1), (2, 1))

        self.world_resources = [self.brick, self.stone]#[self.grass, self.sand]

        self.resource_levels = [self.grass, self.stone]

        self.indestructible_resources = []

        self.inventory = [self.grass, self.sand, self.stone, self.brick]

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

    def get_texture_bounding_vertices(self, x, y, n=4):
        """ Return the bounding vertices of the texture square.

        """
        m = 1.0 / n
        dx = x * m
        dy = y * m
        return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m

    def get_texture_coordinates(self, top, bottom, side):
        """ Return a list of the texture squares for the top, bottom and side.

        """
        top = self.get_texture_bounding_vertices(*top)
        bottom = self.get_texture_bounding_vertices(*bottom)
        side = self.get_texture_bounding_vertices(*side)
        result = []
        result.extend(top)
        result.extend(bottom)
        result.extend(side * 4)
        return result
