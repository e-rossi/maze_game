from src.classes.room import Room


class EnchantedRoom(Room):
    def __init__(self, room_no, the_spell):
        super(EnchantedRoom, self).__init__(room_no)
        print('The spell is: ' + the_spell)
