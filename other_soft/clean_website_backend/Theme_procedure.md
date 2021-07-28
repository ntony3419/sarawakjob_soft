1. find image initial path by using regex
<pre>regex: (([\/|.|\w|\s|-])*\.(?:jpg|gif|png))
    or regex: (([\\\/|\w|\s|-])*\.(?:jpg|gif|png)) (this one better)
case: 14:39:39', '', 0, 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg', 0,
result: //duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg
case: https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg 
result: //duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg
case: et_template_directory_uri(); ?>/images/custom/menulogo.png"
result: /images/custom/menulogo.png
case: "shortcut icon" href="<?php echo get_site_url(); ?>/favico.png">
result: /favico.png
</pre>
2. Find name

OPTION 1: from found path above, get the image name 
<pre>regex: ([^\/]+)$
case: /favico.png
result: favico.png
case:/images/custom/menulogo.png
result: menulogo.png
</pre>
OPTION 2: keep the path above and compare it with the possible path
<pre>
case: /images/custom/menulogo.png
possible file path: c://wordpress/wp-content/themes/themeA/images/custom/menulogo.png
result : case is part of the file path - image path is found

</pre>
3. Once image is found copy the image to another location and keep the same structure
<pre>previous path: c://wordpress/wp-content/upload/images/custom/menulogo.png
COPY TO
new path : c://wordpress/wp-content/themes/themeA/images/custom/menulogo.png
</pre>
// TODO: work out procedure for replace the previous path with the new path (if the new path doesn't need to change) 

