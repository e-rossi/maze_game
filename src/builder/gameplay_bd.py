from src.builder.maze_game_bd import MazeGame


class Builder:
    @classmethod
    def build_using(cls, builder):
        print('******************\n'
              '*** Builder Maze ***\n'
              '******************')

        game = MazeGame()
        builder = builder
        game.create_maze(builder)
        print(builder.get_maze())
