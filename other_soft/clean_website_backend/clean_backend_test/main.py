

from other_soft.clean_website_backend.source.model.theme import theme
from other_soft.clean_website_backend.source.model.directory import directory
from other_soft.clean_website_backend.source.model.database import database
from other_soft.clean_website_backend.source.view.window_app import window_app
from other_soft.clean_website_backend.source.controller.controller import controller
if __name__ == "__main__":
    theme_ctl = theme()
    dir_ctl = directory()
    db_ctl = database()
    ctl = controller(db_ctl,dir_ctl,theme_ctl)
    interface_object = window_app(ctl)
    main_window = interface_object.main_window()
    main_window.mainloop()#starting the interface

