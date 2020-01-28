from src.classes.game_constructor import GameConstructor
from src.no_design_pattern.maze_game import MazeGame


class BaseGame:
    @classmethod
    def run(cls):
        maze_obj = MazeGame().create_maze()
        GameConstructor.construct(maze_obj)
