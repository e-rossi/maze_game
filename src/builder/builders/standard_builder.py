from src.builder.builders.maze_builder import MazeBuilder
from src.classes.direction import Direction
from src.classes.door import Door
from src.classes.maze import Maze
from src.classes.room import Room
from src.classes.wall import Wall


class StandardMazeBuilder(MazeBuilder):
    def __init__(self):
        self.current_maze = None

    def build_maze(self):
        self.current_maze = Maze()

    def build_room(self, n):
        try:
            self.current_maze.room_no(n)
        except:
            print('Room {} does not exist - building it.'.format(n))
            room = Room(n)
            self.current_maze.add_room(room)

            room.set_side(Direction.North.value, Wall())
            room.set_side(Direction.South.value, Wall())
            room.set_side(Direction.East.value, Wall())
            room.set_side(Direction.West.value, Wall())

    def build_door(self, n1, n2):
        r1 = self.current_maze.room_no(n1)
        r2 = self.current_maze.room_no(n2)
        d = Door(r1, r2)

        r1.set_side(self.common_wall(r1, r2), d)
        r2.set_side(self.common_wall(r2, r1), d)

        print()
        for side in range(4):
            if 'Door' in str(r1.sides[side]):
                print('Room 1: ', r1.sides[side], Direction(side))
            if 'Door' in str(r2.sides[side]):
                print('Room 2: ', r2.sides[side], Direction(side))

    def get_maze(self):
        return self.current_maze

    def common_wall(self, a_room, another_room):
        # layout: room1, room2 from left (West) to right (East)
        if a_room.roomNumber < another_room.roomNumber:
            return Direction.East.value
        else:
            return Direction.West.value
