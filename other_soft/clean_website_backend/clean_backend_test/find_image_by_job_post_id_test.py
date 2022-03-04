
from other_soft.clean_website_backend.source.model.database import database
from other_soft.clean_website_backend.source.model.directory import directory
import os
db = database()
dir = directory()

'''init save file'''

db.init_save_file_job_image()
root_folder = r"D:\sarawakjobs\JobsBrunei_Quang_origin_with_upload_folder\JobsBrunei_Quang\CMS_for_jobsbrunei_com"
database_folder = r"D:\sarawakjobs\JobsBrunei_Quang_origin_with_upload_folder\JobsBrunei_Quang\singapur_jobsbrunei01_sql"
db.filter_image_used_by_job_post(root_folder,database_folder)