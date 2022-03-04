import csv
import re
import os
import tkinter.messagebox as msg
import traceback

from other_soft.clean_website_backend.source.model import global_vars

class controller():
    def __init__(self,database, directory, theme):
        self.database = database
        self.directory = directory
        self.theme = theme
        self.user_resume_dict = {}
        self.user_image_dict={}
    def start_find_image(self):
        #print('program started')
        #print(global_vars.img_folder_path)
        #print(global_vars.sql_file_folder)
        #print(global_vars.theme_file_folder)
        # self.database.init_save_file_user_image()
        # self.database.init_save_file_job_image()
        if global_vars.img_folder_path is None:
            msg.showerror(title="error",message="Missing folder for images!!! click Browse to current wordpress folder.")

        for user_data in self.database.extract_image_data():
            if user_data["post_author"] not in self.user_image_dict.items():
                self.user_image_dict[user_data["post_author"]] = [user_data] #expected result : 20089:[{'ID': 276275, 'post_author': 20089, 'post_name': '31_7_2021_test_2', 'post_date': datetime.datetime(2021, 7, 31, 17, 26, 6), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/31_7_2021_test_2.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}]
            else:
                self.user_image_dict[user_data["post_author"]].append(user_data) #append user_data to existed post_author

        #clean up (keep the nearest time)
        for keys, values in self.user_image_dict.items():
            self.user_image_dict[keys] = self.get_latest_entry(values)

        #print to csv
        try:
            with open("image_file_raw.csv",'w',newline='',encoding='utf-8') as csv_file:
                writer=csv.writer(csv_file)
                for key, value in self.user_image_dict.items():
                    writer.writerow([key,value])
        except:
            error = f"{traceback.format_exc()}\n'close excel file'"
            print(traceback.format_exc(), "close excel file")
            msg.showerror(title="error", message=error)

        #print to csv value of id
        try:
            header = False
            with open("image_file_value.csv", 'w', newline='',encoding='utf-8') as csv_file:
                for key, value in self.user_image_dict.items():
                    for dict_value in value:
                        writer = csv.DictWriter(csv_file, fieldnames=dict_value.keys())
                        if header is False:
                            writer.writeheader()
                            header=True
                        writer.writerow(dict_value)
        except:
            error = f"{traceback.format_exc()}\n'close excel file'"
            print(traceback.format_exc(), "close excel file")
            msg.showerror(title="error", message=error)


    def copy_found_images_to_temp_loc(self):
        # find original images from the lastest image base on post_author
        for keys, values in self.user_image_dict.items():
            relative_path = None
            # extract relative path of image from guid i.e:
            # original: 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg',
            # relative: 2014/02/test_image_3.jpg
            # test = self.user_image_dict[keys][0]
            # test_2 =  re.findall(".*((?<=assets\/).*\.(?:jpg|gif|png|jpeg))", self.user_image_dict[keys]["guid"])
            list_abs_path = []
            try:
                relative_path = \
                re.findall(".*((?<=assets\/).*\.(?:jpg|gif|png|jpeg|webp|svg))", self.user_image_dict[keys][0]["guid"])[
                    0]  # case url contains assets
                # get the absolute path
                list_abs_path = self.directory.image_absolute_path(global_vars.img_folder_path,
                                                                   relative_path)  # re turn a list
            except:
                try:
                    relative_path = re.findall(".*((?<=uploads\/).*\.(?:jpg|gif|png|jpeg|webp|svg))", self.user_image_dict[keys][0]["guid"])[0]  # case url contains uploads
                    list_abs_path = self.directory.image_absolute_path(global_vars.img_folder_path,
                                                                       relative_path)  # re turn a list
                except:
                    print(traceback.format_exc(), self.user_image_dict[keys][0]["guid"])
                    err = f'''{traceback.format_exc()}\n{self.user_image_dict[keys][0]["guid"]}'''
                    # msg.showerror(title="error", message=err)
                    pass
            # copy to new location
            for abs_path in list_abs_path:
                if "uploads" in abs_path:
                    window_relative_path = relative_path.replace("/", "\\")
                    window_abs_path = abs_path.replace("/", "\\")
                    # try:
                    #     test = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", window_abs_path)[0]
                    # except:
                    #     err= traceback.format_exc()
                    #     msg = f'''{err}\n{window_abs_path}\n{re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", window_abs_path)}'''
                    #     pass
                    window_upload_folder_path = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", window_abs_path)[0]
                    if window_relative_path in abs_path:  # found correct image
                        temp_upload_folder = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", window_abs_path)[0]
                        temp_upload_folder = os.path.join(os.path.dirname(temp_upload_folder), r"uploads_new")
                        if os.path.exists(temp_upload_folder) is False:  # create the new temp location
                            os.makedirs(temp_upload_folder)
                        # new absolute path based on old relative_path
                        new_abs_path = os.path.join(temp_upload_folder, window_relative_path)
                        self.directory.copy(window_abs_path, new_abs_path)  # copy original image to new location temp

                        '''find other size images original relative path'''
                        ori_size_100_rel_path = "{}{}{}".format(os.path.splitext(window_relative_path)[0], "-100x100",
                                                                os.path.splitext(window_relative_path)[1])
                        ori_size_200_rel_path = "{}{}{}".format(os.path.splitext(window_relative_path)[0], "-200x200",
                                                                os.path.splitext(window_relative_path)[1])
                        ori_size_100_abs_path = os.path.join(window_upload_folder_path, ori_size_100_rel_path)
                        ori_size_200_abs_path = os.path.join(window_upload_folder_path, ori_size_200_rel_path)
                        if os.path.exists(ori_size_100_abs_path):
                            new_size_100_path = os.path.join(temp_upload_folder, ori_size_100_rel_path)
                            self.directory.copy(ori_size_100_abs_path,
                                                new_size_100_path)  # copy original image to new location temp
                        if os.path.exists(ori_size_200_abs_path):
                            new_size_200_path = os.path.join(temp_upload_folder, ori_size_200_rel_path)
                            '''copy other sizes to new location'''
                            self.directory.copy(ori_size_200_abs_path,
                                                new_size_200_path)  # copy original image to new location temp
        print("done working on images")

    def start_find_resume(self):

        if global_vars.img_folder_path is None:
            msg.showerror(title="error", message="Missing folder for images!!! click Browse to current wordpress folder.")

        for user_data in self.database.extract_resume_data():
                if user_data["post_author"] not in self.user_resume_dict.items():
                    self.user_resume_dict[user_data["post_author"]] = [user_data] #expected result : 20089:[{'ID': 276275, 'post_author': 20089, 'post_name': '31_7_2021_test_2', 'post_date': datetime.datetime(2021, 7, 31, 17, 26, 6), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/31_7_2021_test_2.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}]
                else:
                    self.user_resume_dict[user_data["post_author"]].append(user_data) #append user_data to existed post_author

        # clean up (keep the nearest time)
        for keys, values in self.user_resume_dict.items():
            self.user_resume_dict[keys] = self.get_latest_entry(values)

        # print to csv
        try:
            with open("pdf_file_raw.csv", 'w', newline='',encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in self.user_resume_dict.items():
                    writer.writerow([key, value])
        except:
            error = f"{traceback.format_exc()}\n'close excel file'"
            print(traceback.format_exc(), "close excel file")
            msg.showerror(title="error", message=error)

        # print to csv value of id
        header = False
        try:
            with open("pdf_file_value.csv", 'w', newline='',encoding='utf-8') as csv_file:
                for key, value in self.user_resume_dict.items():
                    for dict_value in value:
                        writer = csv.DictWriter(csv_file, fieldnames=dict_value.keys())
                        if header is False:
                            writer.writeheader()
                            header = True
                        writer.writerow(dict_value)
        except:
            error = f"{traceback.format_exc()}\n'close excel file'"
            print(traceback.format_exc(), "close excel file")
            msg.showerror(title="error", message=error)


    def copy_found_resume_to_temp_location(self):
        # find original location of pdf
        for keys, values in self.user_resume_dict.items():
            relative_path = None
            # extract relative path of image from guid i.e:
            list_abs_path = []
            try:
                relative_path = re.findall(".*((?<=assets\/).*\.(?:pdf|doc|docx))", self.user_resume_dict[keys][0]["guid"])[0]
                # get the absolute path
                list_abs_path = self.directory.resume_absolute_path(global_vars.img_folder_path,
                                                                    relative_path)  # re turn a list
            except:
                try:
                    relative_path = re.findall(".*((?<=uploads\/).*\.(?:pdf|doc|docx))", self.user_resume_dict[keys][0]["guid"])[0]
                    list_abs_path = self.directory.resume_absolute_path(global_vars.img_folder_path,
                                                                    relative_path)  # re turn a list
                except:
                    err = f'''{traceback.format_exc()}\n{self.user_resume_dict[keys][0]["guid"]}'''
                    print(traceback.format_exc(), self.user_resume_dict[keys][0]["guid"])
                    #msg.showerror(title="error", message=err)
                    pass
            # copy to new location
            for abs_path in list_abs_path:
                if "uploads" in abs_path:
                    window_relative_path = relative_path.replace("/", "\\")
                    window_abs_path = abs_path.replace("/", "\\")
                    # try:
                    #     test = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", window_abs_path)[0]
                    # except:
                    #     err= traceback.format_exc()
                    #     msg = f'''{err}\n{window_abs_path}\n{re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", window_abs_path)}'''
                    #     pass
                    window_upload_folder_path = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", window_abs_path)[0]
                    if window_relative_path in abs_path:  # found correct image
                        temp_upload_folder = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", window_abs_path)[0]
                        temp_upload_folder = os.path.join(os.path.dirname(temp_upload_folder), r"uploads_new")
                        if os.path.exists(temp_upload_folder) is False:  # create the new temp location
                            os.makedirs(temp_upload_folder)
                        # new absolute path based on old relative_path
                        new_abs_path = os.path.join(temp_upload_folder, window_relative_path)
                        self.directory.copy(window_abs_path,
                                            new_abs_path)  # copy original image to new location temp

        print("done working on resume")

    def get_latest_entry(self, list_entries):
        new_list = []
        lastest_entry = None
        for entry in list_entries:
            lastest_entry = entry
            if entry['post_date'] > lastest_entry['post_date']:
                lastest_entry = entry
        new_list.append(lastest_entry)
        return new_list

        # self.database.filter_images_user_id_base(global_vars.img_folder_path,global_vars.sql_file_folder)
        # self.database.filter_image_used_by_job_post(global_vars.img_folder_path, global_vars.sql_file_folder)

        msg.showinfo(title="Finish", message="click ok to finish")

