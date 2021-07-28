
from other_soft.clean_website_backend.source.model.database import database
from other_soft.clean_website_backend.source.model.directory import directory
db = database()
dir = directory()
#codec = dir.determine_codec(r"D:\sarawakjobs\duplicatedemo_notesquare.com\indopaan_duplicatedemo02.sql")
'''find user id and user name in sql file'''
db.find_user_image(r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin", r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\folder hold database files")

