
from other_soft.clean_website_backend.database import database
from other_soft.clean_website_backend.directory import directory
db = database()
dir = directory()
#codec = dir.determine_codec(r"D:\sarawakjobs\duplicatedemo_notesquare.com\indopaan_duplicatedemo02.sql")
'''find user id and user name in sql file'''
for info in db.find_username_and_id(r"D:\sarawakjobs\duplicatedemo_notesquare.com\indopaan_duplicatedemo02.sql", "latin"):
    print(info["user_id"], info["user_name"])
