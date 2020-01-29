class MazeGame:
    def create_maze(self, builder):
        builder.build_maze()
        builder.build_room(1)
        builder.build_room(2)
        builder.build_door(1, 2)

        return builder.get_maze()

    def create_complex_maze(self, builder):
        builder.build_room(1)
        builder.build_room(1001)

        return builder.get_maze()
