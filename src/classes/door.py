from src.classes.map_site import MapSite


class Door(MapSite):
    def __init__(self, Room1=None, Room2=None):
        self._room1 = Room1
        self._room2 = Room2
        self.isOpen = False

    def other_side_from(self, Room):
        print('\tDoor obj: This door is a side of Room: {}'.format(Room.roomNumber))
        if 1 == Room.roomNumber:
            other_room = self._room2
        else:
            other_room = self._room1
        return other_room

    def enter(self):
        if self.isOpen:
            print('You have passed through this door...')
        else:
            print('This door is closed')
