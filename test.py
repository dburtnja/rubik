import arcade

SCREEN_SIZE = 600

FRONT_SIDE = "front_size"
LEFT_SIDE = "left_size"
RIGHT_SIDE = "right_side"
TOP_SIDE = "top_side"
DOWN_SIDE = "down_side"
BACK_SIDE = "back_side"

RUBIK_COLORS = [
    arcade.color.YELLOW,
    arcade.color.WHITE,
    arcade.color.BLUE,
    arcade.color.RED,
    arcade.color.GREEN,
    arcade.color.ORANGE
]


class RubikSquare:

    def __init__(self, color):
        self.color = color


class RubikSide:

    def __init__(self, center_x, center_y, rubik_squares, size=SCREEN_SIZE/6):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        if isinstance(rubik_squares, tuple):
            self.rubik_squares = [RubikSquare(rubik_squares) for _ in range(9)]
        else:
            self.rubik_squares = rubik_squares
        self.border = size / 40
        self.rubik_square_size = (self.size - (self.border * 4)) / 3
        self.positions = self._get_positions()

    def put_on_bord(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.size, self.size, arcade.color.BLACK)

        for index, square in enumerate(self.rubik_squares):
            arcade.draw_rectangle_filled(self.positions[index][0],
                                         self.positions[index][1],
                                         self.rubik_square_size,
                                         self.rubik_square_size,
                                         square.color)

    def _get_positions(self):
        directions = (-self.rubik_square_size - self.border, 0, self.rubik_square_size + self.border)
        result = []

        for y_direction in directions:
            for x_direction in directions:
                result.append((x_direction + self.center_x, y_direction + self.center_y))
        return result


class Board:

    def __init__(self, size):
        self.size = size
        self.border = size / 40
        self.rubik_size = size / 6
        directions = (-self.rubik_size - self.border, 0, self.rubik_size + self.border)
        center = size / 2
        self.rubik_sides = {
            FRONT_SIDE: (center, center),
            LEFT_SIDE: (directions[0] + center, center),
            RIGHT_SIDE: (directions[2] + center, center),
            DOWN_SIDE: (center, directions[0] + center),
            TOP_SIDE: (center, directions[2] + center),
            BACK_SIDE: (center, directions[2] * 2 + center)
        }
        self.sides = [RubikSide(*self.rubik_sides[key], RUBIK_COLORS[color]) for color, (key, value) in enumerate(self.rubik_sides.items())]
        print(self.rubik_sides)

    def draw_sizes(self):
        arcade.start_render()

        for side in self.sides:
            side.put_on_bord()





if __name__ == '__main__':
    arcade.open_window(SCREEN_SIZE, SCREEN_SIZE, "RUBIK")
    arcade.set_background_color(arcade.color.AERO_BLUE)

    board = Board(SCREEN_SIZE)
    board.draw_sizes()


    # x = 300
    # y = 300
    # radios = 100
    #
    # arcade.draw_rectangle_filled(SCREEN_SIZE / 2, SCREEN_SIZE / 2, SCREEN_SIZE / 6, SCREEN_SIZE / 6, arcade.color.BLACK)
    #
    # # arcade.draw_circle_filled(x, y, radios, arcade.color.BABY_BLUE)

    arcade.finish_render()

    arcade.run()
