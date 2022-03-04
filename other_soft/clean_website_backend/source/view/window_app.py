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

    def submit_db_name(self):
        global_vars.database_name = database_name_text_field.get(1.0,"end-1c")


    def main_window(self):
        window = tk.Tk(className="filter unused images between database and wordpress folder")
        # img_folder_path = StringVar()
        # sql_file_folder = StringVar()

        #title = Label(text = "FILTER UNUSED IMAGES")
        #title.grid(row=0)
        #obtain all images folder path
        source_folder_label = Label(text="Browse to current wordpress folder")
        source_folder_label.grid(row=1, column = 0)

        browse_btn = Button(text="Browse", command=self.source_folder_btn)
        browse_btn.grid(row=1,column=1)

        #enter database name
        database_name_label = Label(text="Enter database name: ")
        database_name_label.grid(row=2,column=0)
        global database_name_text_field
        database_name_text_field = tk.Text(window, height=1,width=10)
        database_name_text_field.grid(row=2,column=1)


        start_btn = Button(text="Start", command=lambda:[self.submit_db_name(), self.ctl.start_find_image(), self.ctl.start_find_resume()])#, self.ctl.copy_found_images_to_temp_loc(),self.ctl.copy_found_resume_to_temp_location()])
        start_btn.grid(row = 1, column=4)
        window.grid_columnconfigure(0, minsize=200)
        window.grid_columnconfigure(1, minsize=100)
        window.grid_columnconfigure(4,minsize=10)
        window.geometry("500x400")
        return window
