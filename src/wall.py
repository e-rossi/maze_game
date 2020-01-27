from src.map_site import MapSite


class Wall(MapSite):
    def enter(self):
        print('You have ran into a wall...')
