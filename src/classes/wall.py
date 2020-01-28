from src.classes.map_site import MapSite


class Wall(MapSite):
    def enter(self):
        print('You have ran into a wall...')


class BombedWall(Wall):
    def __init__(self):
        self.wall_is_damaged = False  # True if bomb has exploded
