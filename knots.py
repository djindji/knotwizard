
class Knot1:

    def __init__(self, color, color_1, row_position, column_position, frame, bg_color):
        self.color = color
        self.color_1 = color_1
        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):

        self.right_frame.create_line((20 * self.column_position) + 90,
                                     (38 * self.row_position) + 90,
                                     (20 * self.column_position) + 90,
                                     (38 * self.row_position) + 98,
                                     fill=self.color, width=4, tags='line')

        self.right_frame.create_line((20 * self.column_position) + 70,
                                     (38 * self.row_position) + 90,
                                     (20 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     fill=self.color_1, width=4, tags='line')

        self.right_frame.create_oval((20 * self.column_position) + 65,
                                     (self.row_position * 38) + 64,
                                     (20 * self.column_position) + 95,
                                     (self.row_position * 38) + 94,
                                     fill=self.bg_color, width=2, outline=self.color)

        self.right_frame.create_line((20 * self.column_position) + 69,
                                     (self.row_position * 38) + 69,
                                     (20 * self.column_position) + 90,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=3)


class Knot2:

    def __init__(self, color, row_position, column_position, frame, bg_color):
        self.color = color
        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):

        self.right_frame.create_oval((20 * self.column_position) + 65,
                                     (self.row_position * 38) + 64,
                                     (20 * self.column_position) + 95,
                                     (self.row_position * 38) + 94,
                                     fill=self.bg_color, width=2, outline=self.color)

        self.right_frame.create_line((20 * self.column_position) + 68,
                                     (self.row_position * 38) + 60,
                                     (20 * self.column_position) + 82,
                                     (self.row_position * 38) + 79,
                                     fill=self.color, width=3)

        self.right_frame.create_line((20 * self.column_position) + 83,
                                     (self.row_position * 38) + 79,
                                     (20 * self.column_position) + 68,
                                     (self.row_position * 38) + 98,
                                     fill=self.color, width=3)


class Knot3:

    def __init__(self, color, color_1, row_position, column_position, frame, bg_color):
        self.color = color
        self.color_1 = color_1
        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):

        self.right_frame.create_line((20 * self.column_position) + 90,
                                     (38 * self.row_position) + 90,
                                     (20 * self.column_position) + 90,
                                     (38 * self.row_position) + 98,
                                     fill=self.color_1, width=4, tags='line')

        self.right_frame.create_line((20 * self.column_position) + 70,
                                     (38 * self.row_position) + 90,
                                     (20 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     fill=self.color, width=4, tags='line')

        self.right_frame.create_oval((20 * self.column_position) + 65,
                                     (self.row_position * 38) + 64,
                                     (20 * self.column_position) + 95,
                                     (self.row_position * 38) + 94,
                                     fill=self.bg_color, width=2, outline=self.color)

        self.right_frame.create_line((20 * self.column_position) + 90,
                                     (self.row_position * 38) + 69,
                                     (20 * self.column_position) + 69,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=3)


class Knot4:

    def __init__(self, color, row_position, column_position, frame, bg_color):
        self.color = color
        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):

        self.right_frame.create_oval((20 * self.column_position) + 65,
                                     (self.row_position * 38) + 64,
                                     (20 * self.column_position) + 95,
                                     (self.row_position * 38) + 94,
                                     fill=self.bg_color, width=2, outline=self.color)

        self.right_frame.create_line((20 * self.column_position) + 91,
                                     (self.row_position * 38) + 60,
                                     (20 * self.column_position) + 79,
                                     (self.row_position * 38) + 79,
                                     fill=self.color, width=3)

        self.right_frame.create_line((20 * self.column_position) + 79,
                                     (self.row_position * 38) + 79,
                                     (20 * self.column_position) + 91,
                                     (self.row_position * 38) + 98,
                                     fill=self.color, width=3)


class Knot0:
    def __init__(self, row_position, column_position, frame):

        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame

        self.draw()

    def draw(self):
        self.right_frame.create_line((20 * self.column_position) + 77,
                                     (self.row_position * 38) + 76,
                                     (20 * self.column_position) + 83,
                                     (self.row_position * 38) + 82,
                                     fill="#C6C6BC", width=2)

        self.right_frame.create_line((20 * self.column_position) + 77,
                                     (self.row_position * 38) + 82,
                                     (20 * self.column_position) + 83,
                                     (self.row_position * 38) + 76,
                                     fill="#C6C6BC", width=2)
