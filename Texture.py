
class Texture:
    def __init__(self, name, texture, mining_level, damage):
        self.name = name
        self.texture = texture
        self.mining_level = mining_level
        self.indestructible = False
        self.damage = damage

        if mining_level > 10:
            self.indestructible = True

    def __str__(self):
        return f"Texture({self.name})"

    def __repr__(self):
        return self.name