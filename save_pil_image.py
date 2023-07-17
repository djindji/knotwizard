
from PIL import Image, ImageDraw, ImageFont
from tkinter.filedialog import asksaveasfile
from pathlib import Path

# Image users text font
entry_font = ImageFont.truetype('arial.ttf', size=16, encoding="uni")
# application links font
entry_font_1 = ImageFont.truetype('arial.ttf', size=12, encoding="uni")

# padding from top depends on : how much "tk.Entry" widgets was filled
noempty_entr_counter = 0




def save_image_test(self):
    # get dimensions and all children of "self.canvas_lf" tk.Canvas widget
    x1, y1, x2, y2 = self.canvas_lf.bbox('all')

    # create dimensions for image
    w, h = x2 - x1 + 50, (self.rows_num * 41) + 400
    # print("image dimensions", w, h)

    # store the graphical representation of "self.canvas_lf" to file "Result.eps"
    self.canvas_lf.postscript(file="Result.eps", x=x1, y=y1, width=w, height=h, pagewidth=w, pageheight=h)

    # read file "Result.eps"
    Image.open("Result.eps")

    # create new object, set mode to "RGB", set dimensions and background color
    image1 = Image.new("RGB", (w, h), self.main_bg_color)

    # draw to object
    draw = ImageDraw.Draw(image1)

    # # User info input area
    # read tk.Entry widgets (self.myEntryBox_(0-12) if not empty and increase line_counter by 1
    if self.myEntryBox_0.get():
        # text attributes
        draw.text((10, 10), self.myEntryBox_0.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        # increase line_counter by 1
        self.line_counter += 1

    if self.myEntryBox_1.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_1.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_2.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_2.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_3.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_3.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_4.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_4.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_5.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_5.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_6.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_6.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_7.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_7.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_8.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_8.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_9.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_9.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_10.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_10.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_11.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_11.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    if self.myEntryBox_12.get():
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_12.get(), fill='#2C2C29', align="right",
                  font=entry_font)
        self.line_counter += 1

    # App info

    text = 'download pattern editor: KNOTWIZARD.COM'
    draw.text((10, 10 + (self.line_counter * 20)), text, fill='black', align="center", font=entry_font_1)
    self.line_counter += 1

    text_1 = 'SOURCE: github.com/djindji/knotwizard  (Python 3.10)'
    draw.text((10, 10 + (self.line_counter * 20)), text_1, fill='black', align="center", font=entry_font_1)


    # Draw rows numbers
    for i in range(self.rows.get()):
        label_row_pad = 30
        text = str(i + 1)

        draw.text((label_row_pad, (10 + (self.line_counter * 20) + 117) + (i * 38)), text, fill='grey', align="right",
                  font=entry_font)

    # Draw Color Picker boxes
    for i in range(self.threads_start_num):
        draw.line(
            [(16 * i) + 70, ((self.line_counter * 20) + 60), (16 * i) + 70, ((self.line_counter * 20) + 70)],
            fill=self.colors_list[i],
            width=10)

    # Draw Center Line for even threads number
    if self.threads.get() % 2 == 0:
        center = self.threads.get() // 2
        draw.line([(16 * center) + 60, ((self.line_counter * 20) + 80),
                   (16 * center) + 60, ((self.line_counter * 20) + 90)],
                  fill='grey', width=2)

    # Draw Center Line for not even threads number
    if self.threads.get() % 2 != 0:
        center = self.threads.get() // 2
        draw.line([(16 * center) + 70, ((self.line_counter * 20) + 80),
                   (16 * center) + 70, ((self.line_counter * 20) + 90)],
                  fill='grey', width=2)

    # Draw lines
    for i in range(self.rows.get()):
        for j in range(self.threads.get()):
            color_num = self.threads_colors_array[i][j]
            color = self.colors_list[color_num]
            draw.line([(16 * j) + 70, (38 * i) + ((self.line_counter * 20) + 110),
                       (16 * j) + 70, (38 * i) + ((self.line_counter * 20) + 148)],
                      fill=color, width=4)

    # create Classes for knots drawing
    class PilKnot1:
        def __init__(self, color, color_1, row_position, column_position, counter):
            self.color = color
            self.color_1 = color_1
            self.row_position = row_position
            self.column_position = column_position
            self.counter = counter
            self.draw()

        def draw(self):
            oval_shape = [((16 * self.column_position) + 67,
                           (self.row_position * 38) + (self.counter * 20) + 114),
                          ((16 * self.column_position) + 89,
                           (self.row_position * 38) + ((self.counter * 20) + 152))]
            draw.ellipse(oval_shape, fill='#DDDCD1', width=4, outline=self.color)

            line_shape = [((16 * self.column_position) + 71,
                           (self.row_position * 38) + ((self.counter * 20) + 124)),
                          ((16 * self.column_position) + 87,
                           (self.row_position * 38) + ((self.counter * 20) + 147))]
            draw.line(line_shape, fill=self.color, width=5)

            # line_shape = [((18 * self.column_position) + 70,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 140)),
            #               ((18 * self.column_position) + 70,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 148))]
            # draw.line(line_shape, fill=self.color_1, width=2)
            #
            # line_shape = [((18 * self.column_position) + 90,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 140)),
            #               ((18 * self.column_position) + 90,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 148))]
            # draw.line(line_shape, fill=self.color, width=2)

    class PilKnot2:
        def __init__(self, color, row_position, column_position, counter):
            self.color = color
            self.row_position = row_position
            self.column_position = column_position
            self.counter = counter
            self.draw()

        def draw(self):
            oval_shape = [((16 * self.column_position) + 67,
                           (self.row_position * 38) + (self.counter * 20) + 114),
                          ((16 * self.column_position) + 89,
                           (self.row_position * 38) + ((self.counter * 20) + 152))]
            draw.ellipse(oval_shape, fill='#DDDCD1', width=4, outline=self.color)

            line_shape = [((16 * self.column_position) + 71,
                           (self.row_position * 38) + ((self.counter * 20) + 120)),
                          ((16 * self.column_position) + 86,
                           (self.row_position * 38) + ((self.counter * 20) + 135))]
            draw.line(line_shape, fill=self.color, width=6)

            line_shape = [((16 * self.column_position) + 86,
                           (self.row_position * 38) + ((self.counter * 20) + 135)),
                          ((16 * self.column_position) + 72,
                           (self.row_position * 38) + ((self.counter * 20) + 149))]
            draw.line(line_shape, fill=self.color, width=6)

    class PilKnot3:
        def __init__(self, color, color_1, row_position, column_position, counter):
            self.color = color
            self.color_1 = color_1
            self.row_position = row_position
            self.column_position = column_position
            self.counter = counter
            self.draw()

        def draw(self):
            oval_shape = [((16 * self.column_position) + 68,
                           (self.row_position * 38) + (self.counter * 20) + 114),
                          ((16 * self.column_position) + 89,
                           (self.row_position * 38) + ((self.counter * 20) + 152))]
            draw.ellipse(oval_shape, fill='#DDDCD1', width=4, outline=self.color)

            line_shape = [((16 * self.column_position) + 87,
                           (self.row_position * 38) + ((self.counter * 20) + 124)),
                          ((16 * self.column_position) + 71,
                           (self.row_position * 38) + ((self.counter * 20) + 147))]
            draw.line(line_shape, fill=self.color, width=5)

            # line_shape = [((20 * self.column_position) + 90,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 109)),
            #               ((20 * self.column_position) + 69,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 130))]
            # draw.line(line_shape, fill=self.color, width=5)
            #
            # line_shape = [((20 * self.column_position) + 70,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 130)),
            #               ((20 * self.column_position) + 70,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 138))]
            # draw.line(line_shape, fill=self.color, width=2)
            #
            # line_shape = [((20 * self.column_position) + 90,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 130)),
            #               ((20 * self.column_position) + 90,
            #                (self.row_position * 38) + (10 + (self.counter * 20) + 138))]
            # draw.line(line_shape, fill=self.color_1, width=2)

    class PilKnot4:
        def __init__(self, color, row_position, column_position, counter):
            self.color = color
            self.row_position = row_position
            self.column_position = column_position
            self.counter = counter
            self.draw()

        def draw(self):
            oval_shape = [((16 * self.column_position) + 67,
                           (self.row_position * 38) + (self.counter * 20) + 114),
                          ((16 * self.column_position) + 89,
                           (self.row_position * 38) + ((self.counter * 20) + 152))]
            draw.ellipse(oval_shape, fill='#DDDCD1', width=4, outline=self.color)

            line_shape = [((16 * self.column_position) + 86,
                           (self.row_position * 38) + ((self.counter * 20) + 120)),
                          ((16 * self.column_position) + 71,
                           (self.row_position * 38) + ((self.counter * 20) + 135))]
            draw.line(line_shape, fill=self.color, width=6)

            line_shape = [((16 * self.column_position) + 72,
                           (self.row_position * 38) + ((self.counter * 20) + 135)),
                          ((16 * self.column_position) + 86,
                           (self.row_position * 38) + ((self.counter * 20) + 149))]
            draw.line(line_shape, fill=self.color, width=6)

    # draw knots
    for i in range(len(self.main_array)):
        for j in range(len(self.main_array[i])):
            if self.main_array[i][j] == 1:
                if i % 2 == 0:
                    left_thread = self.threads_colors_array[i][j * 2]
                    color_num = left_thread
                    color = self.colors_list[color_num]

                    right_thread = self.threads_colors_array[i][j * 2 + 1]
                    color_1 = self.colors_list[right_thread]
                    PilKnot1(color, color_1, i, j * 2, self.line_counter)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]

                    right_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_1 = self.colors_list[right_thread]

                    PilKnot1(color, color_1, i, (j * 2) + 1, self.line_counter)

            if self.main_array[i][j] == 2:
                if i % 2 == 0:
                    left_thread = self.threads_colors_array[i][j * 2]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot2(color, i, j * 2, self.line_counter)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot2(color, i, (j * 2) + 1, self.line_counter)

            if self.main_array[i][j] == 3:
                if i % 2 == 0:
                    right_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = right_thread
                    color = self.colors_list[color_num]

                    left_thread = self.threads_colors_array[i][(j * 2)]
                    color_1 = self.colors_list[left_thread]
                    PilKnot3(color, color_1, i, j * 2, self.line_counter)
                else:
                    right_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_num = right_thread
                    color = self.colors_list[color_num]

                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_1 = self.colors_list[left_thread]
                    PilKnot3(color, color_1, i, (j * 2) + 1, self.line_counter)

            if self.main_array[i][j] == 4:
                if i % 2 == 0:
                    left_thread = self.threads_colors_array[i][j * 2 + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot4(color, i, j * 2, self.line_counter)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot4(color, i, (j * 2) + 1, self.line_counter)

    # file save open dialog
    file = asksaveasfile(mode='w', initialfile='my_bracelet.png', defaultextension=".png",
                         filetypes=(("PNG file", "*.png"), ("GIF file", "*.gif"), ("JPG file", "*.jpg"),
                                    ("BMP file", "*.bmp"), ("All Files", "*.*")))

    # save image object to the file
    if file:
        file_path = Path(file.name)
        image1.save(file_path, quality='keep')






