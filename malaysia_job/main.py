from tkinter import ttk
import tkinter
from malaysia_job.view import ui
from malaysia_job.controller import controller
if __name__=="__main__":
    main_win = tkinter.Tk()
    tabControl = ttk.Notebook(main_win)

    # wordpress tab
    wordpress_tab = ui.wordpress_tab(tabControl)
    tabControl.add(wordpress_tab, text='wordpress')
    tabControl.grid(row=0, column=0, sticky='nw')

    #start it up
    main_win.mainloop()