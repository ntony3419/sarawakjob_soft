import time

import pymysql

def wp_post_query():
    con = pymysql.connect(host="localhost", database="jobbruney2", user="root", passwd="")
    c=con.cursor(pymysql.cursors.DictCursor)

    query='''
    SELECT
      *
    FROM
      wp_posts i
    WHERE
        i.post_type = 'attachment'   
    '''

    c.execute(query)
    #data = c.fetchmany(1000)
    #print(data)
    for row in c.fetchall():
        yield(row)
    c.close()
    con.close()

def wp_postmeta_query():
    con = pymysql.connect(host="localhost", database="duplicate2", user="root", passwd="")
    c = con.cursor(pymysql.cursors.DictCursor)

    query = '''
        SELECT
            *
        FROM
            wp_postmeta 
        WHERE post_type='attachment'
          
       '''

    c.execute(query)
    # data = c.fetchmany(1000)
    # print(data)
    for row in c.fetchall():
        yield (row)
    c.close()
    con.close()
#
# for data in wp_post_query():#wp_post post_type is attachment
#     #for data_2 in wp_postmeta_query():
#     print("data 1: ", data)
#     for data_2 in wp_post_query(): #another set query for wp_post
#         print("data 2: " ,data_2)
#         #time.sleep(1)
#         if (data_2["ID"] == data["post_parent"]): #only when this data_2.ID == previous data.post_parent
#             print("result: " , data)


def test():
    con = pymysql.connect(host="localhost", database="duplicate2", user="root", passwd="")
    c = con.cursor(pymysql.cursors.DictCursor)

    query = '''
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

    c.execute(query)
    # data = c.fetchmany(1000)
    # print(data)
    for row in c.fetchall():
        yield (row)
    c.close()
    con.close()

for data in test():
    print(data)

# con = pymysql.connect(host="localhost", database="jobbruney2", user="root",passwd="")
# c=con.cursor(pymysql.cursors.DictCursor)
# query_combine = '''
# SELECT
#   ID,post_author,post_name,post_date,guid,post_type,post_mime_type
# FROM
#   wp_posts i
# WHERE
#     i.post_type = 'attachment'
#     AND
#     NOT EXISTS (SELECT * FROM wp_posts p WHERE p.ID = i.post_parent)
#     AND
#     NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_key = '_thumbnail_id' AND pm.meta_value = i.ID)
#     AND
#     NOT EXISTS (SELECT * FROM wp_posts p WHERE p.post_type <> 'attachment' AND p.post_content LIKE CONCAT('%',i.guid,'%'))
#     AND
#     NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_value LIKE CONCAT('%',i.guid,'%'))
#     '''
# query_1='''
# SELECT
#   *
# FROM
#   wp_posts i
# WHERE
#     i.post_type = 'attachment'
# '''
# query_2=''''''
#
# query_3='''SELECT * FROM wp_posts p WHERE p.post_type <> 'attachment' AND p.post_content LIKE CONCAT('%',wp_posts.guid,'%')'''
# query_4=''''''
# query_5=''''''
# print("executing the query")
# c.execute(query_1)
# #data = c.fetchmany(1000)
# #print(data)
# for row in c.fetchmany(100):
#     print(row)
# c.close()
# con.close()
#
# def data_wp_posts_query_1():
#     con = pymysql.connect(host="localhost", database="jobbruney2", user="root",passwd="")
#     c=con.cursor(pymysql.cursors.DictCursor)
#
#     query_1='''
#     SELECT
#       *
#     FROM
#       wp_posts i
#     WHERE
#         i.post_type = 'attachment'
#     '''
#
#     c.execute(query_1)
#     #data = c.fetchmany(1000)
#     #print(data)
#     for row in c.fetchall():
#         yield(row)
#     c.close()
#     con.close()
#
#
# def data_wp_posts_post_parent_query_2():
#     con = pymysql.connect(host="localhost", database="jobbruney2", user="root", passwd="")
#     c = con.cursor(pymysql.cursors.DictCursor)
#
#     query_1 = '''
#         SELECT * FROM wp_posts
#     '''
#     c.execute(query_1)
#     # data = c.fetchmany(1000)
#     # print(data)
#     for row in c.fetchall():
#         yield (row)
#     c.close()
#     con.close()
#
# def data_wp_posts_post_meta_query_3():
#     con = pymysql.connect(host="localhost", database="jobbruney2", user="root", passwd="")
#     c = con.cursor(pymysql.cursors.DictCursor)
#
#     query = '''
#         SELECT * FROM wp_postmeta pm WHERE pm.meta_key = '_thumbnail_id'
#     '''
#     c.execute(query)
#     # data = c.fetchmany(1000)
#     # print(data)
#     for row in c.fetchall():
#         yield (row)
#     c.close()
#     con.close()
#
# def data_wp_posts_query_4():
#     con = pymysql.connect(host="localhost", database="jobbruney2", user="root", passwd="")
#     c = con.cursor(pymysql.cursors.DictCursor)
#
#     query = '''
#         SELECT * FROM wp_posts p WHERE p.post_type <> 'attachment'
#     '''
#     c.execute(query)
#     # data = c.fetchmany(1000)
#     # print(data)
#     for row in c.fetchall():
#         yield (row)
#     c.close()
#     con.close()
#
#
# def data_wp_posts_post_meta_query_5():
#     con = pymysql.connect(host="localhost", database="jobbruney2", user="root", passwd="")
#     c = con.cursor(pymysql.cursors.DictCursor)
#     #   modified this SELECT * FROM wp_postmeta pm WHERE pm.meta_value LIKE CONCAT('%',data_query_1.guid,'%')
#     query = '''
#         SELECT * FROM wp_postmeta pm WHERE pm.meta_value LIKE CONCAT('%',{}['guid'],'%')
#     '''.format(data_query_1)
#     c.execute(query)
#     # data = c.fetchmany(1000)
#     # print(data)
#     for row in c.fetchall():
#         yield (row)
#     c.close()
#     con.close()
#
#
# '''compare post ID of query one data with post_parent of Query 2 data'''
# def compare_data_query_1_2(query_1_data, query_2_data):
#     pass
#
# def compare_data_query_1_3(data_query_1, data_query_3):
#     #if data_query_1.ID == data_query_3.meta_value
#     pass
# def compare_data_query_1_4(data_query_1, data_query_4):
#     #if data_query_4.post_content == CONCAT("%", data_query_1, "%")
#     pass

# '''Query 1''' #i.post_type = 'attachment'
# for data in data_wp_posts_query_1():
#     print(data)
#
# '''Query 2''' #  (SELECT * FROM wp_posts p WHERE p.ID = i.post_parent)
# for data in data_wp_posts_post_parent_query_2():
#     print(data)

'''Query 3''' # (SELECT * FROM wp_postmeta pm WHERE pm.meta_key = '_thumbnail_id' AND pm.meta_value = i.ID)
# for data in data_wp_posts_query_4():
#     print(data)
#
# '''query 5'''
# for data in data_wp_posts_query_1():
#     for data_2 in data_wp_posts_post_meta_query_5(data):
#         print(data)

'''
SELECT
  ID,post_author,post_name,post_date,guid,post_type,post_mime_type
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
    '''

#example wp_post
#{'ID': 475512, 'post_author': 34343, 'post_date': datetime.datetime(2021, 7, 14, 19, 30, 47), 'post_date_gmt': datetime.datetime(2021, 7, 14, 11, 30, 47), 'post_content': '', 'post_title': 'recopy2-100x100', 'post_excerpt': '', 'post_status': 'inherit', 'comment_status': 'closed', 'ping_status': 'closed', 'post_password': '', 'post_name': 'recopy2-100x100', 'to_ping': '', 'pinged': '', 'post_modified': datetime.datetime(2021, 7, 14, 19, 30, 47), 'post_modified_gmt': datetime.datetime(2021, 7, 14, 11, 30, 47), 'post_content_filtered': '', 'post_parent': 0, 'guid': 'https://www.jobsbrunei.com/assets/2014/02/recopy2-100x100.jpg', 'menu_order': 0, 'post_type': 'attachment', 'post_mime_type': 'image/jpeg', 'comment_count': 0}
#example post_meta
'''{'meta_id': 4276701, 'post_id': 475503, 'meta_key': '_wp_attached_file', 'meta_value': 'resume_offline/2021/07/NANI-CV-1.docx.pdf'}'''

'''
           SELECT
           ID,post_author,post_name,post_date,guid,post_type,post_mime_type
           FROM
           wp_posts i
           WHERE i.post_type = 'attachment'
           AND i.post_parent > 0
           AND NOT EXISTS (SELECT * FROM wp_posts p WHERE p.ID = i.post_parent)
           AND NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_key = '_thumbnail_id' AND pm.meta_value = i.ID)
           AND NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_key = '_product_image_gallery' AND pm.meta_value LIKE CONCAT('%', i.ID,'%'))
           AND NOT EXISTS (SELECT * FROM wp_posts p WHERE p.post_type <> 'attachment' AND p.post_content LIKE CONCAT('%',i.guid,'%'))
           AND NOT EXISTS (SELECT * FROM wp_postmeta pm WHERE pm.meta_value LIKE CONCAT('%',i.guid,'%'))

         '''
import pymysql
con = None
try:
    con = pymysql.connect(host="localhost", database="duplicate2", user="root", passwd="")
except:
    print("error connection")
    #tkinter.messagebox.showerror("unable to connect to database. Check the SQL server or database name to match")
c = con.cursor(pymysql.cursors.DictCursor)
query = '''
           SELECT
           *
           FROM
           wp_posts i
           WHERE i.post_type = 'attachment'            and i.post_mime_type = 'application/pdf'
           

         '''

c.execute(query)
# data = c.fetchmany(1000)
# print(data)
for row in c.fetchall():
    print(row)
c.close()
con.close()