from src.builder.builders.maze_builder import MazeBuilder


class CountingMazeBuilder(MazeBuilder):
    def __init__(self):
        self.doors = 0
        self.rooms = 0

    def build_room(self, n):
        self.rooms += 1

    def build_door(self, r1, r2):
        self.doors += 1

    def get_counts(self):
        return self.doors, self.rooms
