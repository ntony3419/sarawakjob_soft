import csv
import os
import re
import traceback

from chardet.universaldetector import UniversalDetector
import shutil
class directory():
    def __init__(self):
        pass

    def determine_codec(self, file_path):
        # check the encoding of the file
        file_encode = None
        detector = UniversalDetector()
        rawdata = open(file_path, 'rb')
        for line in rawdata:
            # line = bytes(line,"utf-8")
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        rawdata.close()
        file_encode = detector.result  # export the data
        return file_encode

    '''save a list or tuple of data to file'''

    def append_to_file(self, file_path, datas_list):
        # save_loc =r"C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend\user_image_data.csv"

        try:
            f = open(file_path, 'a+', encoding='utf-8', newline='')
            f_writer = csv.writer(f, delimiter=',')
            f_writer.writerow(datas_list)
            f.close()
        except:
            err=traceback.format_exc()
            # print(err)

    def pixel_resize(self, image_path, size):
        path_no_extension = os.path.splitext(image_path)[0]
        new_path = f"{path_no_extension}-size"
        return


    '''
        DESCRIPTION:
            new_location (ex: C:/temp/)
            file_path (ex: C:/upload/2014/image.jpg)
            result: file is copy to new location and create similar structure ( ex: C:/temp/upload/2014/image.jpg)
            
    '''
    def copy(self, file_path,new_location):
        try:
            #make dirs
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            #copy
            shutil.copy(file_path,new_location)
        except:
            err= traceback.format_exc()
            pass

    '''input : search_location, file_rel_path, file_name
        Description: search_location is the folder that might contain the image (format: C:/theme/upload/)
                    file_rel_path is the relative p[ath of the file ( format: /image/up/file.jpg
                    file_name is the file name to search (format: file.jpg
    '''
    def absolute_path(self, search_location, file_rel_path):
        result = []

        # Wlaking top-down from the root
        file_name = re.findall("([^\/]*.(?:jpg|gif|png))", file_rel_path)[0]
        for root, dir, files in os.walk(search_location):
            if file_name in files:
                result.append(os.path.join(root, file_name))
        '''many file with same file name is found'''
        # location = None
        # for path in result:  # if same file name in multiple location
        #     #convert the '\\' in value of each path to '/' so that the re can match correctly
        #     new_file_path= None
        #     try:
        #         #new_file_path = path.replace("\\","/") #relative path of the file use / for directory so create a new_file_path using / from path for conviniene search
        #         new_file_path = path.replace("/",
        #                                      "\\")  # relative path of the file use / for directory so create a new_file_path using / from path for conviniene search
        #     except:
        #         pass
        #     syntax = None
        #     ''' regex syntax :
        #         source : '\'https://duplicatedemo.notesquare.com/assets/2012/10/13.jpg\''
        #         regex : .*(http.*[assets$]).*
        #         result : https://duplicatedemo.notesquare.com/assets
        #     '''
        #     if re.match(".*(http.*[assets$]).*", file_rel_path) is not None:
        #             syntax = "(?<=uploads).*\.(?:jpg|gif|png)"
        #     else:
        #         syntax = r".*{}.*".format(file_rel_path) #syntax to match relative path of file (file_rel_path) to portion of MODIFIED absolution path (new_file_path)
        #     if re.match(syntax,new_file_path) is not None:
        #         location = path
        return result


    # def absolute_path(self, search_location, file_rel_path):
    #     result = []
    #
    #     # Wlaking top-down from the root
    #     file_name = re.findall("([^\/]*.(?:jpg|gif|png))", file_rel_path)[0]
    #     for root, dir, files in os.walk(search_location):
    #         if file_name in files:
    #             result.append(os.path.join(root, file_name))
    #     '''many file with same file name is found'''
    #     location = None
    #     for path in result:  # if same file name in multiple location
    #         #convert the '\\' in value of each path to '/' so that the re can match correctly
    #         new_file_path= None
    #         try:
    #             new_file_path = path.replace("\\","/") #relative path of the file use / for directory so create a new_file_path using / from path for conviniene search
    #         except:
    #             pass
    #         syntax = r".*{}.*".format(file_rel_path) #syntax to match relative path of file (file_rel_path) to portion of MODIFIED absolution path (new_file_path)
    #         if re.match(syntax,new_file_path) is not None:
    #             location = path
    #     return location