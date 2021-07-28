
from other_soft.clean_website_backend.source.model.database import database
from other_soft.clean_website_backend.source.model.directory import directory
import os
db = database()
dir = directory()

'''init save file'''

db.init_save_file_job_image()
db.filter_image_used_by_job_post(r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit",r"D:\sarawakjobs\duplicatedemo.notesquare.com_origin\folder hold database files")