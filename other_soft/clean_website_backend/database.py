
import re
from other_soft.clean_website_backend.directory import directory
class database():
    def __init__(self):
        self.dir = directory()

    def find_username_and_id(self,database_file, codec):
        user_info = None
        for row in open(database_file,'r', encoding=codec) :
            if re.match(".*( 'nickname', ).*", row) is not None :
                #extract the avalues limted by ','
                row = re.findall('\((.*?)\)', row)[0]
                info = [term.strip() for term in row.split(',')]
                if info is not None:
                    user_info={"user_id": info[1], "user_name": info[3]}
                    yield user_info

    def find_image(self, database_file, codec,  user_id):
        user_image = None
        for row in open(database_file, 'r', encoding=codec):
            user_syntax = ".*(, {}, ').*".format(user_id)
            image_syntax = "\(.*( 'image\/).*\)"
            portion_url_regex = ".*(http:|https:.+?(?<=assets)).*"
            ''' must satisfy three condition: id, image/ , and match https://duplicatedemo.notesquare.com/assets/'''
            if re.match(user_syntax, row) is not None and re.match(image_syntax, row) and re.match(portion_url_regex,row):
            #if re.match(image_syntax, row) :
            #if re.match(portion_url_regex,row):
                # extract the avalues limted by ','
                row = re.findall('\((.*?)\)', row)[0]
                info = [term.strip() for term in row.split(',')]
                if info is not None:
                    user_image = {"user_id": info[1], "user_image_name": info[11], "user_image_url": info[18]}
                    yield user_image

