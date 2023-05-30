# import necessary libraries
import copy
# # # Seaborn python library take too much place and installs Matplot, Pandas and other libraries.
# Too much size when .exe file created.
# decided to use ready list with 100 different colors from "reversed(sns.color_palette("husl", 100).as_hex())"
from my_colors_list import my_colors
# for get random color from colors list
import random

# main engine
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfile, askopenfilename

# my classes for knots drawing
import knots

# my script for img PNG, GIF,
from save_pil_image import *

# for more simple file save, open AND no meter if it Mac, Linux or Windows
from pathlib import Path

# # # after app closes we need delete folder containing snapshots files
import atexit
# for recursive folder deleting
import shutil

# # # for main menu : framework script from "Tkinter-GUI-Application-Development-Blueprints-Second-Edition/Chapter 06/"
# 'https://github.com/PacktPublishing/Tkinter-GUI-Application-Development-Blueprints-Second-Edition/'
# special THANKS to Bhaskar Chaudhary for time saving and understanding how Tkinter works.
import framework

# for image creations from tk.Canvas widget
from PIL import Image

#  save / read python dictionary from file correctly
import ast


# for basis of app i take chapter 06 from "Tkinter-GUI-Application-Development-Blueprints-Second-Edition" book
# because of that MainProgram class is a child class of 'framework' script
class MainProgram(framework.Framework):
    # tuple of "Top bar" functions. When user clicks on button in "Top bar" app get number of button and run func with
    # position number from tuple
    tool_bar_functions = ("add_two_thread_from_left",
                          "drop_two_thread_from_left",
                          "add_rows_top",
                          "drop_rows_top",
                          "two_colors_pattern",
                          "mirror_pattern_array")

    # For app to start we need threads and rows num to start knots array creation
    threads_start_num = 18
    rows_num = 30

    # list of current app colors
    colors_list = []

    # list of current threads colors in every row and column
    threads_colors_array = []

    # for correctly create pattern image with information on it
    line_counter = 0

    # To show/hide (rows number column) boolean variable needed. As tk.Checkbox used.
    # func == self.draw_left_num_bar()  for: first time drawing and redrawing
    # func == self.hide_left_num_bar()  for: hide
    hidden = True

    # # #  List/array to hold knots numbers. Possibilities are:
    #   0 - not knitted                  ( | | )
    #   1 - left thread to right         (  \  )
    #   2 - left to left                 (  >  )
    #   3 - right thread to left         (  /  )
    #   4 - right to right               (  <  )
    #
    #   func ==  self.create_main_array()   for: create array with all zeroes,
    #                                            array length = rows_num,
    #                                            array columns number depends on threads number.
    #
    #                                            if it threads number even (16, 20) :
    #                                               columns number in even row (0,2,4 ... +2) == threads number // 2
    #
    #                                               in not even (1,3,5 ... + 2) == (threads number - 1) // 2
    #
    #                                               0   0 0 0 0 0 0
    #                                               1    0 0 0 0 0
    #                                               2   0 0 0 0 0 0
    #                                               3    0 0 0 0 0
    #                                               4   0 0 0 0 0 0
    #
    #
    #                                            if threads number not even (19, 23 ....):
    #                                               columns number in every row == (threads number - 1) // 2
    #                                                                               (19 - 1) // 2 == 9
    #
    #                                               0   0 0 0 0 0
    #                                               1    0 0 0 0 0
    #                                               2   0 0 0 0 0
    #                                               3    0 0 0 0 0
    #                                               4   0 0 0 0 0
    #
    #

    # # #  Changes by user click on knot button area.

    #   func == self.button_left_clicked()
    #    Left mouse button click 1 (\)
    #    Left mouse button click 2 (>)

    #   func == self.button_right_clicked()
    #    Right mouse button click 1 (/)
    #    Right mouse button click 2 (<)

    #  func == self.button_right_clicked()
    #   Middle mouse button click  (||)
    main_array = []

    # user may change background color but app need some color to start
    main_bg_color = '#dddcd1'

    def __init__(self, root):
        # Threads and Rows integer variables
        self.threads = tk.IntVar()
        self.rows = tk.IntVar()

        # this variable depends on monitor width (int)
        self.max_threads = tk.IntVar()

        # snapshots checkboxes boolean variables
        self.checkCmd = tk.BooleanVar()
        self.checkCmd_1 = tk.BooleanVar()
        self.checkCmd_2 = tk.BooleanVar()
        self.checkCmd_3 = tk.BooleanVar()

        # description line 44
        self.selected_toolbar_func_index = tk.IntVar()

        self.menubar = tk.Menu()
        self.canvas = tk.Canvas()

        self.scrollbar = tk.Scrollbar
        self.window = tk.Frame
        self.top_frame = tk.Frame
        self.snp_frame = tk.Frame
        self.left_frame = tk.Frame
        self.canvas_lf = tk.Canvas
        self.top = tk.Toplevel
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

    # FRAMES AND PACK
    def main_window(self):
        # Save monitor dimensions (width and height) to variables
        self.monitor_width = self.root.winfo_screenwidth()
        self.monitor_height = self.root.winfo_screenheight()

        # Create main frame
        self.window = tk.Frame(self.root,
                               width=self.monitor_width * 0.75,
                               height=self.monitor_height,
                               bg=self.main_bg_color)

        # create top frame for buttons
        self.top_frame = tk.Frame(self.window, bg=self.main_bg_color)

        # pass to icons images
        icon_path = Path.cwd() / 'icons'
        # Create tuple with icons images names
        icons = ('2plus', '2drop', 'add_rows', 'drop_rows', '2colors', 'mirror_pattern')

        # put buttons on top frame and take images for buttons from '/icons' folder
        for i, icon in enumerate(icons):
            if i == 0:
                tool_bar_icon = tk.PhotoImage(file=icon_path / '{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon,
                                     command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=6)

            if i == 1:
                tool_bar_icon = tk.PhotoImage(file=icon_path / '{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon,
                                     command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=6)

                # max threads number devoted by monitor width
                self.max_threads = ((self.monitor_width - 140) // 20)

                # set variable threads to "threads_start_num" (if user run app first time, app needs values)
                self.threads.set(self.threads_start_num)

                thread_spinbox_right = tk.Spinbox(self.top_frame,
                                                  from_=6,
                                                  to=self.max_threads,
                                                  width=3,
                                                  textvariable=self.threads,
                                                  font=("Arial", 26, 'bold'),
                                                  command=self.add_drop_thread_from_right,
                                                  foreground=self.main_bg_color)

                # Put thread_spinbox on top_frame
                thread_spinbox_right.pack(side='left')
                # if user put number and hit enter in spinbox window run "self.add_drop_thread_from_right" func
                thread_spinbox_right.bind("<Return>", (lambda event: self.add_drop_thread_from_right()))

                # max threads label
                tk.Label(self.top_frame, bg=self.main_bg_color, foreground='#42423E', font=("Arial", 7),
                         text='MAX {}'.format(self.max_threads - 1)).pack(side='left', anchor='nw')

                tk.Label(self.top_frame, bg=self.main_bg_color, width=3).pack(side='left', anchor='nw')

            if i == 2:
                tool_bar_icon = tk.PhotoImage(file=icon_path / '{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon,
                                     command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=6)

            if i == 3:
                tool_bar_icon = tk.PhotoImage(file=icon_path / '{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon,
                                     command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=6)

                # # set variable rows to "trows_num" (if user run app first time, app needs values)
                self.rows.set(self.rows_num)
                # create spinbox
                row_widget = tk.Spinbox(self.top_frame,
                                        from_=1, to=200, width=3,
                                        textvariable=self.rows,
                                        font=("Arial", 26, 'bold'),
                                        foreground=self.main_bg_color,
                                        command=self.add_drop_rows_bottom)
                row_widget.pack(side='left')
                # if user change rows number in spinbox window and hit <ENTER>, run self.add_drop_rows_bottom func
                row_widget.bind("<Return>", lambda event: self.add_drop_rows_bottom())

            if i == 4:
                tool_bar_icon = tk.PhotoImage(file=icon_path / '{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon,
                                     command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=60)

            if i == 5:
                tool_bar_icon = tk.PhotoImage(file=icon_path / '{}.gif'.format(icon))
                tool_bar = tk.Button(self.top_frame, image=tool_bar_icon,
                                     command=lambda i=i: self.selected_tool_bar_item(i))
                tool_bar.image = tool_bar_icon
                tool_bar.pack(side='left', padx=20)


        # snapshots area
        self.snp_frame = tk.Frame(self.top_frame, bg=self.main_bg_color)
        tk.Checkbutton(self.snp_frame,
                       variable=self.checkCmd,
                       onvalue=None,
                       indicatoron=True,
                       activebackground='black',
                       background=self.main_bg_color,
                       selectcolor="white",
                       width=1,
                       foreground="black",
                       command=lambda: self.on_check()).grid(row=0, sticky='n')

        tk.Checkbutton(self.snp_frame,
                       variable=self.checkCmd_1,
                       onvalue=None,
                       indicatoron=True,
                       activebackground='black',
                       background=self.main_bg_color,
                       selectcolor="white",
                       width=1,
                       foreground="black",
                       command=lambda: self.on_check_1()).grid(row=0, column=3, sticky='n')

        tk.Checkbutton(self.snp_frame,
                       variable=self.checkCmd_2,
                       onvalue=None,
                       indicatoron=True,
                       activebackground='black',
                       background=self.main_bg_color,
                       selectcolor="white",
                       width=1,
                       foreground="black",
                       command=lambda: self.on_check_2()).grid(row=0, column=5, sticky='n')

        tk.Checkbutton(self.snp_frame,
                       variable=self.checkCmd_3,
                       onvalue=None,
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
                                   width=self.monitor_width,
                                   # for scrolling to be visible
                                   height=self.monitor_height,
                                   bg=self.main_bg_color)

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)




    # SNAPSHOTS AREA logic
    #
    # SAVE
    # 1. user click check box
    # 2. app create dictionary with values of: (self.colors_list,
    #                                           self.threads.get(),
    #                                           self.rows.get(),
    #                                           self.main_array,
    #                                           self.threads_colors_array,
    #                                           self.hidden)
    # 3. create folder "snapshots" in app working directory  if not exists      snapshots/
    # 4. write dictionary to file snapshots_(1-4).txt                           snapshots/snapshot_(1-4).txt

    # OPEN
    # 1. read file
    # 2. rewrite variables
    # 3. delete canvas_lf all elements
    # 4. draw canvas_lf with new variables

    def on_check(self):
        if self.checkCmd.get() == 0:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='1', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=1)
        if self.checkCmd.get() == 1:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='1', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot()).grid(row=0, column=1)

            # create dictionary
            my_dict = {'threads_colors': self.colors_list,
                       'threads_num': self.threads.get(),
                       'rows_num': self.rows.get(),
                       'knots_array': self.main_array,
                       'threads_colors_array': self.threads_colors_array,
                       'rows_number_hidden': self.hidden}

            # current directory
            current_directory = Path.cwd()
            # path to snapshots folder
            snap_dir_path = current_directory / "snapshots"

            # path to snapshot file
            path_to_file = snap_dir_path / "snapshot_0.txt"

            # create directory if not exists
            snap_dir_path.mkdir(exist_ok=True)
            # write to file
            path_to_file.write_text(str(my_dict))

    def run_snapshot(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_file_path = current_directory / "snapshots" / 'snapshot_0.txt'
        # read file
        text = snap_file_path.read_text()
        # put data from file to list
        details = ast.literal_eval(text)

        # # rewrite variables
        # # threads colors array
        self.colors_list = details['threads_colors']

        # number of threads
        # change number in Spinbox
        self.threads.set(details['threads_num'])

        # change "threads_start_num" variable
        self.threads_start_num = details['threads_num']
        #
        # number of rows
        # change "rows_num" variable
        # change number in Spinbox

        self.rows.set(details['rows_num'])
        self.rows_num = details['rows_num']

        # # change knots array to new array
        self.main_array = details['knots_array']

        # change threads colors array
        self.threads_colors_array = details['threads_colors_array']

        # show/hide rows numbers bar
        self.hidden = details['rows_number_hidden']

        # for scrolling work correctly app needs to redraw
        # destroy current left frame
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def on_check_1(self):
        if self.checkCmd_1.get() == 0:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='2', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=4)
        if self.checkCmd_1.get() == 1:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='2', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot_1()).grid(row=0, column=4)

            # create dictionary
            my_dict = {'threads_colors': self.colors_list,
                       'threads_num': self.threads.get(),
                       'rows_num': self.rows.get(),
                       'knots_array': self.main_array,
                       'threads_colors_array': self.threads_colors_array,
                       'rows_number_hidden': self.hidden}

            # current directory
            current_directory = Path.cwd()
            # path to snapshots folder
            snap_dir_path = current_directory / "snapshots"

            # path to snapshot file
            path_to_file = snap_dir_path / "snapshot_1.txt"

            # create directory if not exists
            snap_dir_path.mkdir(exist_ok=True)
            # write to file
            path_to_file.write_text(str(my_dict))

    def run_snapshot_1(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_file_path = current_directory / "snapshots" / 'snapshot_1.txt'
        # read file
        text = snap_file_path.read_text()
        # put data from file to list
        details = ast.literal_eval(text)

        # # rewrite variables
        # # threads colors array
        self.colors_list = details['threads_colors']

        # number of threads
        # change number in Spinbox
        self.threads.set(details['threads_num'])

        # change "threads_start_num" variable
        self.threads_start_num = details['threads_num']
        #
        # number of rows
        # change "rows_num" variable
        # change number in Spinbox

        self.rows.set(details['rows_num'])
        self.rows_num = details['rows_num']

        # # change knots array to new array
        self.main_array = details['knots_array']

        # change threads colors array
        self.threads_colors_array = details['threads_colors_array']

        # show/hide rows numbers bar
        self.hidden = details['rows_number_hidden']

        # for scrolling work correctly app needs to redraw
        # destroy current left frame
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def on_check_2(self):
        if self.checkCmd.get() == 0:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='3', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=6)
        if self.checkCmd.get() == 1:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='3', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot_2()).grid(row=0, column=6)

            # create dictionary
            my_dict = {'threads_colors': self.colors_list,
                       'threads_num': self.threads.get(),
                       'rows_num': self.rows.get(),
                       'knots_array': self.main_array,
                       'threads_colors_array': self.threads_colors_array,
                       'rows_number_hidden': self.hidden}

            # current directory
            current_directory = Path.cwd()
            # path to snapshots folder
            snap_dir_path = current_directory / "snapshots"

            # path to snapshot file
            path_to_file = snap_dir_path / "snapshot_2.txt"

            # create directory if not exists
            snap_dir_path.mkdir(exist_ok=True)
            # write to file
            path_to_file.write_text(str(my_dict))

    def run_snapshot_2(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_file_path = current_directory / "snapshots" / 'snapshot_2.txt'
        # read file
        text = snap_file_path.read_text()
        # put data from file to list
        details = ast.literal_eval(text)

        # # rewrite variables
        # # threads colors array
        self.colors_list = details['threads_colors']

        # number of threads
        # change number in Spinbox
        self.threads.set(details['threads_num'])

        # change "threads_start_num" variable
        self.threads_start_num = details['threads_num']
        #
        # number of rows
        # change "rows_num" variable
        # change number in Spinbox

        self.rows.set(details['rows_num'])
        self.rows_num = details['rows_num']

        # # change knots array to new array
        self.main_array = details['knots_array']

        # change threads colors array
        self.threads_colors_array = details['threads_colors_array']

        # show/hide rows numbers bar
        self.hidden = details['rows_number_hidden']

        # for scrolling work correctly app needs to redraw
        # destroy current left frame
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def on_check_3(self):
        if self.checkCmd.get() == 0:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='4', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=8)
        if self.checkCmd.get() == 1:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='4', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot_3()).grid(row=0, column=8)

            # create dictionary
            my_dict = {'threads_colors': self.colors_list,
                       'threads_num': self.threads.get(),
                       'rows_num': self.rows.get(),
                       'knots_array': self.main_array,
                       'threads_colors_array': self.threads_colors_array,
                       'rows_number_hidden': self.hidden}

            # current directory
            current_directory = Path.cwd()
            # path to snapshots folder
            snap_dir_path = current_directory / "snapshots"

            # path to snapshot file
            path_to_file = snap_dir_path / "snapshot_3.txt"

            # create directory if not exists
            snap_dir_path.mkdir(exist_ok=True)
            # write to file
            path_to_file.write_text(str(my_dict))

    def run_snapshot_3(self):
        # current directory
        current_directory = Path.cwd()
        # path to snapshots folder
        snap_file_path = current_directory / "snapshots" / 'snapshot_3.txt'
        # read file
        text = snap_file_path.read_text()
        # put data from file to list
        details = ast.literal_eval(text)

        # # rewrite variables
        # # threads colors array
        self.colors_list = details['threads_colors']

        # number of threads
        # change number in Spinbox
        self.threads.set(details['threads_num'])

        # change "threads_start_num" variable
        self.threads_start_num = details['threads_num']
        #
        # number of rows
        # change "rows_num" variable
        # change number in Spinbox

        self.rows.set(details['rows_num'])
        self.rows_num = details['rows_num']

        # # change knots array to new array
        self.main_array = details['knots_array']

        # change threads colors array
        self.threads_colors_array = details['threads_colors_array']

        # show/hide rows numbers bar
        self.hidden = details['rows_number_hidden']

        # for scrolling work correctly app needs to redraw
        # destroy current left frame
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    # SHOW/HIDE ROWS NUMBERS
    def draw_left_num_bar(self):
        # the same height as 'self.canvas_lf' scroll-region height
        num_bar_height = self.rows.get() * 50

        # create window for rows numbers (parent canvas_lf)
        self.canvas = tk.Canvas(self.canvas_lf, width=50, height=num_bar_height, bg=self.main_bg_color)
        self.canvas_lf.create_window(2, 2, anchor='nw',  window=self.canvas)

        # put check button
        checkbutton = tk.Checkbutton(self.canvas,
                                     onvalue=self.hidden,
                                     bg=self.main_bg_color,
                                     foreground='#9A9A92',
                                     activebackground=self.main_bg_color,
                                     selectcolor=self.main_bg_color,
                                     command=lambda: self.hide_left_num_bar())
        # create window
        self.canvas.create_window(30, 10, window=checkbutton)

        # if hidden is 'True'
        if self.hidden:
            checkbutton.select()
            for i in range(self.rows.get()):
                label_row_padding = 30
                if i % 2 == 0:
                    label_row = tk.Label(self.canvas,
                                         text=str(i + 1),
                                         font=("Arial", 8),
                                         bg=self.main_bg_color)
                    self.canvas.create_window(label_row_padding, (38 * i) + 88, anchor='se', window=label_row)
                    label_row.config(fg='#6E6E68')

                if i % 2 != 0:
                    label_row = tk.Label(self.canvas, text=str(i + 1), font=("Arial", 8), bg=self.main_bg_color)
                    self.canvas.create_window(label_row_padding, (38 * i) + 88, anchor='se', window=label_row)
                    label_row.config(fg='#6E6E68')

    def hide_left_num_bar(self):
        # destroy
        if self.hidden:
            for item in self.canvas.winfo_children():
                if item.cget("fg") == '#6E6E68':
                    item.destroy()
            self.hidden = False

        # redraw
        else:
            for i in range(self.rows.get()):
                label_row_padding = 30
                if i % 2 == 0:
                    label_row = tk.Label(self.canvas,
                                         text=str(i + 1),
                                         font=("Arial", 7, 'bold'),
                                         bg=self.main_bg_color)
                    self.canvas.create_window(label_row_padding, (38 * i) + 88, anchor='se', window=label_row)
                    label_row.config(fg='#6E6E68')

                if i % 2 != 0:
                    label_row = tk.Label(self.canvas, text=str(i + 1), font=("Arial", 7, "bold"), bg=self.main_bg_color)
                    self.canvas.create_window(label_row_padding, (38 * i) + 88, anchor='se', window=label_row)
                    label_row.config(fg='#6E6E68')

            self.hidden = True



    # COLOR PICKER
    def color_picker_pad(self):
        for i in range(self.threads.get()):
            line_bg = self.canvas_lf.create_line((16 * i) + 70, 3, (16 * i) + 70, 21,
                                                 fill='grey', width=14, tags='cvch')
            line = self.canvas_lf.create_line((16 * i) + 70, 4, (16 * i) + 70, 20,
                                              fill=self.colors_list[i], width=10, tags='cvch')
            self.canvas_lf.tag_bind(line, '<Button-1>', lambda event, i=i: self.color_picker(i))

    def color_picker(self,  i):

        new_colors = askcolor(title="Thread Color")
        ccc = new_colors[1]

        if ccc:
            self.colors_list[i] = ccc

            self.threads_colors_array_handler()
            self.canvas_lf.delete('all')
            self.color_picker_pad()
            self.draw_left_num_bar()
            self.draw_threads()
            self.draw_knots()
            self.put_buttons()

    # DRAW THREADS CENTER
    # little black line between color picker and threads, depend on threads number
    def draw_center_of_threads(self):
        if self.threads.get() % 2 == 0:
            center = self.threads.get() // 2
            self.canvas_lf.create_line([(16 * center) + 61, 38, (16 * center) + 61, 48],
                                       fill='grey', width=2, tags='cvch')
            self.canvas_lf.create_line([(16 * center) + 62, 38, (16 * center) + 62, 48],
                                       fill='grey', width=2, tags='cvch')

        if self.threads.get() % 2 != 0:
            center = self.threads.get() // 2
            self.canvas_lf.create_line([(16 * center) + 70, 38, (16 * center) + 70, 48],
                                       fill='grey', width=3, tags='cvch')

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
        # take colors for threads from my_colors list
        # for drawing threads symmetrically i take only half of threads number, put half random colors to
        # self.colors_list and other half  add to self.colors_list by reverse
        #  1 2 3 4 5  5 4 3 2 1

        if self.threads_start_num % 2 == 0:
            half_colors_1 = []
            for z in range(self.threads_start_num // 2):
                random_number = random.randint(0, 99)
                half_colors_1.append(my_colors[random_number])

            half_colors_2 = half_colors_1[::-1]
            self.colors_list = half_colors_1 + half_colors_2


    # change color of each thread in every row and column depend on main knots array
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


    # TOP BAR BUTTONS COMMANDS HANDLER
    def selected_tool_bar_item(self, i):
        self.selected_toolbar_func_index = i
        self.execute_method()

    def execute_method(self):
        fnc = getattr(self, self.tool_bar_functions[self.selected_toolbar_func_index])
        fnc()


    # ADD/DROP THREADS FROM LEFT AND RIGHT
    def add_two_thread_from_left(self):
        thn_after_click = self.threads.get() + 2
        self.threads.set(thn_after_click)

        colors_append = []
        for i in range(2):
            rand = random.randint(0, 99)
            colors_append.append(my_colors[rand])

        for i in range(len(colors_append)):
            self.colors_list.insert(0, colors_append[i])

        # if threads_start_num even and number of added threads even:
        # add columns to every main_array row
        for row in range(len(self.main_array)):
            self.main_array[row].insert(0, 0)

        # make threads_start_num == new value
        self.threads_start_num = thn_after_click

        self.threads_colors_array_handler()
        self.canvas_lf.delete('cvch')
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def drop_two_thread_from_left(self):
        thn_after_click = self.threads.get() - 2
        self.threads.set(thn_after_click)

        self.colors_list = self.colors_list[2:]

        for i in range(len(self.main_array)):
            self.main_array[i].pop(0)

        # make threads_start_num == new value
        self.threads_start_num = thn_after_click
        self.threads_colors_array_handler()
        self.canvas_lf.delete('cvch')
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def add_drop_thread_from_right(self):
        if self.threads.get() >= self.max_threads:
            return

        thn_after_click = self.threads.get()

        if thn_after_click > self.threads_start_num:
            add_thr_num = thn_after_click - self.threads_start_num

            colors_append = []
            for i in range(add_thr_num):
                rand = random.randint(0, 99)
                colors_append.append(my_colors[rand])

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
        self.canvas_lf.delete('cvch')
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()


    # ADD/DROP ROWS FROM TOP AND BOTTOM
    def add_rows_top(self):
        # Take rows value and add 2
        rows_value = self.rows.get()
        new_rows_value = rows_value + 2

        # set value in spinbox to new value
        self.rows.set(new_rows_value)
        # change rows_num variable to new value
        self.rows_num = new_rows_value

        # Create empty array, rows 2 and columns first row == threads number // 2,
        #                                        second row == (threads number - 1) // 2; (to catch not even number of
        #                                                                                                      threads)
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

        # change threads color in every row and column depend on new values
        self.threads_colors_array_handler()

        # for scrolling work correctly app needs to redraw
        # destroy current left frame
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()

        # Create left frame for pattern editor 50% from monitor width and height with scrolling depend on rows number
        # self.left_frame = tk.Frame(self.root,
        #                            width=self.monitor_width,
        #                            # for scrolling to be visible
        #                            height=self.monitor_height,
        #                            bg=self.main_bg_color)

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def drop_rows_top(self):
        if self.rows.get() < 11:
            return

        # get value from spinbox window
        rows_value = self.rows.get()
        new_rows_value = rows_value - 2

        # set (value in spinbox) - 2
        self.rows.set(new_rows_value)
        # set new value to variable "rows_num"
        self.rows_num = new_rows_value

        # get rid of 2 last rows
        self.main_array = self.main_array[2:]

        # change threads colors in every row and column
        self.threads_colors_array_handler()

        # for scrolling work correctly app needs to redraw
        # destroy current left_frame
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()

        # Create left frame for pattern editor 50% from monitor width and height with scrolling depend on rows number
        # self.left_frame = tk.Frame(self.root,
        #                            width=self.monitor_width,
        #                            # for scrolling to be visible
        #                            height=self.monitor_height,
        #                            bg=self.main_bg_color)

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def add_drop_rows_bottom(self):
        # get value from spinbox
        rows_after_click = self.rows.get()
        if rows_after_click < 1:
            return

        # For adding
        if rows_after_click > self.rows_num:

            # how much rows needs to add?
            add_rows_num = rows_after_click - self.rows_num

            # create empty array
            add_array = []

            # if user set in spinbox window number that more than 1
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
                self.rows_num = rows_after_click

            # if only 1 row was added
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
                self.rows_num = rows_after_click

        # For rows dropping
        if rows_after_click < self.rows_num:
            # how much to drop?
            drop_rows_num = self.rows_num - rows_after_click

            # create loop and drop
            for i in range(drop_rows_num):
                self.main_array.pop()
            self.rows_num = rows_after_click

        # for scrolling work correctly app needs to redraw
        # destroy current left frame
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()


        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        # change threads color in every row and column depend on new values
        self.threads_colors_array_handler()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()


    # CHANGE ALL COLORS -> TWO COLORS and ALL EVEN ROWS KNOTS VALUE == 4 and NOT EVEN == 2
    def two_colors_pattern(self):

        # empty main array
        self.main_array = []
        # create new main array
        for row in range(self.rows.get()):
            self.main_array.append([])
            if row % 2 == 0:
                for column in range(self.threads.get() // 2):
                    self.main_array[row].append(4)
            else:
                for column in range((self.threads.get() - 1) // 2):
                    self.main_array[row].append(2)

        # take random color from my_colors array
        half_colors_1 = my_colors[random.randint(0, 99)]
        half_colors_2 = my_colors[random.randint(0, 99)]

        # create new array which holds new values
        main_half_colors_list = []
        # put values
        for z in range(self.threads_start_num):
            if z % 2 == 0:
                main_half_colors_list.append(half_colors_1)
            if z % 2 != 0:
                main_half_colors_list.append(half_colors_2)

        # empty colors list
        self.colors_list = []

        # set to new values
        self.colors_list = main_half_colors_list

        # redraw canvas
        self.canvas_lf.delete('cvch')
        self.threads_colors_array_handler()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    # DUPLICATE KNOTS
    def mirror_pattern_array(self):

        def check(num):
            if num == 1:
                return 3
            elif num == 3:
                return 1
            else:
                return num

        new_array = [[check(j) for j in i] for i in copy.deepcopy(self.main_array)]
        print(new_array)

        new_array.pop()

        def check_1(num):
            if num == 1:
                return 2
            elif num == 3:
                return 4
            else:
                return num

        self.main_array[-1] = [check_1(j) for j in self.main_array[-1]]

        self.main_array = self.main_array + new_array[::-1]

        self.rows.set(len(self.main_array))
        self.rows_num = len(self.main_array)

        # change threads color in every row and column depend on new values
        self.threads_colors_array_handler()

        # for scrolling work correctly app needs to redraw
        # destroy current left frame
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()

        # Create left frame for pattern editor 50% from monitor width and height with scrolling depend on rows number
        # self.left_frame = tk.Frame(self.root,
        #                            width=self.monitor_width,
        #                            # for scrolling to be visible
        #                            height=self.monitor_height,
        #                            bg=self.main_bg_color)

        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

        self.left_frame.pack(fill=tk.X, padx=5, pady=5)
        self.draw_left_num_bar()
        self.color_picker_pad()
        self.draw_center_of_threads()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()



    # DRAWING
    def draw_threads(self):
        for i in range(self.rows.get()):
            for j in range(self.threads.get()):
                color_num = self.threads_colors_array[i][j]
                color = self.colors_list[color_num]

                self.canvas_lf.create_line((16 * j) + 70,
                                           (38 * i) + 60,
                                           (16 * j) + 70,
                                           (38 * i) + 98,
                                           fill=color, width=4, tags='cvch')

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
                    button_rect[i][j] = self.canvas_lf.create_rectangle(((32 * j) + 67,
                                                                        (38 * i) + 60,
                                                                        (32 * j) + 89,
                                                                        (38 * i) + 98),
                                                                        fill='',
                                                                        outline="", tags='cvch')
                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-1>',
                                        lambda event, i=i, j=j: self.button_left_clicked(i, j))

                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-2>',
                                        lambda event, i=i, j=j: self.button_middle_clicked(i, j))

                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-3>',
                                        lambda event, i=i, j=j: self.button_right_clicked(i, j))

        for i in range(self.rows.get()):
            if i % 2 != 0:
                for j in range((self.threads.get() - 1) // 2):
                    button_rect[i][j] = self.canvas_lf.create_rectangle(((32 * j) + 84,
                                                                        (38 * i) + 60,
                                                                        (32 * j) + 106,
                                                                        (38 * i) + 98),
                                                                        fill='',
                                                                        outline="", tags='cvch')
                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-1>',
                                        lambda event, i=i, j=j: self.button_left_clicked(i, j))

                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-2>',
                                        lambda event, i=i, j=j: self.button_middle_clicked(i, j))

                    self.canvas_lf.tag_bind(button_rect[i][j], '<Button-3>',
                                        lambda event, i=i, j=j: self.button_right_clicked(i, j))

    def button_middle_clicked(self, i, j):
        self.canvas_lf.after(200, self.canvas_lf.delete('cvch'))
        self.main_array[i][j] = 0

        self.draw_center_of_threads()
        self.color_picker_pad()
        self.threads_colors_array_handler()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def button_left_clicked(self, i, j):
        self.canvas_lf.after(200, self.canvas_lf.delete('cvch'))
        if self.main_array[i][j] >= 2 or self.main_array[i][j] == 0:
            self.main_array[i][j] = 1
        else:
            self.main_array[i][j] += 1

        self.draw_center_of_threads()
        self.color_picker_pad()
        self.threads_colors_array_handler()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()

    def button_right_clicked(self, i, j):
        self.canvas_lf.after(200, self.canvas_lf.delete('cvch'))
        if self.main_array[i][j] <= 2 or self.main_array[i][j] >= 4:
            self.main_array[i][j] = 3
        else:
            self.main_array[i][j] += 1

        self.draw_center_of_threads()
        self.color_picker_pad()
        self.threads_colors_array_handler()
        self.draw_threads()
        self.draw_knots()
        self.put_buttons()


    # TOP MENU
    def create_menu(self):
        self.menubar = tk.Menu(self.root)
        menu_definitions = (
            'File- &New Pattern/ /self.new_pattern, Open Pattern/ /self.open_pattern, Save Pattern/ /self.save_pattern,\
            sep, Save As Picture/ /self.image_save, sep, Exit/ /self.exit_app',

            'View- &Hide Top/ /self.hide_top_bar, Show Top/ /self.show_top_bar,\
             Set Background/ /self.set_background_color ',

            'About- &How to .../ /self.help_func, About Project/ /self.about_func')

        self.build_menu(menu_definitions)

    def set_background_color(self):
        choose_bg = askcolor(title="Change Background Color")
        new_bg = choose_bg[1]

        if new_bg:
            self.main_bg_color = new_bg

            # for scrolling work correctly app needs to redraw
            # destroy current left frame
            for widgets in self.left_frame.winfo_children():
                widgets.destroy()

            self.canvas_lf = tk.Canvas(self.left_frame,
                                       width=self.monitor_width,
                                       height=self.monitor_height,
                                       bg=self.main_bg_color,
                                       scrollregion=(0, 0, 500, self.rows_num * 41))

            self.scrollbar = tk.Scrollbar(self.left_frame)
            self.scrollbar.pack(side="right", fill="y")
            self.scrollbar.config(command=self.canvas_lf.yview)
            self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
            self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

            self.left_frame.pack(fill=tk.X, padx=5, pady=5)
            self.draw_left_num_bar()
            self.color_picker_pad()
            self.draw_center_of_threads()
            self.draw_threads()
            self.draw_knots()
            self.put_buttons()

    def hide_top_bar(self):
        self.window.forget()

    def on_check_without_save(self):
        if self.checkCmd.get() == 0:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='1', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=1)
        if self.checkCmd.get() == 1:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='1', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot()).grid(row=0, column=1)

        if self.checkCmd_1.get() == 0:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='2', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=4)
        if self.checkCmd_1.get() == 1:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='2', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot()).grid(row=0, column=4)

        if self.checkCmd_2.get() == 0:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='3', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=6)
        if self.checkCmd_2.get() == 1:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='3', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot()).grid(row=0, column=6)

        if self.checkCmd_3.get() == 0:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='4', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='disabled',
                      relief='flat').grid(row=0, column=8)
        if self.checkCmd_3.get() == 1:
            tk.Button(self.snp_frame,
                      font=("Arial", 18, 'bold'),
                      text='4', bg='#bba5bc',
                      foreground='white',
                      width=3,
                      state='active',
                      relief='raised',
                      command=lambda: self.run_snapshot()).grid(row=0, column=8)

    def show_top_bar(self):

        self.left_frame.forget()

        self.main_window()
        self.on_check_without_save()
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

    def save_pattern(self):
        # create dictionary
        my_dict = {'threads_colors': self.colors_list,
                   'threads_num': self.threads.get(),
                   'rows_num': self.rows.get(),
                   'knots_array': self.main_array,
                   'threads_colors_array': self.threads_colors_array,
                   'rows_number_hidden': self.hidden}

        # file save dialog
        filename = asksaveasfile(initialfile='my_bracelet.knw', defaultextension=".knw",
                                 filetypes=[("All Files", "*.*"), ("Patterns", "*.knw")])
        # if decided to save
        if filename:
            file_path = Path(filename.name)
            # write
            file_path.write_text(str(my_dict))

    def open_pattern(self):
        # open file dialog
        filename = askopenfilename(title='Open a file', initialdir='/', filetypes=[('text files', '*.knw'),
                                                                                   ('All files', '*.*')])
        if not filename:
            return

        # if decided to open
        if filename:
            file_path = Path(filename)

            # read data from file
            data = file_path.read_text()

            # put data from file to list
            details = ast.literal_eval(data)

            # # rewrite variables
            # # threads colors array
            self.colors_list = details['threads_colors']

            # number of threads
            # change number in Spinbox
            self.threads.set(details['threads_num'])

            # change "threads_start_num" variable
            self.threads_start_num = details['threads_num']
            #
            # number of rows
            # change "rows_num" variable
            # change number in Spinbox

            self.rows.set(details['rows_num'])
            self.rows_num = details['rows_num']

            # # change knots array to new array
            self.main_array = details['knots_array']

            # change threads colors array
            self.threads_colors_array = details['threads_colors_array']

            # show/hide rows numbers bar
            self.hidden = details['rows_number_hidden']


            # for scrolling work correctly app needs to redraw
            # destroy current left frame
            for widgets in self.left_frame.winfo_children():
                widgets.destroy()

            self.canvas_lf = tk.Canvas(self.left_frame,
                                       width=self.monitor_width,
                                       height=self.monitor_height,
                                       bg=self.main_bg_color,
                                       scrollregion=(0, 0, 500, self.rows_num * 41))

            self.scrollbar = tk.Scrollbar(self.left_frame)
            self.scrollbar.pack(side="right", fill="y")
            self.scrollbar.config(command=self.canvas_lf.yview)
            self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
            self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)

            self.left_frame.pack(fill=tk.X, padx=5, pady=5)
            self.draw_left_num_bar()
            self.color_picker_pad()
            self.draw_center_of_threads()
            self.draw_threads()
            self.draw_knots()
            self.put_buttons()

    def new_pattern(self):
        # set threads and rows in snipping tool windows to default values
        self.threads.set(18)
        self.threads_start_num = 18
        self.rows.set(30)
        self.rows_num = 30

        # for scrolling work correctly app needs to redraw left frame

        # destroy current left frame children objects
        for widgets in self.left_frame.winfo_children():
            widgets.destroy()

        # create new objects
        self.canvas_lf = tk.Canvas(self.left_frame,
                                   width=self.monitor_width,
                                   height=self.monitor_height,
                                   bg=self.main_bg_color,
                                   scrollregion=(0, 0, 500, self.rows_num * 41))

        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.canvas_lf.yview)
        self.canvas_lf.config(yscrollcommand=self.scrollbar.set)
        self.canvas_lf.pack(fill=tk.X, padx=5, pady=5)
        self.left_frame.pack(fill=tk.X, padx=5, pady=5)

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

    # if user close app from main menu, folder "/snapshots" removed  recursively (with all files in it)
    # if user close app by clicking on red "X" in right top, function "exit_handler()" used in "main"
    def exit_app(self):
        # current directory
        current_directory = Path.cwd()

        # path to snapshots folder
        snap_dir_path = current_directory / "snapshots"

        # drop directory
        shutil.rmtree(snap_dir_path)

        # close app
        self.root.destroy()

    def image_save(self):

        top = self.top = tk.Toplevel(self.window, background=self.main_bg_color)
        self.top.geometry("614x750")

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
                                        font=("Arial", 10))
        self.mySubmitButton.grid(row=13, column=1, sticky='w', pady=40, padx=60, ipady=10)

        self.mySubmitButton1 = tk.Button(top, text='Pass and Save', command=self.parent_func, foreground='#2C2C29',
                                         font=("Arial", 10))
        self.mySubmitButton1.grid(row=13, column=2, sticky='e', pady=40, padx=60, ipady=10)

    def parent_func(self):
        self.save_image()
        self.top.destroy()

    def about_func(self):
        top = self.top = tk.Toplevel(self.window, background=self.main_bg_color)
        self.top.geometry("600x600")
        text_1 = '\n \n KnotWizard Project \n \n' \
                 ' The idea of the project:\n create the best friendship bracelet pattern editor. \n \n'  \
                 ' For the latest version or donations please visit:\n  knotwizard.com \n \n' \
                 ' Application created in Python 3.10 \n \n'  \
                 ' Open source code: github.com/djindji/knotwizard \n \n' \
                 ' Version: beta 1.0\n \n' \
                 ' Feel free to update or change.\n \n \n \n' \
                 ' Special thanks to: \n' \
                 '  Mihai Cătălin Teodosiu for Python Video Course and\n' \
                 '  Bhaskar Chaudhary for understanding how Tkinter works.\n \n \n' \
                 ' Kindest regards,\n' \
                 '  Eduard Kruminsh'

        text_window = tk.Text(top, width=600, height=600)
        text_window.insert(tk.INSERT, text_1)
        text_window.pack()

    def help_func(self):
        top = self.top = tk.Toplevel(self.window, background=self.main_bg_color)
        self.top.geometry("656x434")

        bg_path = Path.cwd() / 'icons' / 'help.png'

        tool_bar_icon = tk.PhotoImage(file=bg_path)

        tool_bar = tk.Label(self.top, image=tool_bar_icon)
        tool_bar.image = tool_bar_icon
        tool_bar.pack()


def main():
    root = tk.Tk()
    root.title('KnotWizard')

    data_folder = Path('icons')
    logo_file = data_folder / 'new_logo.ico'
    root.iconbitmap(logo_file)

    # root.state('zoomed')
    root.geometry('1200x700')

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
