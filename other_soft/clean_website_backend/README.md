<h1>How to build</h1>
<p>1. Make sure pyinstaller is installed. If not install using 
   
<pre>
pip install pyinstaller
</pre>
2. Change directory to .py to create .exe
3. use template "pyinstaller --onefile pythonFile.py"  to create the executable: 
```python 
   pyinsstaller --onefile main.py
   ```
Extra: If the executable file open a command prompt, rebuild the program again with '-w' option
<pre>
pyinstaller --onefile -w main.py
</pre></p>
<p>ERROR: If there is error when execute .exe. Find the file main.spec (located in same location as main.py)</p>
<p>Modified</p>
<pre>a = Analysis(['main.py'],
             pathex=['C:\\Users\\quang nguyen\\PycharmProjects\\python\\sarawakjob_soft\\other_soft\\clean_website_backend'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)</pre>
<p>To:
<pre>a = Analysis(['main.py'],
             pathex=['C:\\ProgramData\\Anaconda3\\Lib', 'C:\\Users\\quang nguyen\\PycharmProjects\\python\\sarawakjob_soft\\other_soft\\clean_website_backend','C:\\Users\\quang nguyen\\PycharmProjects\\python\\sarawakjob_soft','C:\\ProgramData\\Anaconda3\\Lib\\site-packages'],
             binaries=[],
             datas=[],
             hiddenimports=['tkiner.messagebox'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)</pre></p>


<h1>Feature:</h1>
<h2>Find lastest image used by user from database sql</h2>
<pre>query:
 '''
                   SELECT
                   ID,post_author,post_name,post_date,guid,post_type,post_mime_type
                   FROM
                   wp_posts i
                   WHERE i.post_type = 'attachment'            
                   AND NOT EXISTS (SELECT * FROM wp_posts p WHERE p.ID = i.post_parent)
                   AND NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_key = '_thumbnail_id' AND pm.meta_value = i.ID)            
                   AND NOT EXISTS (SELECT * FROM wp_posts p WHERE p.post_type <> 'attachment' AND p.post_content LIKE CONCAT('%',i.guid,'%'))
                   AND NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_value LIKE CONCAT('%',i.guid,'%'))

                 '''
</pre>
<h2>Find lastest offline resume used by user from database sql</h2>
<pre>Example:
 '''
           SELECT
           *
           FROM
           wp_posts i
           WHERE i.post_type = 'attachment'            and i.post_mime_type = 'application/pdf'
           

         '''
{'ID': 276223, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 15, 21), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 15, 21), 'post_content': '', 'post_title': 'test_resume.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-pdf-3', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 15, 21), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 15, 21), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
{'ID': 276224, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 17, 14), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 17, 14), 'post_content': '', 'post_title': 'test_resume.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-pdf-4', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 17, 14), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 17, 14), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
{'ID': 276225, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 20, 11), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 20, 11), 'post_content': '', 'post_title': 'test_resume.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-pdf-5', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 20, 11), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 20, 11), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
{'ID': 276226, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 20, 57), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 20, 57), 'post_content': '', 'post_title': 'test_resume.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-pdf-6', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 20, 57), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 20, 57), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
5{'ID': 276227, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 21, 36), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 21, 36), 'post_content': '', 'post_title': 'test_resume - Copy.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-copy-pdf', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 21, 36), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 21, 36), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume-Copy.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
4{'ID': 276228, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 22, 43), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 22, 43), 'post_content': '', 'post_title': 'test_resume - Copy.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-copy-pdf-2', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 22, 43), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 22, 43), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume-Copy.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
{'ID': 276229, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 30, 15), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 30, 15), 'post_content': '', 'post_title': 'test_resume.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-pdf-7', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 30, 15), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 30, 15), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
3{'ID': 276230, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 31, 5), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 31, 5), 'post_content': '', 'post_title': 'test_resume - Copy.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-copy-pdf-3', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 31, 5), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 31, 5), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume-Copy.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
2{'ID': 276231, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 34, 1), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 34, 1), 'post_content': '', 'post_title': 'test_resume - Copy.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-copy-pdf-4', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 34, 1), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 34, 1), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume-Copy.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
1{'ID': 276232, 'post_author': 18885, 'post_date': datetime.datetime(2021, 7, 15, 18, 35, 19), 'post_date_gmt': datetime.datetime(2021, 7, 15, 10, 35, 19), 'post_content': '', 'post_title': 'test_resume - Copy.pdf', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'test_resume-copy-pdf-5', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 15, 18, 35, 19), 'post_modified_gmt': datetime.datetime(2021, 7, 15, 10, 35, 19), 'post_content_filtered': '', 'post_parent': 274009, 'guid': 'https://duplicatedemo.notesquare.com/assets/resume_offline/2021/07/test_resume-Copy.pdf', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'application/pdf', 'comment_count': 0}
</pre>
<h2> Manual mode </h2>
<p><strong>*** Perform the task on local computer and then upload the new content to the server </strong></p>
- find wordpress username directly from database sql file
- find the image that associate with the username in database sql
- find the image that used by the theme
- locate and copy the user profile image to similar structure directory
    <pre>(ex. old structure : uploads/2014/07
    temp structure : temp/uploads/2014/07 )</pre> 
- locate and copy the image that used by the theme to similar structure directory
<pre>(ex. old structure : uploads/2014/theme-image
    temp structure : temp/theme/sjob/images )</pre>
- replace the old image url that used by the theme to new one
    <pre>ex. : old:  /uploads/2014/07/menulogo.png
                new : theme/images/menulogo.png
</pre>

<h2>Automatic mode</h2>
<p><strong>*** Perform the tasks directly on server through ssh access, no more need of download all the old content and upload new content </strong></p>
- automatically remove the old folder and its content
    <pre>ex. remove old upload folder: wp-content/uploads/*
            * all active content and inactive content
</pre>
- automatically move the new  folder to the old location
    <pre>move new upload folder: temp/uploads/*
            TO                  : wp-content/ 
        * only move the 'uploads/*' part to wp-content/
</pre>