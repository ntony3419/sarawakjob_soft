from other_soft.clean_website_backend.database import database
from other_soft.clean_website_backend.directory import directory
db = database()
dir = directory()

user_id ='20089'
for info in db.find_image(r"D:\sarawakjobs\duplicatedemo_notesquare.com\indopaan_duplicatedemo02 - test_1.sql", "latin", user_id):
    print(info["user_id"], info["user_image_name"], info["user_image_url"])

