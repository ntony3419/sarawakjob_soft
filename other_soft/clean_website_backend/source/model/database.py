import datetime
import traceback
import csv
import os
import re
import shutil
from other_soft.clean_website_backend.source.model.directory import directory
class database():
    def __init__(self):
        self.dir = directory()


    '''input : root_folder, folder_hold_sql_file
        output : 
        description: root_foler- folder contain all images of the site
                    - folder_hold_sql_file - if the site has more than 1 database sql
    '''
    def find_user_image_data_multi_sql(self, root_folder, folder_hold_sql_file):
        '''find user id and user name in sql files'''
        for user_info in self.user_and_id_multi_files(folder_hold_sql_file, "latin"):
            #user_info will be a dict contain "user_id" and "user_name"
            #find image location and other info using user0info above
            image_data_list=[]
            for image_data_in_sql in self.user_image_data_from_multi_sql_files(folder_hold_sql_file,"latin",user_info):
                image_data_list.append(image_data_in_sql)
            #find the latest on base on upload time
            latest_image_data = None
            if len(image_data_list) >0:
                latest_image_data = image_data_list[0]
                for item in image_data_list: #loop to find the latest one base on upload time
                    if datetime.datetime.strptime(latest_image_data["upload_time"], "%Y-%m-%d %H:%M:%S") < datetime.datetime.strptime(item["upload_time"], "%Y-%m-%d %H:%M:%S"):
                        latest_image_data = item #item is newer
            #image_data_in_sql["user_id",user_image_name,user_image_url]
            #find location using image_data_in_sql dict {user_id, user_image, user_image_url}

            '''find image location'''
            if latest_image_data is not None:
                image_name = self.extract_image_name(latest_image_data["user_image_url"])
                image_location_data = self.find_file_location(root_folder, image_name)
                image_all_data = {"user_id":latest_image_data["user_id"],"user_name":user_info["user_name"],
                                  "user_image_name":image_name,"user_image_short_name":latest_image_data["user_image_short_name"],
                                  "user_image_url":latest_image_data["user_image_url"],
                                  "image_location":image_location_data, "file_using_image":latest_image_data["file_contain_image_url"],
                                  "source_row":latest_image_data["source_row"]}
                yield image_all_data #use this value to move file



    def extract_image_name(self, image_url):
        image_name = None
        try:
            image_name = re.findall("([^\/]*.(?:jpg|gif|png|jpeg))", image_url)[0]
        except:
            print(f"issue with extracting image name: \n"
                  f"statement :  image_name=re.findall('([^\/]*.(?:jpg|gif|png|jpeg))', image_url)[0]\n"
                  f"source: {image_url}"
                                                                    )
        return image_name


    def find_file_location(self, root_folder, file_name):
        file_location = None
        for root, subdir, files in os.walk(root_folder):
            for file in files:
                file_path = os.path.join(root, file)
                if file_name == file: #compare the name portion of the iterating file to the file_name
                    file_location = file_path
        return file_location

    def init_save_file_user_image(self):
        '''create a csv file to save the data for manual check'''
        parrent_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        user_image_data_file_path = f"{parrent_folder}\\user_image_data.csv"
        f = open(
            user_image_data_file_path,
            "w+", encoding='utf-8',
            newline='')  # C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend
        writer = csv.writer(f, delimiter=',')
        writer.writerow(
            ["USER_ID", "USER_NAME", "IMAGE NAME", "IMAGE_SHORT_NAME","IMAGE PATH STRUCTURE USED IN FILE","SOURCE ROW CONTAIN IMAGE", "IMAGE_FILE_LOCATION", "FILE USING IMAGE"])
        f.close()
    def init_save_file_job_image(self):
        '''create a csv file to save the data for manual check'''
        parrent_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        user_image_data_file_path = f"{parrent_folder}\\job_img.csv"
        f = open(
            user_image_data_file_path,
            "w+", encoding='utf-8',
            newline='')  # C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend
        writer = csv.writer(f, delimiter=',')
        writer.writerow(
            ["IMAGE ID", "IMAGE RELATIVE PATH",  "IMAGE PATH STRUCTURE USED IN FILE",
             "SOURCE ROW CONTAIN IMAGE", "IMAGE ABSOLUTE PATH", "FILE USING IMAGE"])
        f.close()

    '''method to find user and id from multiple sql files in one folder 
        INPUT: sql file, encoding
    '''
    def user_and_id_multi_files(self, database_folder, codec):
        for root, subdirs, files in os.walk(database_folder):
            for file in files:
                sql_file_path = os.path.join(root,file)
                for user_info in self.user_and_id(sql_file_path, codec):
                    yield user_info

    '''find user name and user id from single sql file'''
    def user_and_id(self,database_file, codec):
        user_info = None
        if os.path.splitext(database_file)[1] == ".sql": #make sure the file extension is .sql
            for row in open(database_file,'r', encoding=codec) :
                if re.match(".*( 'nickname', ).*", row) is not None :
                    #extract the avalues limted by ','
                    row = re.findall('\((.*?)\)', row)[0]
                    info = [term.strip() for term in row.split(',')]
                    if info is not None:
                        user_info={"user_id": info[1], "user_name": info[3].replace("'","")}
                        yield user_info

    '''export user_id, user_name, image_name, user_image_url '''
    def user_image_from_sql_file(self, sql_file, codec, user_info):
        for row in open(sql_file, 'r', encoding=codec):
            user_syntax = ".*(, {}, ').*".format(user_info["user_id"])
            image_syntax = "\(.*( 'image\/).*\)"
            portion_url_regex = ".*(http:|https:.+?(?<=assets)).*"
            ''' must satisfy three condition: id, image/ , and match https://duplicatedemo.notesquare.com/assets/'''
            if re.match(user_syntax, row) is not None and re.match(image_syntax, row) is not None and re.match(
                    portion_url_regex, row) is not None:
                # if re.match(image_syntax, row) :
                # if re.match(portion_url_regex,row):
                # extract the avalues limted by ','
                row = re.findall('\((.*?)\)', row)[0]
                info = [term.strip() for term in row.split(',')]

                if info is not None:
                    try:
                        #get the latest image base on upload time. upload time is 3rd place (index 2)
                        #upload_time = info[2]


                        user_image = {"user_id": info[1], "user_image_name": info[11].replace("'",""), "upload_time":info[2].replace("'",""),
                                      "user_image_short_name":info[11].replace("'",""),
                                      "user_image_url": info[18].replace("'",""), "file_contain_image_url": sql_file, "source_row": row}
                        yield user_image
                    except Exception as err:
                        print(
                            f"error in extracting image using user id: {err.__traceback__}\nworking on value data: {info}\n maybe that row doesn't have image information")
    '''Description: call user_image_from_sql_file() to get the infor of image associate with user in multiple sql files
        data will be : (user_id, user_image, user_image_url)
    '''
    def user_image_data_from_multi_sql_files(self, folder_hold_sql_files, codec, user_info):
        for root, subdirs, files in os.walk(folder_hold_sql_files):
            for file in files:
                sql_file = os.path.join(root, file)

                for data in self.user_image_from_sql_file(sql_file,codec,user_info):
                    yield data


    '''this function will find the image that connect to user by user id'''
    '''TODO: depereciated can be deleted- new method user_image'''
    def profile_image(self, database_file, codec,  user_id):
        user_image = None
        for row in open(database_file, 'r', encoding=codec):
            user_syntax = ".*(, {}, ').*".format(user_id)
            image_syntax = "\(.*( 'image\/).*\)"
            portion_url_regex = ".*(http:|https:.+?(?<=assets)).*"
            ''' must satisfy three condition: id, image/ , and match https://duplicatedemo.notesquare.com/assets/'''
            if re.match(user_syntax, row) is not None and re.match(image_syntax, row) is not None and re.match(portion_url_regex,row) is not None:
            #if re.match(image_syntax, row) :
            #if re.match(portion_url_regex,row):
                # extract the avalues limted by ','
                row = re.findall('\((.*?)\)', row)[0]
                info = [term.strip() for term in row.split(',')]

                if info is not None:
                    try:
                        user_image = {"user_id": info[1], "user_image_name": info[11], "user_image_url": info[18] }
                        yield user_image
                    except Exception as err:
                        print(f"error in extracting image using user id: {err.__traceback__}\nworking on value data: {info}")


    ''' all the images in database generator 
        TODO: depreciated'''
    def images_use_in_database(self, folder_hold_sql_file):
        '''create a csv file to save the data for manual check'''
        # image_data_file_path = r"C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend\all_images_in_db.csv"
        # f = open(
        #     image_data_file_path,
        #     "w+", encoding='utf-8',
        #     newline='')  # C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend
        # writer = csv.writer(f, delimiter=',')
        # writer.writerow(["USER_ID", "IMAGE", "IMAGE ABSOLUTE PATH", "FILE USING IMAGE URL"])
        # f.close()

        '''find user id and user name in sql files'''
        for root, subdirs, files in os.walk(folder_hold_sql_file):  # go throug each sql file in the folder
            for file in files:
                sql_file_path = os.path.join(root, file)

                for image_info in self.find_image_relative_path(sql_file_path):
                    '''TODO: use image_info to find absolute path'''
                    image_name = image_info[0]
                    rel_path = image_info[1]

                    '''add to file for testing purpose'''




    def find_image_relative_path(self, file_name, codec):
        user_image = None
        for row in open(file_name, 'r', encoding=codec):
            image_rel_path_syntax = "(([\\\/|\w|\s|-])*\.(?:jpg|gif|png|jpeg))"
            image_relative_path = None
            if re.match(image_rel_path_syntax, row) is not None: #match relative regex to the row data
                # if re.match(image_syntax, row) :
                # if re.match(portion_url_regex,row):
                # extract the avalues limted by ','
                image_relative_path = re.findall(image_rel_path_syntax,row)[0]
                image_name = re.findall("([^\/]*.(?:jpg|gif|png|jpeg))", image_relative_path)
                yield image_name,image_relative_path
    '''copy the found image to new location'''
    def copy_found_image_to_new_location(self, new_location,image_datas):
        pass

    def update_sql(self, sql_folder, image_datas):
        pass

    def filter_image_used_by_job_post(self,images_folder, sql_folder):
        for image_info in self.find_feature_image_in_sql(sql_folder,"latin"):
            img_relative_path = image_info["image_relative_path"]
            image_info["img_path_structure_in_file"] = img_relative_path
            img_relative_path_window = img_relative_path.replace("/","\\") #convert to window format
            try:
                if os.path.splitext(img_relative_path_window)[1] in ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'):
                    img_name = re.findall(r"([^\\]*.(?:jpg|gif|png|jpeg))", img_relative_path_window)[0]
            except:
                print("\nIssue in filter_image-used_by_job_post: \n{}other details\n"
                      "statement: img_name = re.findall(r'([^\\]*.(?:jpg|gif|png|jpeg))', img_relative_path_window)[0]\n"
                      "source: {}\n"
                      "source type: {}\n"
                      "regex result : {}".format(traceback.format_exc(),img_relative_path_window,type(img_relative_path_window),re.findall(r'([^\\]*.(?:jpg|gif|png|jpeg))', img_relative_path_window)))
                print(img_relative_path_window)
            #use img_relative_path_window to find the image location
            for root, subdir, files in os.walk(images_folder):
                for file in files:
                    image_abs_path = os.path.join(root,file)
                    image_abs_path=image_abs_path.replace("/","\\")
                    image_info["img_abs_path"] = image_abs_path
                    if img_relative_path_window in image_abs_path: #found correct image
                        temp_upload_folder = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", image_abs_path)[0]
                        temp_upload_folder = os.path.join(os.path.dirname(temp_upload_folder), r"uploads_new")
                        if os.path.exists(temp_upload_folder) is False:
                            os.makedirs(temp_upload_folder)
                        print(temp_upload_folder)

                        # start copy
                        file_dest = os.path.join(temp_upload_folder,
                                                 img_relative_path_window)  # result ex:  D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\Test-1-employer.jpg'
                        dest_folder = re.findall(r"([a-zA-Z]:\\.*?\\)((?:[^\\]|\\\/)+?)(?:(?<!\\)\s|$)", file_dest)[0][
                            0]  # result ex:D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\
                        print(dest_folder)
                        # print(type(dest_folder))
                        if os.path.exists(dest_folder) is False:
                            os.makedirs(dest_folder)
                        try:
                            shutil.copy(image_abs_path, file_dest)
                        except shutil.SameFileError:
                            print("same file same path was copied")
                        except:
                            err = traceback.format_exc()
                            print(err)
            '''for manual testing'''
            parrent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            save_to_file = f"{parrent_folder}\\job_image.csv"
            self.dir.append_to_file(save_to_file,
                               [image_info["image_id"], image_info["image_relative_path"],
                                image_info["image_relative_path"],
                                image_info["source_row"],
                                image_info["img_abs_path"], image_info["file_use_image"]])


    def find_feature_image_in_sql(self ,sql_folder,codec):
        feature_image_info = None
        for root, subdir, files in os.walk(sql_folder):

            for file in files:
                sql_file = os.path.join(root, file)
                if os.path.splitext(sql_file)[1] == ".sql":  # make sure the file extension is .sql
                    for row in open(sql_file, 'r', encoding=codec):
                        if re.match(".*( '_wp_attached_file', ).*", row) is not None:
                            # extract the avalues limted by ','
                            row = re.findall('\((.*?)\)', row)[0]
                            info = [term.strip() for term in row.split(',')]
                            if info is not None:
                                feature_image_info = {"image_id": info[1], "image_relative_path": info[3].replace("'", ""), "source_row": row, "file_use_image": sql_file}
                                yield feature_image_info


    def filter_images_user_id_base(self, images_folder, sql_folder):
        for image_all_data in self.find_user_image_data_multi_sql(   images_folder,sql_folder):
            # image_all_data_list = list(db.find_user_image_data_multi_sql(r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit",r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\folder hold database files"))
            # for image_all_data in image_all_data_list:
            print(image_all_data)
            found_image_url = image_all_data["user_image_url"]
            relative_path = re.findall(".*((?<=assets\/).*\.(?:jpg|gif|png|jpeg))", found_image_url)[0]
            print(relative_path)
            # convert_relative_path to window path
            window_format_relative_path = relative_path.replace("/", "\\")
            print(window_format_relative_path)
            # find the image in the upload folder
            for root, subdirs, files in os.walk(images_folder):
                for file in files:
                    original_img_file_path = os.path.join(root, file)
                    original_img_file_path=original_img_file_path.replace("/","\\")
                    img_100_path = self.generate_other_img_size(original_img_file_path,"100x100")
                    img_200_path = self.generate_other_img_size(original_img_file_path,"200x200")

                    if window_format_relative_path in original_img_file_path:
                        print("original iamge path ", original_img_file_path)
                        if img_100_path is not None:
                            print(img_100_path)
                        if img_200_path is not None:
                            print(img_200_path)
                        # copy this to the temp
                        temp_upload_folder = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", original_img_file_path)[0]
                        temp_upload_folder = os.path.join(os.path.dirname(temp_upload_folder), r"uploads_new")
                        if os.path.exists(temp_upload_folder) is False:
                            os.makedirs(temp_upload_folder)
                        print(temp_upload_folder)

                        # start copy
                        file_dest = os.path.join(temp_upload_folder,
                                                 window_format_relative_path)  # result ex:  D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\Test-1-employer.jpg'
                        dest_folder = re.findall(r"([a-zA-Z]:\\.*?\\)((?:[^\\]|\\\/)+?)(?:(?<!\\)\s|$)", file_dest)[0][
                            0]  # result ex:D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\
                        print(dest_folder)
                        # print(type(dest_folder))
                        if os.path.exists(dest_folder) is False:
                            os.makedirs(dest_folder)
                        try:
                            shutil.copy(original_img_file_path, file_dest)
                            if os.path.exists(img_100_path) is True:
                                shutil.copy(img_100_path, file_dest)
                            if os.path.exists(img_200_path) is True:
                                shutil.copy(img_100_path, file_dest)
                        except shutil.SameFileError:
                            print("same file same path was copied")
                        except:
                            err = traceback.format_exc()
                            print(err)

            '''for manual testing'''
            parrent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            save_to_file = f"{parrent_folder}\\user_image_data.csv"
            self.dir.append_to_file(save_to_file,
                               [image_all_data["user_id"], image_all_data["user_name"], image_all_data["user_image_name"],
                                image_all_data["user_image_url"], image_all_data["source_row"],
                                image_all_data["image_location"], image_all_data["file_using_image"]])

    def generate_other_img_size(self, original_img_path, new_size):
        new_image_size_path= None
        if original_img_path.endswith((".jpg",".gif",".png",".jpeg")):
            img_name = re.findall(r"([^\/]*.(?:jpg|gif|png|jpeg))", original_img_path)[0]
            img_dir = re.findall(r"([a-zA-Z]:\\.*?\\)((?:[^\\]|\\\/)+?)(?:(?<!\\)\s|$)", original_img_path)[0][0]
            #img_dir = re.findall(r"([a-zA-Z]:\\.*?\\)((?:[^\\]|\\\/)+?)(?:(?<!\\)\s|$)", original_img_path)
            img_name_no_ext = os.path.splitext(img_name)[0]
            img_ext = os.path.splitext(img_name)[1]
            new_image_size = f"{img_name_no_ext}-{new_size}{img_ext}"
            new_image_size_path =os.path.join(img_dir, new_image_size)
        return new_image_size_path

