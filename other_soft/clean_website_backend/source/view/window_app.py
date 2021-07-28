import tkinter as tk
from tkinter import *
from tkinter import filedialog
from other_soft.clean_website_backend.source.model import global_vars

class window_app():
    def __init__(self, control):
        self.ctl = control


    def source_folder_btn(self):

        global_vars.img_folder_path = filedialog.askdirectory()

    def sql_folder_btn(self):

        global_vars.sql_file_folder = filedialog.askdirectory()

    def theme_folder_btn(self):
        global_vars.theme_file_folder = filedialog.askdirectory()

    def main_window(self):
        window = tk.Tk(className="filter unused images between database and wordpress folder")
        # img_folder_path = StringVar()
        # sql_file_folder = StringVar()

        #title = Label(text = "FILTER UNUSED IMAGES")
        #title.grid(row=0)
        #obtain all images folder path
        source_folder_label = Label(text="Browse to current uploads folder")
        source_folder_label.grid(row=1, column = 0)

        browse_btn = Button(text="Browse", command=self.source_folder_btn)
        browse_btn.grid(row=1,column=1)


        #obtain sql image folder
        sql_folder_label = Label(text="Browse to sql files folder")
        sql_folder_label.grid(row=2, column=0)
        browse_btn = Button(text="Browse", command=self.sql_folder_btn)
        browse_btn.grid(row=2,column=1)

        # obtain sql image folder
        sql_folder_label = Label(text="Browse to theme files folder")
        sql_folder_label.grid(row=3, column=0)
        browse_btn = Button(text="Browse", command=self.theme_folder_btn)
        browse_btn.grid(row=3, column=1)


        start_btn = Button(text="Start", command=self.ctl.start)
        start_btn.grid(row = 1, column=4)
        window.grid_columnconfigure(0, minsize=200)
        window.grid_columnconfigure(1, minsize=100)
        window.grid_columnconfigure(4,minsize=10)
        window.geometry("500x400")
        return window