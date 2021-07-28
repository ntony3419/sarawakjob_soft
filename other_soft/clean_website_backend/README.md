
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
</pre>
</p>
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