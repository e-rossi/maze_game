class Maze:
    def __init__(self):
        # dictionary to hold roomNumber, room_obj <key, value> pairs
        self.rooms = {}

    def add_room(self, room):
        # use roomNumber as lookup value to retrieve room object
        self.rooms[room.roomNumber] = room

    def room_no(self, room_number):
        return self.rooms[room_number]
