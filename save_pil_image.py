from PIL import Image, ImageDraw, ImageFont
from tkinter.filedialog import asksaveasfile
import os


def save_image_test(self):
    x1, y1, x2, y2 = self.canvas_lf.bbox('all')
    w, h = x2 - x1 + 50, (y2 - y1) // 2
    self.canvas_lf.postscript(file="Result.eps", x=x1, y=y1, width=w, height=h, pagewidth=w, pageheight=h)
    Image.open("Result.eps")
    image1 = Image.new("RGB", (w, h), self.main_bg_color)
    draw = ImageDraw.Draw(image1)
    print("save", w, h)

    # Create Header
    # 'CREATED BY'
    line_counter = 0
    line_y = 10 + (line_counter * 20)
    # 'TEXT' 0
    if self.myEntryBox_0.get():
        draw.text((10, 10), self.myEntryBox_0.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 1
    if self.myEntryBox_1.get():
        draw.text((10, line_y), self.myEntryBox_1.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 2
    if self.myEntryBox_2.get():
        draw.text((10, line_y), self.myEntryBox_2.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 3
    if self.myEntryBox_3.get():
        draw.text((10, line_y), self.myEntryBox_3.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 4
    if self.myEntryBox_4.get():
        draw.text((10, line_y), self.myEntryBox_4.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 5
    if self.myEntryBox_5.get():
        draw.text((10, line_y), self.myEntryBox_5.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 6
    if self.myEntryBox_6.get():
        draw.text((10, line_y), self.myEntryBox_6.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 7
    if self.myEntryBox_7.get():
        draw.text((10, line_y), self.myEntryBox_7.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 8
    if self.myEntryBox_8.get():
        draw.text((10, line_y), self.myEntryBox_8.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 9
    if self.myEntryBox_9.get():
        draw.text((10, line_y), self.myEntryBox_9.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 10
    if self.myEntryBox_10.get():
        draw.text((10, line_y), self.myEntryBox_10.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 11
    if self.myEntryBox_11.get():
        draw.text((10, line_y), self.myEntryBox_11.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # 'TEXT' 12
    if self.myEntryBox_12.get():
        draw.text((10, line_y), self.myEntryBox_12.get(), fill='#2C2C29', align="right",
                  font=ImageFont.truetype("arial.ttf", 15))
        line_counter += 1

    # # 'LABEL'
    # text = 'KNOTWIZARD'
    # draw.text((x2 - 50, 20), text, fill='grey', align="right",
    #           font=ImageFont.load_default())

    # Add Labels to rows in PIL
    for i in range(self.rows.get()):
        label_row_pad = 30
        text = str(i + 1)
        font = ImageFont.truetype("arial.ttf", 8)
        draw.text((label_row_pad, (line_y + 117) + (i * 38)), text, fill='grey', align="right", font=font)

    # Draw Color Picker boxes
    for i in range(len(self.colors_list)):
        draw.line([(20 * i) + 70, (line_y + 50), (20 * i) + 70, (line_y + 60)], fill=self.colors_list[i], width=10)

    # Draw Center Line
    if self.threads.get() % 2 == 0:
        center = self.threads.get() // 2
        draw.line([(20 * center) + 60, (line_y + 70), (20 * center) + 60, (line_y + 75)], fill='grey', width=2)

    if self.threads.get() % 2 != 0:
        center = self.threads.get() // 2
        draw.line([(20 * center) + 70, (line_y + 70), (20 * center) + 70, (line_y + 75)], fill='grey', width=2)

    # Draw lines
    for i in range(self.rows.get()):
        for j in range(self.threads.get()):
            color_num = self.threads_colors_array[i][j]
            color = self.colors_list[color_num]
            draw.line([(20 * j) + 70, (38 * i) + (line_y + 100),
                       (20 * j) + 70, (38 * i) + (line_y + 138)],
                      fill=color, width=4)

    class PilKnot1:

        def __init__(self, color, color_1, row_position, column_position):
            self.color = color
            self.color_1 = color_1
            self.row_position = row_position
            self.column_position = column_position
            self.draw()

        def draw(self):
            oval_shape = [((20 * self.column_position) + 65,
                           (self.row_position * 38) + (line_y + 104)),
                          ((20 * self.column_position) + 95,
                           (self.row_position * 38) + (line_y + 134))]
            draw.ellipse(oval_shape, fill='#DDDCD1', width=2, outline=self.color)

            line_shape = [((20 * self.column_position) + 69,
                           (self.row_position * 38) + (line_y + 109)),
                          ((20 * self.column_position) + 90,
                           (self.row_position * 38) + (line_y + 130))]
            draw.line(line_shape, fill=self.color, width=3)

            line_shape = [((20 * self.column_position) + 70,
                           (self.row_position * 38) + (line_y + 130)),
                          ((20 * self.column_position) + 70,
                           (self.row_position * 38) + (line_y + 138))]
            draw.line(line_shape, fill=self.color_1, width=4)

            line_shape = [((20 * self.column_position) + 90,
                           (self.row_position * 38) + (line_y + 130)),
                          ((20 * self.column_position) + 90,
                           (self.row_position * 38) + (line_y + 138))]
            draw.line(line_shape, fill=self.color, width=4)

    class PilKnot2:
        def __init__(self, color, row_position, column_position):
            self.color = color
            self.row_position = row_position
            self.column_position = column_position
            self.draw()

        def draw(self):
            oval_shape = [((20 * self.column_position) + 65,
                           (self.row_position * 38) + (line_y + 104)),
                          ((20 * self.column_position) + 95,
                           (self.row_position * 38) + (line_y + 134))]
            draw.ellipse(oval_shape, fill='#DDDCD1', width=2, outline=self.color)

            line_shape = [((20 * self.column_position) + 69,
                           (self.row_position * 38) + (line_y + 108)),
                          ((20 * self.column_position) + 82,
                           (self.row_position * 38) + (line_y + 119))]
            draw.line(line_shape, fill=self.color, width=3)

            line_shape = [((20 * self.column_position) + 83,
                           (self.row_position * 38) + (line_y + 120)),
                          ((20 * self.column_position) + 70,
                           (self.row_position * 38) + (line_y + 131))]
            draw.line(line_shape, fill=self.color, width=3)

    class PilKnot3:

        def __init__(self, color, color_1, row_position, column_position):
            self.color = color
            self.color_1 = color_1
            self.row_position = row_position
            self.column_position = column_position
            self.draw()

        def draw(self):
            oval_shape = [((20 * self.column_position) + 65,
                           (self.row_position * 38) + (line_y + 104)),
                          ((20 * self.column_position) + 95,
                           (self.row_position * 38) + (line_y + 134))]
            draw.ellipse(oval_shape, fill='#DDDCD1', width=2, outline=self.color)

            line_shape = [((20 * self.column_position) + 90,
                           (self.row_position * 38) + (line_y + 109)),
                          ((20 * self.column_position) + 69,
                           (self.row_position * 38) + (line_y + 130))]
            draw.line(line_shape, fill=self.color, width=3)

            line_shape = [((20 * self.column_position) + 70,
                           (self.row_position * 38) + (line_y + 130)),
                          ((20 * self.column_position) + 70,
                           (self.row_position * 38) + (line_y + 138))]
            draw.line(line_shape, fill=self.color, width=4)

            line_shape = [((20 * self.column_position) + 90,
                           (self.row_position * 38) + (line_y + 130)),
                          ((20 * self.column_position) + 90,
                           (self.row_position * 38) + (line_y + 138))]
            draw.line(line_shape, fill=self.color_1, width=4)

    class PilKnot4:

        def __init__(self, color, row_position, column_position):
            self.color = color
            self.row_position = row_position
            self.column_position = column_position
            self.draw()

        def draw(self):
            oval_shape = [((20 * self.column_position) + 65,
                           (self.row_position * 38) + (line_y + 104)),
                          ((20 * self.column_position) + 95,
                           (self.row_position * 38) + (line_y + 134))]
            draw.ellipse(oval_shape, fill='#DDDCD1', width=2, outline=self.color)

            line_shape = [((20 * self.column_position) + 91,
                           (self.row_position * 38) + (line_y + 108)),
                          ((20 * self.column_position) + 79,
                           (self.row_position * 38) + (line_y + 119))]
            draw.line(line_shape, fill=self.color, width=4)

            line_shape = [((20 * self.column_position) + 79,
                           (self.row_position * 38) + (line_y + 118)),
                          ((20 * self.column_position) + 91,
                           (self.row_position * 38) + (line_y + 131))]

            draw.line(line_shape, fill=self.color, width=4)

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
                    PilKnot1(color, color_1, i, j * 2)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]

                    right_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_1 = self.colors_list[right_thread]

                    PilKnot1(color, color_1, i, (j * 2) + 1)

            if self.main_array[i][j] == 2:
                if i % 2 == 0:
                    left_thread = self.threads_colors_array[i][j * 2]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot2(color, i, j * 2)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot2(color, i, (j * 2) + 1)

            if self.main_array[i][j] == 3:
                if i % 2 == 0:
                    right_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_num = right_thread
                    color = self.colors_list[color_num]

                    left_thread = self.threads_colors_array[i][(j * 2)]
                    color_1 = self.colors_list[left_thread]
                    PilKnot3(color, color_1, i, j * 2)
                else:
                    right_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_num = right_thread
                    color = self.colors_list[color_num]

                    left_thread = self.threads_colors_array[i][(j * 2) + 1]
                    color_1 = self.colors_list[left_thread]
                    PilKnot3(color, color_1, i, (j * 2) + 1)

            if self.main_array[i][j] == 4:
                if i % 2 == 0:
                    left_thread = self.threads_colors_array[i][j * 2 + 1]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot4(color, i, j * 2)
                else:
                    left_thread = self.threads_colors_array[i][(j * 2) + 2]
                    color_num = left_thread
                    color = self.colors_list[color_num]
                    PilKnot4(color, i, (j * 2) + 1)

    # save frame image
    file = asksaveasfile(mode='w', initialfile='my_bracelet.png', defaultextension=".png",
                         filetypes=(("PNG file", "*.png"), ("GIF file", "*.gif"), ("JPG file", "*.jpg"),
                                    ("BMP file", "*.bmp"), ("All Files", "*.*")))

    # save image to the input file name
    if file:
        abs_path = os.path.abspath(file.name)
        image1.save(abs_path)