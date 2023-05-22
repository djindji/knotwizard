# import necessary libraries
import tkinter as tk
import seaborn as sns
import knots
from save_pil_image import *
from pathlib import Path

from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfile, askopenfilename
import atexit
import framework
from PIL import Image, ImageDraw, ImageFont
import os
import ast
import shutil

app_path = Path.cwd()


class MainProgram(framework.Framework):
    tool_bar_functions = ("add_two_thread_from_left",
                          "drop_two_thread_from_left",
                          "add_rows_top",
                          "drop_rows_top",
                          "snapshot_plus",
                          "snapshot_minus")

    # For app to start we need threads and rows num to start knots array creation
    threads_start_num = 8
    rows_num = 10
    colors_list = []
    threads_colors_array = []

    # Create variable to hold add/ drop situation. if we add 'not even' number to threads from LEFT
    left_add_drop_sit = 0

    # Rows number column show/hide
    hidden = True

    main_array = []

    colors_bg_test = list(reversed(sns.color_palette("Set3", 20).as_hex()))
    # main_bg_color = colors_bg_test[3] #dddcd1
    main_bg_color = '#dddcd1'

    snapshot_counter = 0

    line_counter = 0

    def __init__(self, root):
        # Threads and Rows integers o
        self.threads = tk.IntVar()
        self.rows = tk.IntVar()

        self.checkCmd = tk.StringVar()
        self.checkCmd_1 = tk.StringVar()
        self.checkCmd_2 = tk.StringVar()
        self.checkCmd_3 = tk.StringVar()


        self.selected_toolbar_func_index = tk.StringVar()

        self.menubar = tk.Menu()
        self.canvas = tk.Canvas()

        self.window = tk.Frame
        self.top_frame = tk.Frame
        self.snp_frame = tk.Frame
        self.left_frame = tk.Frame
        self.canvas_lf = tk.Canvas
        self.root = root

        self.main_window()
        self.on_check()
        self.on_check_1()
        self.on_check_2()
        self.on_check_3()

        self.create_main_array()
        self.colors()
        self.threads_colors_array_handler()
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()
        self.create_menu()

    # VISUALISATION
    def main_window(self):
        # Save monitor dimensions (width and height) to variables
        monitor_width = self.root.winfo_screenwidth()
        monitor_height = self.root.winfo_screenheight()
        self.threads.set(self.threads_start_num)

        # Create main frame
        self.window = tk.Frame(self.root,
                               width=monitor_width * 0.75,
                               height=monitor_height,
                               bg=self.main_bg_color)

        self.top_frame = tk.Frame(self.window, bg=self.main_bg_color)

        # Create icons tuple
        icons = ('2plus', '2drop', 'add_rows', 'drop_rows', 'snapshot', 'drop_snapshot')
        for i, icon in enumerate(icons):
            if i == 0:

                tool_bar_icon = tk.PhotoImage(file='icons/{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon, command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=6)

            if i == 1:
                tool_bar_icon = tk.PhotoImage(file='icons/{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon, command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=6)

                thread_spinbox_right = tk.Spinbox(self.top_frame,
                                                  from_=6,
                                                  to=40,
                                                  width=2,
                                                  textvariable=self.threads,
                                                  font=("Arial", 26, 'bold'),
                                                  command=self.add_drop_thread_from_right,
                                                  foreground=self.main_bg_color
                                                  )
                # Put thread_spinbox on top_frame
                thread_spinbox_right.pack(side='left')
                # when user put number and hit enter
                thread_spinbox_right.bind("<Return>", (lambda event: self.add_drop_thread_from_right()))
                tk.Label(self.top_frame, bg=self.main_bg_color, width=10).pack(side='left')

            if i == 2:
                tool_bar_icon = tk.PhotoImage(file='icons/{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon, command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=6)

            if i == 3:
                tool_bar_icon = tk.PhotoImage(file='icons/{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon,
                                     command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=6)

                self.rows.set(self.rows_num)

                # rows = 20
                row_widget = tk.Spinbox(self.top_frame,
                                        from_=2, to=60, width=3,
                                        textvariable=self.rows,
                                        font=("Arial", 26, 'bold'),
                                        foreground=self.main_bg_color,
                                        command=self.add_drop_rows_bottom
                                        )
                row_widget.pack(side='left')
                row_widget.bind("<Return>", lambda event: self.add_drop_rows_bottom())
                tk.Label(self.top_frame, bg=self.main_bg_color, width=10).pack(side='left')

                tk.Label(self.top_frame, bg=self.main_bg_color, width=2).pack(side='left')

        self.snp_frame = tk.Frame(self.top_frame, bg=self.main_bg_color)

        self.checkCmd.set('0')

        tk.Checkbutton(self.snp_frame,
                       variable=self.checkCmd,
                       indicatoron=True,
                       activebackground='black',
                       background=self.main_bg_color,
                       selectcolor="white",
                       width=1,

                       foreground="black",
                       command=lambda: self.on_check()).grid(row=0, sticky='n')

        self.checkCmd_1.set('0')
        tk.Checkbutton(self.snp_frame,
                       variable=self.checkCmd_1,
                       indicatoron=True,
                       activebackground='black',
                       background=self.main_bg_color,
                       selectcolor="white",
                       width=1,

                       foreground="black",
                       command=lambda: self.on_check_1()
                       ).grid(row=0, column=3, sticky='n')

        self.checkCmd_2.set('0')

        tk.Checkbutton(self.snp_frame,
                       variable=self.checkCmd_2,
                       indicatoron=True,
                       activebackground='black',
                       background=self.main_bg_color,
                       selectcolor="white",
                       width=1,

                       foreground="black",
                       command=lambda: self.on_check_2()).grid(row=0, column=5, sticky='n')

        self.checkCmd_3.set('0')

        tk.Checkbutton(self.snp_frame,
                       variable=self.checkCmd_3,
                       indicatoron=True,
                       activebackground='black',
                       background=self.main_bg_color,
                       selectcolor="white",
                       width=1,

                       foreground="black",
                       command=lambda: self.on_check_3()).grid(row=0, column=7, sticky='n')

        self.snp_frame.pack(side='left')
        self.top_frame.pack(side="left", anchor='n')

        self.window.pack(anchor='w', fill=tk.X,)

        # Create left frame for pattern editor 50% from monitor width and height with scrolling depend on rows number
        self.left_frame = tk.Frame(self.root,
                                   width=monitor_width,
                                   # for scrolling to be visible
                                   height=monitor_height,
                                   bg=self.main_bg_color,
                                   )

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=monitor_width,
                                   height=monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 50))

        scrollbar = tk.Scrollbar(self.left_frame)
        scrollbar.pack(side="right", fill="y")
        scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5,)

    def on_check(self):

        if self.checkCmd.get() == "0":
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='1', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=1)

        if self.checkCmd.get() == "1":

            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='1', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot()).grid(row=0, column=1)

            # Dictionary

            my_dict = {'colors': self.colors_list,
                       'knots': self.main_array,
                       'threads': self.threads_colors_array,
                       'rows_num': self.rows_num,
                       'threads_start_num': self.threads_start_num,
                       'left_add_drop_sit': self.left_add_drop_sit}

            # current directory
            current_directory = Path.cwd()
            # path to snapshots folder
            snap_dir_path = current_directory / "snapshots"

            # # # Create directory
            if not os.path.exists(snap_dir_path):
                try:
                    os.mkdir(snap_dir_path)
                except OSError as error:
                    print(error)

            # path to snapshot file
            path_to_file = snap_dir_path / "snapshot_1.txt"
            file = open(path_to_file, 'w')
            file.write(str(my_dict))
            file.close()

    def run_snapshot(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_dir_path = current_directory / "snapshots"

        # Path
        path_to_file = snap_dir_path / 'snapshot_1.txt'


        with open(path_to_file, 'r') as fp:
            data = fp.read()
            details = ast.literal_eval(data)
            self.colors_list = details['colors']
            self.main_array = details['knots']
            self.threads_colors_array = details['threads']
            self.rows_num = details['rows_num']
            self.threads_start_num = details['threads_start_num']
            self.left_add_drop_sit = details['left_add_drop_sit']

            self.canvas_lf.delete('all')
            self.color_picker_pad()
            self.draw_left_num_bar()
            self.draw_threads()
            self.draw_knots()
            self.put_buttons()

    def on_check_1(self):

        if self.checkCmd_1.get() == "0":
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='2', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=4)

        if self.checkCmd_1.get() == "1":

            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='2', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot_1()).grid(row=0, column=4)

            my_dict = {'colors': self.colors_list,
                       'knots': self.main_array,
                       'threads': self.threads_colors_array,
                       'rows_num': self.rows_num,
                       'threads_start_num': self.threads_start_num,
                       'left_add_drop_sit': self.left_add_drop_sit}

            # current directory
            current_directory = Path.cwd()
            # path to snapshots folder
            snap_dir_path = current_directory / "snapshots"

            # # # Create directory
            if not os.path.exists(snap_dir_path):
                try:
                    os.mkdir(snap_dir_path)
                except OSError as error:
                    print(error)

            # path to snapshot file
            path_to_file = snap_dir_path / "snapshot_2.txt"
            file = open(path_to_file, 'w')
            file.write(str(my_dict))
            file.close()

    def run_snapshot_1(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_dir_path = current_directory / "snapshots"

        # Path
        path_to_file = snap_dir_path / 'snapshot_2.txt'

        with open(path_to_file, 'r') as fp:
            data = fp.read()
            details = ast.literal_eval(data)
            self.colors_list = details['colors']
            self.main_array = details['knots']
            self.threads_colors_array = details['threads']
            self.rows_num = details['rows_num']
            self.threads_start_num = details['threads_start_num']
            self.left_add_drop_sit = details['left_add_drop_sit']

            self.canvas_lf.delete('all')
            self.color_picker_pad()
            self.draw_left_num_bar()
            self.draw_threads()
            self.draw_knots()
            self.put_buttons()

    def on_check_2(self):

        if self.checkCmd_2.get() == "0":
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='3', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=6)

        if self.checkCmd_2.get() == "1":

            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='3', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot_2()).grid(row=0, column=6)

            my_dict = {'colors': self.colors_list,
                       'knots': self.main_array,
                       'threads': self.threads_colors_array,
                       'rows_num': self.rows_num,
                       'threads_start_num': self.threads_start_num,
                       'left_add_drop_sit': self.left_add_drop_sit}

            # current directory
            current_directory = Path.cwd()
            # path to snapshots folder
            snap_dir_path = current_directory / "snapshots"

            # # # Create directory
            if not os.path.exists(snap_dir_path):
                try:
                    os.mkdir(snap_dir_path)
                except OSError as error:
                    print(error)

            # path to snapshot file
            path_to_file = snap_dir_path / "snapshot_3.txt"
            file = open(path_to_file, 'w')
            file.write(str(my_dict))
            file.close()

    def run_snapshot_2(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_dir_path = current_directory / "snapshots"

        # Path
        path_to_file = snap_dir_path / 'snapshot_3.txt'

        with open(path_to_file, 'r') as fp:
            data = fp.read()
            details = ast.literal_eval(data)
            self.colors_list = details['colors']
            self.main_array = details['knots']
            self.threads_colors_array = details['threads']
            self.rows_num = details['rows_num']
            self.threads_start_num = details['threads_start_num']
            self.left_add_drop_sit = details['left_add_drop_sit']

            self.canvas_lf.delete('all')
            self.color_picker_pad()
            self.draw_left_num_bar()
            self.draw_threads()
            self.draw_knots()
            self.put_buttons()

    def on_check_3(self):

        if self.checkCmd_3.get() == "0":
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='4', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=8)

        if self.checkCmd_3.get() == "1":

            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='4', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot_3()).grid(row=0, column=8)

            my_dict = {'colors': self.colors_list,
                       'knots': self.main_array,
                       'threads': self.threads_colors_array,
                       'rows_num': self.rows_num,
                       'threads_start_num': self.threads_start_num,
                       'left_add_drop_sit': self.left_add_drop_sit}

            # current directory
            current_directory = Path.cwd()
            # path to snapshots folder
            snap_dir_path = current_directory / "snapshots"

            # # # Create directory
            if not os.path.exists(snap_dir_path):
                try:
                    os.mkdir(snap_dir_path)
                except OSError as error:
                    print(error)

            # path to snapshot file
            path_to_file = snap_dir_path / "snapshot_4.txt"
            file = open(path_to_file, 'w')
            file.write(str(my_dict))
            file.close()

    def run_snapshot_3(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_dir_path = current_directory / "snapshots"

        # Path
        path_to_file = snap_dir_path / 'snapshot_4.txt'

        with open(path_to_file, 'r') as fp:
            data = fp.read()
            details = ast.literal_eval(data)
            self.colors_list = details['colors']
            self.main_array = details['knots']
            self.threads_colors_array = details['threads']
            self.rows_num = details['rows_num']
            self.threads_start_num = details['threads_start_num']
            self.left_add_drop_sit = details['left_add_drop_sit']

            self.canvas_lf.delete('all')
            self.color_picker_pad()
            self.draw_left_num_bar()
            self.draw_threads()
            self.draw_knots()
            self.put_buttons()

    # ADD/DROP ROWS NUMBERS
    def draw_left_num_bar(self):
        num_bar_height = self.rows.get() * 100

        self.canvas = tk.Canvas(self.canvas_lf, width=50, height=num_bar_height, bg=self.main_bg_color)
        self.canvas_lf.create_window(2, 2, anchor='nw',  window=self.canvas)

        checkbutton = tk.Checkbutton(self.canvas,
                                     onvalue=True,
                                     bg=self.main_bg_color,
                                     foreground='#9A9A92',
                                     activebackground=self.main_bg_color,
                                     background=self.main_bg_color,
                                     selectcolor=self.main_bg_color,
                                     command=lambda: self.drop_left_num_bar())
        checkbutton.select()
        self.canvas.create_window(30, 10, window=checkbutton)

        for i in range(self.rows.get()):
            label_row_padding = 30
            if i % 2 == 0:
                label_row = tk.Label(self.canvas,
                                     text=str(i + 1),
                                     font=("Arial", 7, 'bold'),
                                     bg=self.main_bg_color,
                                     )
                self.canvas.create_window(label_row_padding, (38 * i) + 88, anchor='se', window=label_row)
                label_row.config(fg='#6E6E68')

            if i % 2 != 0:
                label_row = tk.Label(self.canvas, text=str(i + 1), font=("Arial", 7, "bold"), bg=self.main_bg_color)
                self.canvas.create_window(label_row_padding, (38 * i) + 88, anchor='se', window=label_row)
                label_row.config(fg='#6E6E68')

    def drop_left_num_bar(self):
        if self.hidden:
            for item in self.canvas.winfo_children():
                if item.cget("fg") == '#6E6E68':
                    item.config(fg=self.main_bg_color)
            self.hidden = False

        else:
            for item in self.canvas.winfo_children():
                if item.cget("fg") == self.main_bg_color:
                    item.config(fg='#6E6E68')

            self.hidden = True

    # COLOR PICKER
    def color_picker_pad(self):
        for i in range(self.threads.get()):
            line_bg = self.canvas_lf.create_line((20 * i) + 70, 3, (20 * i) + 70, 21, fill='grey', width=14)
            line = self.canvas_lf.create_line((20 * i) + 70, 4, (20 * i) + 70, 20, fill=self.colors_list[i], width=10)
            self.canvas_lf.tag_bind(line, '<Button-1>', lambda event, i=i: self.color_picker(i))

    def color_picker(self,  i):

        new_colors = askcolor(title="Thread Color")
        ccc = new_colors[1]
        self.colors_list[i] = ccc

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    # DRAW THREADS CENTER
    def draw_center_of_threads(self):
        if self.threads.get() % 2 == 0:
            center = self.threads.get() // 2
            self.canvas_lf.create_line([(20 * center) + 60, 38, (20 * center) + 60, 42], fill='grey', width=2)

        if self.threads.get() % 2 != 0:
            center = self.threads.get() // 2
            self.canvas_lf.create_line([(20 * center) + 70, 38, (20 * center) + 70, 42], fill='grey', width=2)

    # MAIN KNOTS ARRAY
    def create_main_array(self):
        # clear main_array list and create new
        self.main_array = []
        for row in range(self.rows.get()):
            self.main_array.append([])
            if row % 2 == 0:
                for column in range(self.threads.get() // 2):
                    self.main_array[row].append(0)
            else:
                for column in range((self.threads.get() - 1) // 2):
                    self.main_array[row].append(0)

    # COLORS
    def colors(self):
        if self.threads_start_num % 2 == 0:
            for z in range(self.threads_start_num):
                half_colors_1 = list(reversed(sns.color_palette("husl", self.threads_start_num // 2).as_hex()))
                half_colors_2 = half_colors_1[::-1]
                self.colors_list = half_colors_1 + half_colors_2

        else:
            for z in range(self.threads_start_num // 2):
                half_colors_1 = list(reversed(sns.color_palette("husl", self.threads_start_num // 2 + 1).as_hex()))
                half_colors_2 = half_colors_1[::-1]
                half_colors_2.pop()
                self.colors_list = half_colors_1 + half_colors_2

    def threads_colors_array_handler(self):

        # Clear threads_colors_array if not empty
        self.threads_colors_array = []
        for row in range(self.rows.get()):
            self.threads_colors_array.append([])
            for column in range(self.threads.get()):
                self.threads_colors_array[row].append(column)

        # go through knots array and change self.threads_colors_array by knots
        for row in range(len(self.main_array)):
            for column in range(len(self.main_array[row])):

                # if not from left side not even number added

                if row % 2 == 0:

                    # only 2 knots change threads color list 1 and 3
                    if self.main_array[row][column] == 1 or self.main_array[row][column] == 3:

                        # Change all lower threads colors
                        for k in range(row + 1, len(self.main_array)):

                            self.threads_colors_array[k][column * 2] = self.threads_colors_array[row][(column * 2) + 1]
                            self.threads_colors_array[k][(column * 2) + 1] = self.threads_colors_array[row][(column * 2)]

                if row % 2 != 0:
                    if self.main_array[row][column] == 1 or self.main_array[row][column] == 3:

                        for k in range(row + 1, len(self.main_array)):
                            self.threads_colors_array[k][(column * 2) + 1] = self.threads_colors_array[row][(column * 2) + 2]
                            self.threads_colors_array[k][(column * 2) + 2] = self.threads_colors_array[row][(column * 2) + 1]

    # TOP BAR BUTTONS FUNCTIONS
    def selected_tool_bar_item(self, i):
        self.selected_toolbar_func_index = i
        self.execute_method()

    def execute_method(self):
        fnc = getattr(self, self.tool_bar_functions[int(self.selected_toolbar_func_index)])
        fnc()

    def add_two_thread_from_left(self):

        thn_after_click = self.threads.get() + 2
        self.threads.set(thn_after_click)

        # Insert new  colors to 0 color list
        add_thr_num = 2

        colors_append = list(reversed(sns.color_palette("husl", add_thr_num).as_hex()))
        for i in range(len(colors_append)):
            self.colors_list.insert(0, colors_append[i])

        # if threads_start_num even and number of added threads even:
        # add columns to every main_array row
        for row in range(len(self.main_array)):
            self.main_array[row].insert(0, 0)

        # make threads_start_num == new value
        self.threads_start_num = thn_after_click

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    def drop_two_thread_from_left(self):
        thn_after_click = self.threads.get() - 2
        self.threads.set(thn_after_click)

        self.colors_list = self.colors_list[2:]

        for i in range(len(self.main_array)):
            self.main_array[i].pop(0)

        # make threads_start_num == new value
        self.threads_start_num = thn_after_click
        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    def add_drop_thread_from_right(self):
        thn_after_click = self.threads.get()

        if thn_after_click > self.threads_start_num:
            add_thr_num = thn_after_click - self.threads_start_num

            colors_append = list(reversed(sns.color_palette("husl", add_thr_num).as_hex()))
            for i in range(len(colors_append)):
                self.colors_list.append(colors_append[i])

            #     8 + 2 or 9 + 2
            if add_thr_num % 2 == 0:
                for row in range(len(self.main_array)):
                    for column in range(add_thr_num // 2):
                        self.main_array[row].append(0)

            #    9 + 3 or 9 + 1
            if add_thr_num % 2 != 0 and self.threads_start_num % 2 != 0:
                for row in range(len(self.main_array)):
                    if row % 2 == 0:
                        for column in range(add_thr_num // 2 + 1):
                            self.main_array[row].append(0)

                    if row % 2 != 0:
                        for column in range(add_thr_num // 2):
                            self.main_array[row].append(0)

            # #    8 + 1 or 8 + 3
            if add_thr_num % 2 != 0 and self.threads_start_num % 2 == 0:
                for row in range(len(self.main_array)):
                    if row % 2 == 0:
                        for column in range(add_thr_num // 2):
                            self.main_array[row].append(0)

                    if row % 2 != 0:
                        for column in range(add_thr_num // 2 + 1):
                            self.main_array[row].append(0)
                self.threads_start_num = thn_after_click

        if thn_after_click < self.threads_start_num:
            drop_thr_num = self.threads_start_num - thn_after_click

            for i in range(drop_thr_num):
                self.colors_list.pop()

            #   9 - 2
            if drop_thr_num % 2 == 0:
                for row in range(len(self.main_array)):
                    for column in range(drop_thr_num // 2):
                        self.main_array[row].pop()

            #    9 - 3 or 9 - 1
            if drop_thr_num % 2 != 0 and self.threads_start_num % 2 != 0:
                for row in range(len(self.main_array)):
                    if row % 2 == 0:
                        for column in range(drop_thr_num // 2):
                            self.main_array[row].pop()

                    if row % 2 != 0:
                        for column in range(drop_thr_num // 2 + 1):
                            self.main_array[row].pop()

            #  10 - 1
            if drop_thr_num % 2 != 0 and self.threads_start_num % 2 == 0:
                for row in range(len(self.main_array)):
                    if row % 2 == 0:
                        for column in range(drop_thr_num // 2 + 1):
                            self.main_array[row].pop()

                    if row % 2 != 0:
                        for column in range(drop_thr_num // 2):
                            self.main_array[row].pop()

        self.threads_start_num = thn_after_click

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def add_drop_rows_bottom(self):

        # get value from spinbox
        rows_after_click = self.rows.get()


        # For adding
        if rows_after_click > self.rows_num:
            add_rows_num = rows_after_click - self.rows_num

            add_array = []
            if add_rows_num > 1:
                for row in range(add_rows_num):
                    add_array.append([])
                    if row % 2 == 0:
                        for column in range(self.threads.get() // 2):
                            add_array[row].append(0)
                    else:
                        for column in range((self.threads.get() - 1) // 2):
                            add_array[row].append(0)

                if self.rows_num % 2 == 0:
                    self.main_array = self.main_array + add_array
                if self.rows_num % 2 != 0:
                    self.main_array = self.main_array + add_array.reverse()

            if add_rows_num == 1:
                for row in range(2):
                    add_array.append([])
                    if row % 2 == 0:
                        for column in range(self.threads.get() // 2):
                            add_array[row].append(0)
                    else:
                        for column in range((self.threads.get() - 1) // 2):
                            add_array[row].append(0)

                if self.rows_num % 2 == 0:
                    self.main_array = self.main_array + [add_array[0]]
                if self.rows_num % 2 != 0:
                    self.main_array = self.main_array + [add_array[1]]

            print(add_array)
            print(self.main_array)



        # For rows dropping
        if rows_after_click < self.rows_num:
            drop_rows_num = self.rows_num - rows_after_click
            for i in range(drop_rows_num):
                self.main_array.pop()

        self.rows_num = rows_after_click

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    def add_rows_top(self):

        # Take rows value and add 2
        rows_value = self.rows.get()
        new_rows_value = rows_value + 2
        self.rows.set(new_rows_value)
        self.rows_num = new_rows_value

        # Create empty array
        new_array = []
        for row in range(2):
            new_array.append([])
            if row % 2 == 0:
                for column in range(self.threads.get() // 2):
                    new_array[row].append(0)
            else:
                for column in range((self.threads.get() - 1) // 2):
                    new_array[row].append(0)

        # Insert new array in start of old array
        self.main_array = new_array + self.main_array

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    def drop_rows_top(self):

        # Take rows value and add 2
        rows_value = self.rows.get()
        new_rows_value = rows_value - 2
        self.rows.set(new_rows_value)
        self.rows_num = new_rows_value

        self.main_array = self.main_array[2:]

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    # DRAWING
    def draw_threads(self):

        for i in range(self.rows.get()):
            for j in range(self.threads.get()):
                color_num = self.threads_colors_array[i][j]
                color = self.colors_list[color_num]

                self.canvas_lf.create_line((20 * j) + 70,
                                           (38 * i) + 60,
                                           (20 * j) + 70,
                                           (38 * i) + 98,
                                           fill=color, width=4, tags='line')

    def draw_knots(self):
        for i in range(len(self.main_array)):
            for j in range(len(self.main_array[i])):
                if self.main_array[i][j] == 1:
                    if i % 2 == 0:
                        left_thread = self.threads_colors_array[i][j * 2]
                        color_num = left_thread
                        color = self.colors_list[color_num]

                        right_thread = self.threads_colors_array[i][(j * 2) + 1]
                        color_1 = self.colors_list[right_thread]
                        knots.Knot1(color, color_1, i, j * 2, self.canvas_lf, self.main_bg_color)
                    else:
                        left_thread = self.threads_colors_array[i][(j * 2) + 1]
                        color_num = left_thread
                        color = self.colors_list[color_num]

                        right_thread = self.threads_colors_array[i][(j * 2) + 2]
                        color_1 = self.colors_list[right_thread]

                        knots.Knot1(color, color_1, i, (j * 2) + 1, self.canvas_lf, self.main_bg_color)

                if self.main_array[i][j] == 2:
                    if i % 2 == 0:
                        left_thread = self.threads_colors_array[i][j * 2]
                        color_num = left_thread
                        color = self.colors_list[color_num]
                        knots.Knot2(color, i, j * 2, self.canvas_lf, self.main_bg_color)
                    else:
                        left_thread = self.threads_colors_array[i][(j * 2) + 1]
                        color_num = left_thread
                        color = self.colors_list[color_num]
                        knots.Knot2(color, i, (j * 2) + 1, self.canvas_lf, self.main_bg_color)

                if self.main_array[i][j] == 3:
                    if i % 2 == 0:
                        right_thread = self.threads_colors_array[i][(j * 2) + 1]
                        color_num = right_thread
                        color = self.colors_list[color_num]

                        left_thread = self.threads_colors_array[i][(j * 2)]
                        color_1 = self.colors_list[left_thread]
                        knots.Knot3(color, color_1, i, j * 2, self.canvas_lf, self.main_bg_color)
                    else:
                        right_thread = self.threads_colors_array[i][(j * 2) + 2]
                        color_num = right_thread
                        color = self.colors_list[color_num]

                        left_thread = self.threads_colors_array[i][(j * 2) + 1]
                        color_1 = self.colors_list[left_thread]
                        knots.Knot3(color, color_1, i, (j * 2) + 1, self.canvas_lf, self.main_bg_color)

                if self.main_array[i][j] == 4:
                    if i % 2 == 0:
                        right_thread = self.threads_colors_array[i][(j * 2) + 1]
                        color_num = right_thread
                        color = self.colors_list[color_num]
                        knots.Knot4(color, i, j * 2, self.canvas_lf, self.main_bg_color)
                    else:
                        right_thread = self.threads_colors_array[i][(j * 2) + 2]
                        color_num = right_thread
                        color = self.colors_list[color_num]
                        knots.Knot4(color, i, (j * 2) + 1, self.canvas_lf, self.main_bg_color)

                if self.main_array[i][j] == 0:
                    if i % 2 == 0:
                        knots.Knot0(i, j * 2, self.canvas_lf)
                    else:
                        knots.Knot0(i, (j * 2) + 1, self.canvas_lf)

    # KNOTS BUTTONS
    def put_buttons(self):
        button_rect = []
        for row in range(self.rows.get()):
            button_rect.append([])
            if row % 2 == 0:
                for column in range(self.threads.get() // 2):
                    button_rect[row].append(0)
            else:
                for column in range((self.threads.get() - 1) // 2):
                    button_rect[row].append(0)

        for i in range(self.rows.get()):
            if i % 2 == 0:
                for j in range(self.threads.get() // 2):
                    button_rect[i][j] = self.canvas_lf.create_rectangle(((40 * j) + 68,
                                                                        (38 * i) + 60,
                                                                        (40 * j) + 92,
                                                                        (38 * i) + 98),
                                                                        fill='',
                                                                        outline="")
                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-1>', lambda event, i=i,
                                                                                      j=j: self.button_left_clicked(i, j))

                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-2>', lambda event, i=i,
                                                                                      j=j: self.button_middle_clicked(i, j))


                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-3>', lambda event, i=i,
                                                                                    j=j: self.button_right_clicked(i, j))



        for i in range(self.rows.get()):
            if i % 2 != 0:
                for j in range((self.threads.get() - 1) // 2):
                    button_rect[i][j] = self.canvas_lf.create_rectangle(((40 * j) + 88,
                                                                        (38 * i) + 60,
                                                                        (40 * j) + 112,
                                                                        (38 * i) + 98),
                                                                        fill='',
                                                                        outline="")
                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-1>', lambda event, i=i,
                                                                                       j=j: self.button_left_clicked(i, j))

                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-2>', lambda event, i=i,
                                                                                      j=j: self.button_middle_clicked(i, j))


                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-3>', lambda event, i=i,
                                                                                    j=j: self.button_right_clicked(i, j))

    def button_middle_clicked(self, i, j):
        self.main_array[i][j] = 0
        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    def button_left_clicked(self, i, j):

        if self.main_array[i][j] >= 2 or self.main_array[i][j] == 0:
            self.main_array[i][j] = 1
        else:
            self.main_array[i][j] += 1

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    def button_right_clicked(self, i, j):

        if self.main_array[i][j] <= 2 or self.main_array[i][j] >= 4:
            self.main_array[i][j] = 3
        else:
            self.main_array[i][j] += 1

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    # TOP MENU
    def create_menu(self):
        self.menubar = tk.Menu(self.root)
        menu_definitions = (
            'File- &New Pattern/ /self.new_pattern, Open Pattern/ /self.open_pattern, Save Pattern/ /self.save_pattern,\
            sep, Save As Picture/ /self.test_save,Save For Printer/ /self.save_as_vector, sep, Exit/ /self.exit_app',

            'View- &Hide Top/ /self.hide_top_bar, Show Top/ /self.show_top_bar,\
             Set Background/ /self.set_background_color ',

            'About- &How to .../ /self.hide_top_bar, Github/ /self.hide_top_bar')

        self.build_menu(menu_definitions)

    def set_background_color(self):
        choose_bg = askcolor(title="Thread Color")
        new_bg = choose_bg[1]
        self.main_bg_color = new_bg

        for widgets in self.root.winfo_children():
            widgets.destroy()

        self.main_window()
        self.on_check()
        self.on_check_1()
        self.on_check_2()
        self.on_check_3()

        self.create_main_array()
        self.colors()
        self.threads_colors_array_handler()
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()
        self.create_menu()

    def hide_top_bar(self):
        self.window.forget()

    def show_top_bar(self):
        self.window.forget()
        self.left_frame.forget()

        self.main_window()
        self.on_check()
        self.on_check_1()
        self.on_check_2()
        self.on_check_3()

        self.colors()
        self.threads_colors_array_handler()
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()
        self.create_menu()

    def save_image(self):
        save_image_test(self)


    # Ok
    def save_as_vector(self):
        x1, y1, x2, y2 = self.canvas_lf.bbox('all')
        w, h = x2 - x1, y2 - y1
        self.canvas_lf.postscript(file="Result.eps", x=x1, y=y1, width=w, height=h, pagewidth=w, pageheight=h)
        img = Image.open("Result.eps")

        file = asksaveasfile(mode='w', initialfile='my_bracelet.eps', defaultextension=".eps",
                             filetypes=(("EPS file", "*.eps"), ("All Files", "*.*")))

        # save image to the input file name
        if file:
            abs_path = os.path.abspath(file.name)
            img.save(abs_path)

    def save_pattern(self):
        my_dict = {'colors': self.colors_list,
                   'knots': self.main_array,
                   'threads': self.threads_colors_array,
                   'rows_num': self.rows_num,
                   'threads_start_num': self.threads_start_num,
                   'left_add_drop_sit': self.left_add_drop_sit,
                   }

        filename = asksaveasfile(initialfile='my_bracelet.knw', defaultextension=".knw",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if filename:
            abs_path = os.path.abspath(filename.name)
            file = open(abs_path, 'w')
            file.write(str(my_dict))
            file.close()

    def open_pattern(self):

        filename = askopenfilename(title='Open a file', initialdir='/', filetypes=[('text files', '*.knw'),
                                                                                   ('All files', '*.*')])
        if not filename:
            return

        if filename:
            abs_path = os.path.abspath(filename)
            with open(abs_path, 'r') as fp:
                data = fp.read()
                details = ast.literal_eval(data)
                self.colors_list = details['colors']
                self.main_array = details['knots']
                self.threads_colors_array = details['threads']
                self.rows_num = details['rows_num']
                self.threads_start_num = details['threads_start_num']
                self.left_add_drop_sit = details['left_add_drop_sit']

                self.canvas_lf.delete('all')
                self.color_picker_pad()
                self.draw_left_num_bar()
                self.draw_threads()
                self.draw_knots()
                self.put_buttons()

    def new_pattern(self):

        self.main_array = []
        self.create_main_array()

        self.threads_colors_array_handler()
        self.canvas_lf.delete('all')
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()
        self.draw_center_of_threads()

    # Ok
    def exit_app(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_dir_path = current_directory / "snapshots"

        # # # Create directory
        if os.path.exists(snap_dir_path):
            try:
                os.rmdir(snap_dir_path)
            except OSError as error:
                print(error)

        self.root.destroy()

    def test_save(self):

        top = self.top = tk.Toplevel(self.window, background=self.main_bg_color)
        self.top.geometry("800x750")

        self.myEntryBox_0 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_0.grid(row=0, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_1 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_1.grid(row=1, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_2 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_2.grid(row=2, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_3 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_3.grid(row=3, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_4 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_4.grid(row=4, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_5 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_5.grid(row=5, column=0, padx=32, pady=2, sticky='we', columnspan=9)

        self.myEntryBox_6 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_6.grid(row=6, column=0, padx=32, pady=2, sticky='we', columnspan=9)

        self.myEntryBox_7 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_7.grid(row=7, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_8 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_8.grid(row=8, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_9 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_9.grid(row=9, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_10 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_10.grid(row=10, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_11 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_11.grid(row=11, column=0, padx=32, pady=2, sticky='we', columnspan=8)

        self.myEntryBox_12 = tk.Entry(top, width=34, font=("Arial", 17, 'bold'), foreground='#6E6E68')
        self.myEntryBox_12.grid(row=12, column=0, padx=32, pady=2, sticky='we', columnspan=9)

        self.mySubmitButton = tk.Button(top, text='Add Info and Save', command=self.parent_func, foreground='#2C2C29',
                                        font=("Arial", 10, 'bold'))
        self.mySubmitButton.grid(row=13, column=1, sticky='w', pady=40, padx=60, ipady=20)

        self.mySubmitButton1 = tk.Button(top, text='Pass and Save', command=self.parent_func, foreground='#2C2C29',
                                         font=("Arial", 10, 'bold'))
        self.mySubmitButton1.grid(row=13, column=2, sticky='w', pady=40, padx=60, ipady=20)

    def parent_func(self):
        self.save_image()
        self.top.destroy()

    def test_function(self):
        colors_bg_test = list(reversed(sns.color_palette("husl", self.threads_start_num).as_hex()))
        self.main_bg_color = colors_bg_test[0]


def main():
    root = tk.Tk()
    root.title('KnotWizard')

    data_folder = Path('icons')
    logo_file = data_folder / 'new_logo.ico'
    root.iconbitmap(logo_file)

    # root.state('zoomed')
    root.geometry('900x700')

    MainProgram(root)

    def exit_handler():
        # On app close we need erase/drop folder which contains snapshots files
        # folder for snapshots == snapshots
        # get path to folder where program sits

        # create path
        snapshots_folder = Path('snapshots')
        # try to remove folder
        try:
            shutil.rmtree(snapshots_folder)
        except OSError as e:
            pass
    # register command at exit
    atexit.register(exit_handler)

    root.mainloop()


if __name__ == "__main__":
    main()
