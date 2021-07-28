import sys
sys.path.append(r"C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft")

from source.model.theme import theme
from source.model.directory import directory
from source.model.database import database
from source.view.window_app import window_app
from source.controller.controller import controller

if __name__ == "__main__":
    theme_ctl = theme()
    dir_ctl = directory()
    db_ctl = database()
    ctl = controller(db_ctl, dir_ctl, theme_ctl)
    interface_object = window_app(ctl)
    main_window = interface_object.main_window()
    main_window.mainloop()  # starting the interface
