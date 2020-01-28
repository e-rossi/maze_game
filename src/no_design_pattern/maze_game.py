from src.classes.direction import Direction
from src.classes.door import Door
from src.classes.maze import Maze
from src.classes.room import Room
from src.classes.wall import Wall


class MazeGame:
    def create_maze(self):
        a_maze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        the_door = Door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)

        r1.set_side(Direction.North.value, Wall())
        r1.set_side(Direction.East.value, the_door)
        r1.set_side(Direction.South.value, Wall())
        r1.set_side(Direction.West.value, Wall())

        r2.set_side(Direction(0).value, Wall())
        r2.set_side(Direction(1).value, Wall())
        r2.set_side(Direction(2).value, Wall())
        r2.set_side(Direction(3).value, the_door)

        return a_maze
