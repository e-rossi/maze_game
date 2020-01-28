from src.classes.map_site import MapSite


class Room(MapSite):
    def __init__(self, roomNo):
        self.sides = [MapSite] * 4
        self.roomNumber = int(roomNo)

    def get_side(self, Direction):
        return self.sides[Direction]

    def set_side(self, Direction, MapSite):
        self.sides[Direction] = MapSite

    def enter(self):
        print('You have entered a room:' + str(self.roomNumber))


class RoomWithABomb(Room):
    def __init__(self, room_no):
        super(RoomWithABomb, self).__init__(room_no)
        self.has_bomb = True
        self.bomb_exploded = False
