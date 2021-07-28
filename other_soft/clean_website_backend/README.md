

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