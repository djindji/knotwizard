
from PIL import Image, ImageDraw, ImageFont
from tkinter.filedialog import asksaveasfile
from pathlib import Path
import sys

if sys.platform.startswith('win'):
    entry_font = ImageFont.truetype('arial.ttf', size=12)

else:
    entry_font = ImageFont.load_default()


def save_pattern_to_img(self):
    # get dimensions and all children of "self.canvas_lf" tk.Canvas widget
    x1, y1, x2, y2 = self.canvas_lf.bbox('all')

    # create dimensions for image
    if self.vert_view:
        w, h = x2 - x1 + 50, (self.rows_num * 41) + 800
    else:
        w, h = y2 - y1 + 50, (self.rows_num * 41) + 800

    if w < 405:
        w = 405
    # store the graphical representation of "self.canvas_lf" to file "Result.eps"
    self.canvas_lf.postscript(file="Result.eps", x=x1, y=y1, width=w, height=h, pagewidth=w, pageheight=h)

    # read file "Result.eps"
    Image.open("Result.eps")

    # create new object, set mode to "RGB", set dimensions and background color
    image1 = Image.new("RGB", (w, h), self.main_bg_color)

    # draw to object
    draw = ImageDraw.Draw(image1)

    # 'info text'
    text = "KnotWizard project:\n\nLet's create the best\n friendship bracelet pattern editor. \n\n"  \
           ' For the latest stable version or \ndonations  please visit:\n knotwizard.com \n\n' \
           ' Application created in Python 3.10 \n'  \
           ' Open source code:\n  github.com/djindji/knotwizard \n \n' \
           ' Feel free to fork.\n\n' \
           '                     Kindest regards,\n' \
           '                                  Eduard Kruminsh'

    draw.text(((w // 2) - 94, 10), text, fill='black', align="center", font=entry_font, encoding="uni")

    # draw underline
    cur_x = 0
    cur_y = 310
    image_width = w
    for x in range(cur_x, image_width, 14):
        draw.line([(x, cur_y), (x + 7, cur_y)], fill='black')

    # # User info input area
    # read tk.Entry widgets (self.myEntryBox_(0-12) if not empty and increase line_counter by 1
    if self.myEntryBox_0.get():
        # text attributes
        draw.text((10, 10 + (self.line_counter * 20)), self.myEntryBox_0.get(), fill='#2C2C29', align="right",
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

    # Draw lines/threads
    for i in range(self.rows.get()):
        for j in range(self.threads.get()):
            color_num = self.threads_colors_array[i][j]
            color = self.colors_list[color_num]
            draw.line([(16 * j) + 70, (38 * i) + ((self.line_counter * 20) + 110),
                       (16 * j) + 70, (38 * i) + ((self.line_counter * 20) + 148)],
                      fill=color, width=4)

    # create Classes for knots drawing
    class PilKnot1:
        def __init__(self, color1, color2, row_position, column_position, counter, bg_color):
            self.color = color1
            self.color_1 = color2
            self.row_position = row_position
            self.column_position = column_position
            self.counter = counter
            self.bg_color = bg_color
            self.draw()

        def draw(self):
            oval_shape = [((16 * self.column_position) + 67,
                           (self.row_position * 38) + (self.counter * 20) + 114),
                          ((16 * self.column_position) + 89,
                           (self.row_position * 38) + ((self.counter * 20) + 152))]
            draw.ellipse(oval_shape, fill=self.bg_color, width=4, outline=self.color)

            line_shape = [((16 * self.column_position) + 71,
                           (self.row_position * 38) + ((self.counter * 20) + 124)),
                          ((16 * self.column_position) + 87,
                           (self.row_position * 38) + ((self.counter * 20) + 147))]
            draw.line(line_shape, fill=self.color, width=5)

    class PilKnot2:
        def __init__(self, color1, row_position, column_position, counter, bg_color):
            self.color = color1
            self.row_position = row_position
            self.column_position = column_position
            self.counter = counter
            self.bg_color = bg_color
            self.draw()

        def draw(self):
            oval_shape = [((16 * self.column_position) + 67,
                           (self.row_position * 38) + (self.counter * 20) + 114),
                          ((16 * self.column_position) + 89,
                           (self.row_position * 38) + ((self.counter * 20) + 152))]
            draw.ellipse(oval_shape, fill=self.bg_color, width=4, outline=self.color)

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
        def __init__(self, color1, color2, row_position, column_position, counter, bg_color):
            self.color = color1
            self.color_1 = color2
            self.row_position = row_position
            self.column_position = column_position
            self.counter = counter
            self.bg_color = bg_color
            self.draw()

        def draw(self):
            oval_shape = [((16 * self.column_position) + 68,
                           (self.row_position * 38) + (self.counter * 20) + 114),
                          ((16 * self.column_position) + 89,
                           (self.row_position * 38) + ((self.counter * 20) + 152))]
            draw.ellipse(oval_shape, fill=self.bg_color, width=4, outline=self.color)

            line_shape = [((16 * self.column_position) + 87,
                           (self.row_position * 38) + ((self.counter * 20) + 124)),
                          ((16 * self.column_position) + 71,
                           (self.row_position * 38) + ((self.counter * 20) + 147))]
            draw.line(line_shape, fill=self.color, width=5)

    class PilKnot4:
        def __init__(self, color1, row_position, column_position, counter, bg_color):
            self.color = color1
            self.row_position = row_position
            self.column_position = column_position
            self.counter = counter
            self.bg_color = bg_color
            self.draw()

        def draw(self):
            oval_shape = [((16 * self.column_position) + 67,
                           (self.row_position * 38) + (self.counter * 20) + 114),
                          ((16 * self.column_position) + 89,
                           (self.row_position * 38) + ((self.counter * 20) + 152))]
            draw.ellipse(oval_shape, fill=self.bg_color, width=4, outline=self.color)

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
                    PilKnot1(color, color_1, i, j * 2, self.line_counter, self.main_bg_color)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]

                    right_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_1 = self.colors_list[right_thread]

                    PilKnot1(color, color_1, i, (j * 2) + 1, self.line_counter, self.main_bg_color)

            if self.main_array[i][j] == 2:
                if i % 2 == 0:
                    left_thread = self.threads_colors_array[i][j * 2]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot2(color, i, j * 2, self.line_counter, self.main_bg_color)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot2(color, i, (j * 2) + 1, self.line_counter, self.main_bg_color)

            if self.main_array[i][j] == 3:
                if i % 2 == 0:
                    right_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = right_thread
                    color = self.colors_list[color_num]

                    left_thread = self.threads_colors_array[i][(j * 2)]
                    color_1 = self.colors_list[left_thread]
                    PilKnot3(color, color_1, i, j * 2, self.line_counter, self.main_bg_color)
                else:
                    right_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_num = right_thread
                    color = self.colors_list[color_num]

                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_1 = self.colors_list[left_thread]
                    PilKnot3(color, color_1, i, (j * 2) + 1, self.line_counter, self.main_bg_color)

            if self.main_array[i][j] == 4:
                if i % 2 == 0:
                    left_thread = self.threads_colors_array[i][j * 2 + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot4(color, i, j * 2, self.line_counter, self.main_bg_color)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot4(color, i, (j * 2) + 1, self.line_counter, self.main_bg_color)

    # current directory
    current_directory = Path.cwd()

    # file save open dialog
    file = asksaveasfile(mode='w', initialfile='my_bracelet.png', defaultextension=".png", initialdir=current_directory,
                         filetypes=(("PNG file", "*.png"), ("GIF file", "*.gif")))

    # save image object to the file
    if file:
        file_path = Path(file.name)
        image1.save(file_path, quality='keep')
