import tkinter as tk


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
        self.right_frame.create_line((16 * self.column_position) + 86,
                                     (38 * self.row_position) + 90,
                                     (16 * self.column_position) + 86,
                                     (38 * self.row_position) + 98,
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 70,
                                     (38 * self.row_position) + 90,
                                     (16 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     fill=self.color_1, width=4, joinstyle=tk.ROUND, smooth=True, tags='cvch')


        # oval
        self.right_frame.create_oval((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 60,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 98,
                                     fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 69,
                                     (16 * self.column_position) + 87,
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
        # # circle
        # self.right_frame.create_oval((20 * self.column_position) + 65,
        #                              (self.row_position * 38) + 64,
        #                              (20 * self.column_position) + 95,
        #                              (self.row_position * 38) + 94,
        #                              fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        # # oval
        # self.right_frame.create_oval((18 * self.column_position) + 68,
        #                              (self.row_position * 38) + 59,
        #                              (18 * self.column_position) + 92,
        #                              (self.row_position * 38) + 99,
        #                              fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        # oval
        self.right_frame.create_oval((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 60,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 98,
                                     fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 72,
                                     (self.row_position * 38) + 66,
                                     (16 * self.column_position) + 82,
                                     (self.row_position * 38) + 79,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 83,
                                     (self.row_position * 38) + 79,
                                     (16 * self.column_position) + 72,
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

        self.right_frame.create_line((16 * self.column_position) + 70,
                                     (38 * self.row_position) + 90,
                                     (16 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 86,
                                     (38 * self.row_position) + 90,
                                     (16 * self.column_position) + 86,
                                     (38 * self.row_position) + 98,
                                     fill=self.color_1, width=4, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        # oval
        self.right_frame.create_oval((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 60,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 98,
                                     fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 87,
                                     (self.row_position * 38) + 69,
                                     (16 * self.column_position) + 67,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='cvch')





        # # oval
        # self.right_frame.create_oval((18 * self.column_position) + 68,
        #                              (self.row_position * 38) + 59,
        #                              (18 * self.column_position) + 92,
        #                              (self.row_position * 38) + 99,
        #                              fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        # circle
        # self.right_frame.create_oval((20 *self.column_position) + 65,
        #                              (self.row_position * 38) + 64,
        #                              (20 * self.column_position) + 95,
        #                              (self.row_position * 38) + 94,
        #                              fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        # self.right_frame.create_line((18 * self.column_position) + 90,
        #                              (self.row_position * 38) + 69,
        #                              (18 * self.column_position) + 69,
        #                              (self.row_position * 38) + 90,
        #                              fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')


class Knot4:
    def __init__(self, color, row_position, column_position, frame, bg_color):
        self.color = color
        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):
        # circle
        # self.right_frame.create_oval((20 * self.column_position) + 65,
        #                              (self.row_position * 38) + 64,
        #                              (20 * self.column_position) + 95,
        #                              (self.row_position * 38) + 94,
        #                              fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        # # oval
        # self.right_frame.create_oval((18 * self.column_position) + 68,
        #                              (self.row_position * 38) + 59,
        #                              (18 * self.column_position) + 92,
        #                              (self.row_position * 38) + 99,
        #                              fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        # oval
        self.right_frame.create_oval((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 60,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 98,
                                     fill=self.bg_color, width=4, outline=self.color, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 83,
                                     (self.row_position * 38) + 69,
                                     (16 * self.column_position) + 70,
                                     (self.row_position * 38) + 81,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 71,
                                     (self.row_position * 38) + 78,
                                     (16 * self.column_position) + 83,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='cvch')


class Knot0:
    def __init__(self, row_position, column_position, frame):

        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame

        self.draw()

    def draw(self):
        self.right_frame.create_line((16 * self.column_position) + 75,
                                     (self.row_position * 38) + 76,
                                     (16 * self.column_position) + 81,
                                     (self.row_position * 38) + 82,
                                     fill="#C6C6BC", width=3, capstyle=tk.PROJECTING, smooth=True, tags='cvch')

        self.right_frame.create_line((16 * self.column_position) + 75,
                                     (self.row_position * 38) + 82,
                                     (16 * self.column_position) + 81,
                                     (self.row_position * 38) + 76,
                                     fill="#C6C6BC", width=3, capstyle=tk.PROJECTING, smooth=True, tags='cvch')
