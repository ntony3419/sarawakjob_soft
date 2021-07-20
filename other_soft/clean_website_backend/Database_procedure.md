<h1><strong>DATABASE:</strong></h1>

I. Find username:
1. Search for the username from nickname base on format
<pre>show in database: (445919, 20089, 'nickname', 'duplicatedemo_wp'),
    user id :     20089
    username is : duplicatedemo_wp
    reference key : nickname
    Note: each username is unique
</pre>

II. User-image connection:
1. once the username is found, program return the username and userid to find image  associate with user id
 
2. The image is linked to user's "nickname" through user id
<pre>(276264, 20089, '2021-07-19 22:39:39', '2021-07-19 14:39:39', '', 'test_image_3', '', 'inherit', 'closed', 'closed', '', 'test_image_3', '', '', '2021-07-19 22:39:39', '2021-07-19 14:39:39', '', 0, 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg', 0, 'attachment', 'image/jpeg', 0),
    user id : 20089
    image url : https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg 
    image name : test_image_3.jpg
</pre>
3. To get the image from the above format, program should attempt verify following exist in the format
<pre>user id :20089
file type : image/jpeg (can use only term 'image' as there are more type of image than just jpeg)
part of image url :https://duplicatedemo.notesquare.com/assets/
</pre>
4. once ALL the three criterias above are satisfied, use regular expression to extract the images
<pre>(276264, 20089, '2021-07-19 22:39:39', '2021-07-19 14:39:39', '', 'test_image_3', '', 'inherit', 'closed', 'closed', '', 'test_image_3', '', '', '2021-07-19 22:39:39', '2021-07-19 14:39:39', '', 0, 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg', 0, 'attachment', 'image/jpeg', 0)
    regex: (http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?
    result: https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg
</pre>
5. extract the image name out of the previous url
<pre>
https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg
    regex: ([^\/]+)$
    result: test_image_3.jpg </pre>




