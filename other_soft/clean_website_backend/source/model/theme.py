import csv
import os
import traceback
import re
from other_soft.clean_website_backend.source.model.directory import directory


class theme():
    def __init__(self):
        pass
        self.dir = directory()
    def start(self, image_folder, theme_folder):
        '''create a csv file to save the data for manual check'''
        f = open(r"C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend\theme_image_data.csv", "w+", encoding='utf-8', newline='')                  #C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend
        writer = csv.writer(f,delimiter=',')
        writer.writerow(["IMAGE RELATIVE PATH", "ORIGINAL TEXT","IMAGE ABSOLUTE PATH", "FROM FILE"])
        f.close()

        '''main algorithm'''
        for root, subdir , files in os.walk(theme_folder):
            for file in files:
                #if file.endswith(".php"):
                    file_path = os.path.join(root,file)

                    try:
                        for tup_item in self.find_image(theme_folder,file_path):
                            image_relative_path=None
                            if tup_item[0] is not None :
                                if len(tup_item) !=0:
                                    #print(tup_item)
                                    image_relative_path =tup_item[0][0]
                                    abs_path = tup_item[1]
                                    print(image_relative_path, ",", abs_path)
                                    '''TODO: copy abs_path image to a temp location with similar structure'''
                                    self.dir.copy(r"C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend",abs_path)

                    except:
                        err = traceback.format_exc()
                        pass
    def find_image(self, folder, file_path):
        codec = directory().determine_codec(file_path)
        for row in open(file_path, 'r', encoding=codec["encoding"]):
            image_rel_path= None
            abs_path= None
            image_regex = "(([\\\/|\w|\s|-])*\.(?:jpg|gif|png))"
            try:
                image_rel_path = re.findall(image_regex, row)[0]

                '''attempt to find absolute path of image'''
                file_name = re.findall("([^\/]+\.(?:jpg|gif|png))",
                                     image_rel_path[0])[0]  # only get file name and its extension
                abs_path= self.dir.absolute_path(folder, image_rel_path[0].strip())

                ''' attempt to write to file for manual check'''
                self.append_to_file([image_rel_path[0], row, abs_path, file_path] )
            except:
                err = traceback.format_exc()
                pass

            yield image_rel_path, abs_path

    '''save a list or tuple of data to file'''
    def append_to_file(self, datas):
        save_loc =r"C:\Users\quang nguyen\PycharmProjects\python\sarawakjob_soft\other_soft\clean_website_backend\theme_image_data.csv"
        with open(save_loc,'a+',encoding='utf-8', newline='') as f:
            writer=csv.writer(f, delimiter=',')
            writer.writerow(datas)



