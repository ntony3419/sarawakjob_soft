import os

import time
import traceback

from chardet.universaldetector import UniversalDetector
''' this function take in a folder and will loop through all the FILE in that folder (except sub directory) and seach the keyword content'''
def search_file_contain_keyword(folder, keyword):
    # change working directory to the target location
    os.chdir(folder)
    found_file = []
    if len(os.listdir(folder)) != 0:
        for item in os.listdir(): #loop through each file
            #if file extension is php
            file_name = os.path.splitext(item)[0]
            file_extension = os.path.splitext(item)[1]
            if file_extension =='.php':
                #open file
                try:
                    f = open(item, mode='r')
                    for line in f:
                        if keyword in line:
                            found_file.append(item)
                            found = True
                            break
                    f.close()
                except:
                    pass
    if len(found_file) > 0:
        for i in found_file:
            print(i)

def find_replace_phrase(folder, old_text, new_text):
    try:
        for root, subdirs, files in os.walk(folder):  # get all the files in folder and sub folder
            for file in os.listdir(root):
                file_path = os.path.join(root,file)
                new_content = []
                try:
                    f = open(file_path,errors='ignore')
                    for line in f:
                        if old_text in line:
                            old_line=line
                            line=line.replace(old_text, new_text)
                            print(f"replacing\nold_text: {old_text} to \nnew_text: {new_text} in \nsource: {old_line}\nresult: {line}\n")
                        new_content.append(line)
                    f.close()
                except:
                    pass

                #open the file in write mode and write new content to the file
                try:
                    f = open(file_path, mode="w",errors='ignore')
                    for item in new_content:
                        f.write(item)
                    f.close()
                except:
                    pass
    except:
        err= (traceback.format_exc())
        pass
def find_phrase_in_folder(folder, text):
    os.chdir(folder)
    found_file = []
    list_file = []
    for root, subdirs, files in os.walk(folder): #get all the files in folder and sub folder
        try:
            for file in files: # loop through each file
                file_path=os.path.join(root,file)

                #found_file.append(os.path.join(root,file))
                file_name = os.path.splitext(file)[0]
                file_extension = os.path.splitext(file)[1]
                if file_extension == '.php':
                    # open file
                    list_file.append(file_path)
                    if file_name == "autoptimizeImages": #can remove this if block
                        time.sleep(1)
                    file_codec = determine_codec(file_path)

                    try:
                        f = None
                        if file_codec is not None and file_codec["encoding"] != "Windows-1254":
                            f = open(file_path, mode='r', encoding=file_codec["encoding"])
                            # successfuly open the file using 1 of the above
                        else:#chardet library doesn't support codec cp1254 (aliases: Windows-1254)
                            f = open(file_path, mode='r', encoding="cp1254")
                        for line in f:
                            if text in line:
                                found_file.append(file_path)
                                found = True
                                break
                        f.close()
                    except:
                        #TODO: for some reason codec cp1254 is successfully open the file but during the iteration will cause exception so can be ignor
                        #print(f"Attempt to open file using {file_codec} encoding failed {traceback.format_exc()}")
                        err=traceback.format_exc()
                        pass
        except:
            err= (traceback.format_exc())
            pass

    if len(found_file) > 0:
        for i in found_file:
            print(i)
    # if len(list_file) > 0:
    #     for i in list_file:
    #         print(i)

def determine_codec(file_path):
    # check the encoding of the file
    file_encode = None
    detector = UniversalDetector()
    rawdata = open(file_path, 'rb')
    for line in rawdata:
        #line = bytes(line,"utf-8")
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    rawdata.close()
    file_encode = detector.result #export the data
    return file_encode

#print(determine_codec(r"D:\duplicatedemo.notesquare.com - original\duplicatedemo.notesquare.com_edit\wp-comments-post.php"))
#find_replace_phrase(r"D:\duplicatedemo.notesquare.com\home\wp-content\themes\sjobsv2", "msia.notesquare.com","duplicatedemo.notesquare.com")
find_replace_phrase(r"D:\sarawakjobs\JobsBrunei Quang\JobsBrunei Quang\CMS for jobsbrunei.com", "www.jobsbrunei.com","jbdemo.notesquare.com")
#search_file_contain_keyword(r"D:\duplicatedemo.notesquare.com - original\duplicatedemo.notesquare.com_edit\home\wp-content\themes\sjobsv2", "Keyword: Admin")
#find_phrase_in_folder(r"D:\duplicatedemo.notesquare.com - original\duplicatedemo.notesquare.com_edit", "user_custom_avatar_id")
#search_file_contain_keyword(r"C:\Users\quang nguyen\Downloads\test_text", "column-search")


