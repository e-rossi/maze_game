class Maze:
    def __init__(self):
        # dictionary to hold roomNumber, room_obj <key, value> pairs
        self.rooms = {}

    def add_room(self, room):
        # use roomNumber as lookup value to retrieve room object
        self.rooms[room.roomNumber] = room

    # room_no getter
    def room_no(self, room_no):
        return self.rooms[room_no]
