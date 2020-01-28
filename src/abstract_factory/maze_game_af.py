from src.classes.direction import Direction
from src.abstract_factory.factories.maze_base_factory import BaseFactory


class MazeGame:
    def create_maze(self, factory=BaseFactory()):
        a_maze = factory.make_maze()
        r1 = factory.make_room(1)
        r2 = factory.make_room(2)
        the_door = factory.make_door(r1, r2)

        a_maze.add_room(r1)
        a_maze.add_room(r2)

        r1.set_side(Direction.North.value, factory.make_wall())
        r1.set_side(Direction.East.value, the_door)
        r1.set_side(Direction.South.value, factory.make_wall())
        r1.set_side(Direction.West.value, factory.make_wall())

        r2.set_side(Direction(0).value, factory.make_wall())
        r2.set_side(Direction(1).value, factory.make_wall())
        r2.set_side(Direction(2).value, factory.make_wall())
        r2.set_side(Direction(3).value, the_door)

        return a_maze
