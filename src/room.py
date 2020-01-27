from src.map_site import MapSite


class Room(MapSite):
    def __init__(self, roomNo):
        self._sides = [MapSite] * 4
        self.roomNumber = int(roomNo)

    def get_side(self, Direction):
        return self._sides[Direction]

    def set_side(self, Direction, MapSite):
        self._sides[Direction] = MapSite

    def enter(self):
        print('You have entered a room:' + str(self.roomNumber))
