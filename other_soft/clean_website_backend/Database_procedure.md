<h2>Find images from sql</h2>
<p>-1. Query will find all row that contains images url.</p>
<pre>  SELECT
  ID,post_author,post_name,post_date,guid,post_type,post_mime_type
  FROM
  wp_posts i
  WHERE i.post_type = 'attachment'            
  AND NOT EXISTS (SELECT * FROM wp_posts p WHERE p.ID = i.post_parent)
  AND NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_key = '_thumbnail_id' AND pm.meta_value = i.ID)            
  AND NOT EXISTS (SELECT * FROM wp_posts p WHERE p.post_type <> 'attachment' AND p.post_content LIKE CONCAT('%',i.guid,'%'))
  AND NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_value LIKE CONCAT('%',i.guid,'%'))</pre>
<p>Result of above query:</p>
<pre>{'ID': 276256, 'post_author': 18888, 'post_name': '2', 'post_date': datetime.datetime(2021, 7, 19, 19, 45, 24), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/2.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276257, 'post_author': 18888, 'post_name': '3-3', 'post_date': datetime.datetime(2021, 7, 19, 19, 46, 19), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/3.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276260, 'post_author': 20090, 'post_name': '3-4', 'post_date': datetime.datetime(2021, 7, 19, 19, 56, 12), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/3.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276261, 'post_author': 20090, 'post_name': '1-2', 'post_date': datetime.datetime(2021, 7, 19, 19, 57, 41), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/1.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276264, 'post_author': 20089, 'post_name': 'test_image_3', 'post_date': datetime.datetime(2021, 7, 19, 22, 39, 39), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276266, 'post_author': 20091, 'post_name': 'test_image_3-2', 'post_date': datetime.datetime(2021, 7, 19, 23, 22, 41), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276267, 'post_author': 20089, 'post_name': '22_7_2021_test', 'post_date': datetime.datetime(2021, 7, 22, 14, 16, 44), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/22_7_2021_test.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276268, 'post_author': 20084, 'post_name': '23_7_2021_test_1', 'post_date': datetime.datetime(2021, 7, 23, 16, 37, 41), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/23_7_2021_test_1.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276269, 'post_author': 20084, 'post_name': '23_7_2021_test_2', 'post_date': datetime.datetime(2021, 7, 23, 16, 38, 15), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/23_7_2021_test_2.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276274, 'post_author': 20089, 'post_name': '31_7_2021_test', 'post_date': datetime.datetime(2021, 7, 31, 17, 9, 30), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/31_7_2021_test.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
{'ID': 276275, 'post_author': 20089, 'post_name': '31_7_2021_test_2', 'post_date': datetime.datetime(2021, 7, 31, 17, 26, 6), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/31_7_2021_test_2.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}</pre>
<p>2. Sort and order data to list of dictionaries base on post_author</p>
<pre>Example List of data for post_author 20089:
'20089':[
{'ID': 276275, 'post_author': 20089, 'post_name': '31_7_2021_test_2', 'post_date': datetime.datetime(2021, 7, 31, 17, 26, 6), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/31_7_2021_test_2.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'},
{'ID': 276274, 'post_author': 20089, 'post_name': '31_7_2021_test', 'post_date': datetime.datetime(2021, 7, 31, 17, 9, 30), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/31_7_2021_test.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'},
{'ID': 276267, 'post_author': 20089, 'post_name': '22_7_2021_test', 'post_date': datetime.datetime(2021, 7, 22, 14, 16, 44), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/22_7_2021_test.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'},
{'ID': 276264, 'post_author': 20089, 'post_name': 'test_image_3', 'post_date': datetime.datetime(2021, 7, 19, 22, 39, 39), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
]
</pre>
<p>3. Clean up the post_author data. For each post_author, iterating over list of entries, and find the entry with nearest post_date time</p>
<pre>
Example: Below entry is newest from the list of entries
{'ID': 276275, 'post_author': 20089, 'post_name': '31_7_2021_test_2', 'post_date': datetime.datetime(2021, 7, 31, 17, 26, 6), 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/31_7_2021_test_2.jpg', 'post_type': 'attachment', 'post_mime_type': 'image/jpeg'}
</pre>
<p>4. For each latest user id found, use the guid to find other image size (100x100, 200x200)</p>
<pre>Example: 'guid': 'https://duplicatedemo.notesquare.com/assets/2014/02/31_7_2021_test_2.jpg'
other size images are : 2014/02/31_7_2021_test_2-100x100.jpg, 2014/02/31_7_2021_test_2-200x200.jpg
</pre>
<p>4.1 Find original iamge from guid</p>
<pre>'guid':'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg'</pre>




























<pre><h1>Below method doesn't work</h1><h1><strong>DATABASE:</strong></h1>

<h2>I. Find username:</h2>
<h3>1. Search for the username from nickname base on format</h3>
<pre>show in database: (445919, 20089, 'nickname', 'duplicatedemo_wp'),
    user id :     20089
    username is : duplicatedemo_wp
    reference key : nickname
    Note: each username is unique
</pre>

<h2>II. User-image connection:</h2>
<h3>1. once the username is found, program return the username and userid to find image  associate with user id</h3>
 
<h3>2. The image is linked to user's "nickname" through user id</h3>
<pre>(276264, 20089, '2021-07-19 22:39:39', '2021-07-19 14:39:39', '', 'test_image_3', '', 'inherit', 'closed', 'closed', '', 'test_image_3', '', '', '2021-07-19 22:39:39', '2021-07-19 14:39:39', '', 0, 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg', 0, 'attachment', 'image/jpeg', 0),
    user id : 20089
    image url : https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg 
    image name : test_image_3.jpg
</pre>
<h3>3. To get the image from the above format, program should attempt verify following exist in the format</h3>
<pre>user id :20089
file type : image/jpeg (can use only term 'image' as there are more type of image than just jpeg)
part of image url :https://duplicatedemo.notesquare.com/assets/
</pre>
<h3>4. once ALL the three criterias above are satisfied, use regular expression to extract the images</h3>
<pre>(276264, 20089, '2021-07-19 22:39:39', '2021-07-19 14:39:39', '', 'test_image_3', '', 'inherit', 'closed', 'closed', '', 'test_image_3', '', '', '2021-07-19 22:39:39', '2021-07-19 14:39:39', '', 0, 'https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg', 0, 'attachment', 'image/jpeg', 0)
    regex: (http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?
    result: https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg
</pre>
<h3>5. extract the image name out of the previous url</h3>
<pre>
https://duplicatedemo.notesquare.com/assets/2014/02/test_image_3.jpg
    regex: ([^\/]+)$
    result: test_image_3.jpg </pre>


<h2>Resume </h2>

<h2>query to find images being use in the database</h2>

SELECT
  *
FROM
  wp_posts i
WHERE
  i.post_type = 'attachment'
  AND
  NOT EXISTS (SELECT * FROM wp_posts p WHERE p.ID = i.post_parent)
  AND
  NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_key = '_thumbnail_id' AND pm.meta_value = i.ID)
  AND
  NOT EXISTS (SELECT * FROM wp_posts p WHERE p.post_type <> 'attachment' AND p.post_content LIKE CONCAT('%',i.guid,'%'))
  AND
  NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_value LIKE CONCAT('%',i.guid,'%'))



</pre>