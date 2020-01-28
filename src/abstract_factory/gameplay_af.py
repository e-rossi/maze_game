from src.abstract_factory.maze_game_af import MazeGame
from src.classes.game_constructor import GameConstructor


class Factory:
    @classmethod
    def run_factory(cls, factory, explode_bomb=False):
        maze_obj = MazeGame().create_maze(factory)
        GameConstructor.construct(maze_obj)

        if explode_bomb:
            print('\n****** Bomb Exploded! - Walls have been damaged... ******\n')
            maze_obj.rooms[1].bomb_exploded = True
            for side in range(4):
                cur_side = maze_obj.rooms[1].sides[side]
                if 'BombedWall' in str(cur_side):
                    cur_side.wall_is_damaged = True
                    print('Wall is damaged:', cur_side, cur_side.wall_is_damaged)
