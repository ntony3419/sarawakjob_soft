import tkinter.messagebox as msg
from other_soft.clean_website_backend.source.model import global_vars
class controller():
    def __init__(self,database, directory, theme):
        self.database = database
        self.directory = directory
        self.theme = theme
    def start(self):
        print('program started')
        print(global_vars.img_folder_path)
        print(global_vars.sql_file_folder)
        print(global_vars.theme_file_folder)
        self.database.init_save_file_user_image()
        self.database.init_save_file_job_image()
        #self.database.filter_images_user_id_base(global_vars.img_folder_path,global_vars.sql_file_folder)
        self.database.filter_image_used_by_job_post(global_vars.img_folder_path, global_vars.sql_file_folder)

        msg.showinfo(title="Finish", message="click ok to finish")