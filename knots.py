import  tkinter as tk
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
                                     fill=self.color, width=2, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_line((20 * self.column_position) + 70,
                                     (38 * self.row_position) + 90,
                                     (20 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     fill=self.color_1, width=2, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_oval((20 * self.column_position) + 65,
                                     (self.row_position * 38) + 64,
                                     (20 * self.column_position) + 95,
                                     (self.row_position * 38) + 94,
                                     fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        self.right_frame.create_line((20 * self.column_position) + 69,
                                     (self.row_position * 38) + 69,
                                     (20 * self.column_position) + 90,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='cvch')


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
                                     fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        self.right_frame.create_line((20 * self.column_position) + 72,
                                     (self.row_position * 38) + 66,
                                     (20 * self.column_position) + 82,
                                     (self.row_position * 38) + 79,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_line((20 * self.column_position) + 83,
                                     (self.row_position * 38) + 79,
                                     (20 * self.column_position) + 72,
                                     (self.row_position * 38) + 92,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')


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
                                     fill=self.color_1, width=2, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_line((20 * self.column_position) + 70,
                                     (38 * self.row_position) + 90,
                                     (20 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     fill=self.color, width=2, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_oval((20 * self.column_position) + 65,
                                     (self.row_position * 38) + 64,
                                     (20 * self.column_position) + 95,
                                     (self.row_position * 38) + 94,
                                     fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        self.right_frame.create_line((20 * self.column_position) + 90,
                                     (self.row_position * 38) + 69,
                                     (20 * self.column_position) + 69,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')


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
                                     fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        self.right_frame.create_line((20 * self.column_position) + 88,
                                     (self.row_position * 38) + 69,
                                     (20 * self.column_position) + 76,
                                     (self.row_position * 38) + 81,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_line((20 * self.column_position) + 77,
                                     (self.row_position * 38) + 78,
                                     (20 * self.column_position) + 88,
                                     (self.row_position * 38) + 92,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')




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
                                     fill="#C6C6BC", width=2, capstyle=tk.PROJECTING, smooth=True)

        self.right_frame.create_line((20 * self.column_position) + 77,
                                     (self.row_position * 38) + 82,
                                     (20 * self.column_position) + 83,
                                     (self.row_position * 38) + 76,
                                     fill="#C6C6BC", width=2, capstyle=tk.PROJECTING, smooth=True)
