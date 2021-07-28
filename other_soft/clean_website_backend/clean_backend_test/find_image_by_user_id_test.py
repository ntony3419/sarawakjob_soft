import re
import shutil
import traceback

from source.model.database import database
from source.model.directory import directory
import os
db = database()
dir = directory()

'''init save file'''
db.init_save_file_user_image()

'''find user name and user id'''

db.filter_images_user_id_base(r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit",r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\folder hold database files")
#
# for image_all_data in db.find_user_image_data_multi_sql(r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit",r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\folder hold database files"):
# #image_all_data_list = list(db.find_user_image_data_multi_sql(r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit",r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\folder hold database files"))
# #for image_all_data in image_all_data_list:
#     print(image_all_data)
#     found_image_url = image_all_data["user_image_url"]
#     relative_path = re.findall(".*((?<=assets\/).*\.(?:jpg|gif|png|jpeg))", found_image_url)[0]
#     print(relative_path)
#     #convert_relative_path to window path
#     window_format_relative_path = relative_path.replace("/", "\\")
#     print(window_format_relative_path)
#     #find the image in the upload folder
#     for root, subdirs, files in os.walk(r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit"):
#         for file in files:
#             file_path = os.path.join(root,file)
#             if window_format_relative_path in file_path:
#                 print(file_path)
#                 #copy this to the temp
#                 temp_upload_folder = re.findall(".*([a-zA-Z]:.+?(?<=uploads)).*", file_path)[0]
#                 temp_upload_folder = os.path.join(os.path.dirname(temp_upload_folder),r"uploads_new")
#                 if os.path.exists(temp_upload_folder) is False:
#                     os.makedirs(temp_upload_folder)
#                 print(temp_upload_folder)
#
#                 #start copy
#                 file_dest = os.path.join(temp_upload_folder,window_format_relative_path)                    #result ex:  D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\Test-1-employer.jpg'
#                 dest_folder = re.findall(r"([a-zA-Z]:\\.*?\\)((?:[^\\]|\\\/)+?)(?:(?<!\\)\s|$)", file_dest)[0][0] #result ex:D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\
#                 print(dest_folder)
#                 #print(type(dest_folder))
#                 if os.path.exists(dest_folder) is False:
#                     os.makedirs(dest_folder)
#                 try:
#                     shutil.copy(file_path, file_dest)
#                 except shutil.SameFileError:
#                     print("same file same path was copied")
#                 except:
#                     err = traceback.format_exc()
#                     print(err)
#
#
#
#


    # '''for manual testing'''
    # parrent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # save_to_file = f"{parrent_folder}\\user_image_data.csv"
    # dir.append_to_file(save_to_file,
    #                    [image_all_data["user_id"], image_all_data["user_name"], image_all_data["user_image_name"],
    #                     image_all_data["user_image_url"], image_all_data["source_row"],
    #                     image_all_data["image_location"], image_all_data["file_using_image"]])
    # '''find all other image size'''



    # '''for manual checking - export to a csv file'''


#user_id ='20089'
#for info in db.find_user_image_data_multi_sql(r"D:\sarawakjobs\duplicatedemo_notesquare.com\indopaan_duplicatedemo02 - test_1.sql", "latin", user_id):
#   print(info["user_id"], info["user_image_name"], info["user_image_url"])

