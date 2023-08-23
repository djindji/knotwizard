import tkinter as tk


# DRAW PATTERN VERTICAL

# NOT KNITTED "X" SYMBOL ON BUTTON
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
                                     fill="#C6C6BC", width=3, capstyle=tk.PROJECTING, smooth=True, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 75,
                                     (self.row_position * 38) + 82,
                                     (16 * self.column_position) + 81,
                                     (self.row_position * 38) + 76,
                                     fill="#C6C6BC", width=3, capstyle=tk.PROJECTING, smooth=True, tags='canvas_change')


# LEFT MOUSE BUTTON CLICKED FIRST TIME, KNOT FROM LEFT TO RIGHT:  "\"
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
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 70,
                                     (38 * self.row_position) + 90,
                                     (16 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     fill=self.color_1, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        # OVAL
        self.right_frame.create_oval((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 60,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 98,
                                     fill=self.bg_color, width=4, outline=self.color, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 69,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')


# LEFT MOUSE BUTTON CLICKED SECOND TIME, KNOT FROM LEFT TO LEFT:  ">"
class Knot2:
    def __init__(self, color, row_position, column_position, frame, bg_color):
        self.color = color
        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):

        # OVAL
        self.right_frame.create_oval((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 60,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 98,
                                     fill=self.bg_color, width=4, outline=self.color, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 72,
                                     (self.row_position * 38) + 66,
                                     (16 * self.column_position) + 82,
                                     (self.row_position * 38) + 79,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 83,
                                     (self.row_position * 38) + 79,
                                     (16 * self.column_position) + 72,
                                     (self.row_position * 38) + 92,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')


# RIGHT MOUSE BUTTON CLICKED FIRST TIME, KNOT FROM RIGHT TO LEFT:  "/"
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
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 86,
                                     (38 * self.row_position) + 90,
                                     (16 * self.column_position) + 86,
                                     (38 * self.row_position) + 98,
                                     fill=self.color_1, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        # OVAL
        self.right_frame.create_oval((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 60,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 98,
                                     fill=self.bg_color, width=4, outline=self.color, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 87,
                                     (self.row_position * 38) + 69,
                                     (16 * self.column_position) + 67,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')


# RIGHT MOUSE BUTTON CLICKED SECOND TIME, KNOT FROM RIGHT TO RIGHT:  "<"
class Knot4:
    def __init__(self, color, row_position, column_position, frame, bg_color):
        self.color = color
        self.row_position = row_position
        self.column_position = column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):

        # OVAL
        self.right_frame.create_oval((16 * self.column_position) + 67,
                                     (self.row_position * 38) + 60,
                                     (16 * self.column_position) + 87,
                                     (self.row_position * 38) + 98,
                                     fill=self.bg_color, width=4, outline=self.color, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 83,
                                     (self.row_position * 38) + 69,
                                     (16 * self.column_position) + 70,
                                     (self.row_position * 38) + 81,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        self.right_frame.create_line((16 * self.column_position) + 71,
                                     (self.row_position * 38) + 78,
                                     (16 * self.column_position) + 83,
                                     (self.row_position * 38) + 90,
                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')


# DRAW PATTERN HORIZONTAL
# NOT KNITTED "X" SYMBOL ON BUTTON
class Knot0x:
    def __init__(self, row_position, column_position, frame, threads_num):

        self.row_position = row_position
        self.threads_num = threads_num
        self.column_position = (threads_num - 2) - column_position
        self.right_frame = frame

        self.draw()

    def draw(self):
        self.right_frame.create_line((self.row_position * 38) + 82,
                                     (16 * self.column_position) + 75,
                                     (self.row_position * 38) + 76,
                                     (16 * self.column_position) + 81,

                                     fill="#C6C6BC", width=3, capstyle=tk.PROJECTING, smooth=True, tags='canvas_change')

        self.right_frame.create_line((self.row_position * 38) + 76,
                                     (16 * self.column_position) + 75,
                                     (self.row_position * 38) + 82,
                                     (16 * self.column_position) + 81,

                                     fill="#C6C6BC", width=3, capstyle=tk.PROJECTING, smooth=True, tags='canvas_change')


# LEFT MOUSE BUTTON CLICKED FIRST TIME, KNOT FROM BOTTOM TO TOP:  "/"
class Knot1x:
    def __init__(self, color, color_1, row_position, column_position, frame, bg_color, threads_num):
        self.color = color
        self.color_1 = color_1
        self.row_position = row_position
        self.threads_num = threads_num
        self.column_position = (threads_num - 2) - column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):
        self.right_frame.create_line((38 * self.row_position) + 90,
                                     (16 * self.column_position) + 86,
                                     (38 * self.row_position) + 98,
                                     (16 * self.column_position) + 86,
                                     fill=self.color_1, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        self.right_frame.create_line((38 * self.row_position) + 90,
                                     (16 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     (16 * self.column_position) + 70,

                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        # OVAL
        self.right_frame.create_oval((self.row_position * 38) + 60,
                                     (self.column_position * 16) + 67,
                                     (self.row_position * 38) + 98,
                                     (self.column_position * 16) + 87,

                                     fill=self.bg_color, width=4, outline=self.color, tags='canvas_change')

        self.right_frame.create_line((self.row_position * 38) + 69,
                                     (self.column_position * 16) + 87,
                                     (self.row_position * 38) + 90,
                                     (self.column_position * 16) + 67,

                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')


# LEFT MOUSE BUTTON CLICKED SECOND TIME, KNOT FROM BOTTOM TO BOTTOM:  "/\"
class Knot2x:
    def __init__(self, color, row_position, column_position, frame, bg_color, threads_num):
        self.color = color
        self.row_position = row_position
        self.threads_num = threads_num
        self.column_position = (threads_num - 2) - column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):
        # OVAL
        self.right_frame.create_oval((self.row_position * 38) + 60,
                                     (self.column_position * 16) + 67,
                                     (self.row_position * 38) + 98,
                                     (self.column_position * 16) + 87,
                                     fill=self.bg_color, width=4, outline=self.color, tags='canvas_change')

        self.right_frame.create_line((self.row_position * 38) + 66,
                                     (16 * self.column_position) + 82,
                                     (self.row_position * 38) + 79,
                                     (16 * self.column_position) + 72,

                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        self.right_frame.create_line((self.row_position * 38) + 92,
                                     (16 * self.column_position) + 83,
                                     (self.row_position * 38) + 79,
                                     (16 * self.column_position) + 72,

                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')


# RIGHT MOUSE BUTTON CLICKED FIRST TIME, KNOT FROM TOP TO BOTTOM:  "\"
class Knot3x:
    def __init__(self, color, color_1, row_position, column_position, frame, bg_color, threads_num):
        self.color = color
        self.color_1 = color_1
        self.row_position = row_position
        self.threads_num = threads_num
        self.column_position = (threads_num - 2) - column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):

        self.right_frame.create_line((38 * self.row_position) + 90,
                                     (16 * self.column_position) + 86,
                                     (38 * self.row_position) + 98,
                                     (16 * self.column_position) + 86,
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        self.right_frame.create_line((38 * self.row_position) + 90,
                                     (16 * self.column_position) + 70,
                                     (38 * self.row_position) + 98,
                                     (16 * self.column_position) + 70,

                                     fill=self.color_1, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        # OVAL
        self.right_frame.create_oval((self.row_position * 38) + 60,
                                     (self.column_position * 16) + 67,
                                     (self.row_position * 38) + 98,
                                     (self.column_position * 16) + 87,

                                     fill=self.bg_color, width=4, outline=self.color, tags='canvas_change')

        self.right_frame.create_line(
                                     (self.row_position * 38) + 69,
                                     (16 * self.column_position) + 67,
                                     (self.row_position * 38) + 90,
                                    (16 * self.column_position) + 87,
                                     fill=self.color, width=4, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')


# RIGHT MOUSE BUTTON CLICKED SECOND TIME, KNOT FROM TOP TO TOP:  "\/"
class Knot4x:
    def __init__(self, color, row_position, column_position, frame, bg_color, threads_num):
        self.color = color
        self.row_position = row_position
        self.threads_num = threads_num
        self.column_position = (threads_num - 2) - column_position
        self.right_frame = frame
        self.bg_color = bg_color
        self.draw()

    def draw(self):
        # OVAL
        self.right_frame.create_oval((self.row_position * 38) + 60,
                                     (self.column_position * 16) + 67,
                                     (self.row_position * 38) + 98,
                                     (self.column_position * 16) + 87,
                                     fill=self.bg_color, width=4, outline=self.color, tags='canvas_change')

        self.right_frame.create_line((self.row_position * 38) + 81,
                                     (16 * self.column_position) + 83,
                                     (self.row_position * 38) + 69,
                                     (16 * self.column_position) + 70,

                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')

        self.right_frame.create_line((self.row_position * 38) + 90,
                                     (16 * self.column_position) + 71,
                                     (self.row_position * 38) + 78,
                                     (16 * self.column_position) + 83,

                                     fill=self.color, width=5, joinstyle=tk.ROUND, smooth=True, tags='canvas_change')