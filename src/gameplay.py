from src.direction import Direction
from src.maze_game import MazeGame

if __name__ == '__main__':

    print('*' * 21 + '\n*** The Maze Game ***\n' + '*' * 21)

    # create the maze
    maze_obj = MazeGame().create_maze()

    # find its rooms
    maze_rooms = []
    for room_number in range(5):
        try:
            # get the room number
            room = maze_obj.room_no(room_number)
            print('\n^^^ Maze\'s got room: {}'.format(room_number, room))
            print('Entering the room')
            room.enter()
            # add rooms to list
            maze_rooms.append(room)
            for idx in range(4):
                side = room.get_side(idx)
                side_str = str(side.__class__).replace("<class '__main__.", "").replace("'>", "")
                print('Room: {}, {:<15s}, Type: {}'.format(room_number, Direction(idx), side_str))
                print('Trying to enter:', Direction(idx))
                side.enter()
                if 'Door' in side_str:
                    door = side
                    if not door.isOpen:
                        print('Opening the door...')
                        door.isOpen = True
                        door.enter()
                    print('\t', door)
                    # get the room on the other side of the door
                    other_room = door.other_side_from(room)
                    print('On the other side of this door is room: {}\n'
                          .format(other_room.roomNumber))
        except KeyError:
            print('No room', room_number)
    num_of_rooms = len(maze_rooms)
    print('\nThere are {} rooms in the Maze'.format(num_of_rooms))

    print('Both doors are the same object, dividing the rooms along East and West.')
