from src.classes.door import Door
from src.classes.maze import Maze
from src.classes.room import Room
from src.classes.wall import Wall


class BaseFactory:
    @classmethod
    def make_maze(cls):
        return Maze()

    @classmethod
    def make_wall(cls):
        return Wall()

    @classmethod
    def make_room(cls, n):
        return Room(n)

    @classmethod
    def make_door(cls, r1, r2):
        return Door(r1, r2)
