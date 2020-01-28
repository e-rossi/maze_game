from src.abstract_factory.factories.maze_base_factory import BaseFactory
from src.classes.room import RoomWithABomb
from src.classes.wall import BombedWall


class BombedFactory(BaseFactory):
    @classmethod
    def make_wall(cls):
        return BombedWall()

    @classmethod
    def make_room(cls, n):
        return RoomWithABomb(n)
