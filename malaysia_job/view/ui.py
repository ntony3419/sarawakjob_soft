import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from malaysia_job.model import global_var
from malaysia_job.controller import controller
def wordpress_tab(tab_control):
    wordpress = ttk.Frame(tab_control)

    data_file_label = Label(wordpress, text="Data File: ")
    data_file_label.grid(row=0,column=0)

    sel_file_btn = Button(wordpress, text="browse", command=select_file)
    sel_file_btn.grid(row=0,column=1)


    startBtn = Button(wordpress, text='Start', command=controller.start)
    startBtn.grid(row=0,column=2)
    return wordpress
def select_file():
    global_var.data_file_name = askopenfilename(title="Select a File")


def print_a():
    print(global_var.data_file_name)
