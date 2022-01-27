import mysql.connector as mc
from starlette.status import HTTP_404_NOT_FOUND

connection = mc.connect( host = "localhost", passwd = "qwertyuiopasdfghjkl" ,user = "root",database = "api")
cursor = connection.cursor()
cursor.execute('use api;')

# insert new record 
# if you want to pass in a null value, use 'null' in the value holder.
def inster_to_table(record : dict):
    global cursor
    cursor.execute(f"INSERT INTO video_db(title,likes,comments) VALUES ( '{record['title']}', {record['likes']}, {record['comments']} )")
    connection.commit()
    return 201
    
    
# retreiev all data
def get_all():
    global cursor
    v = []
    cursor.execute('select * from video_db')
    for i in cursor:
        v.append(i)
    return 200,v


# get one data
def get_one_specific_data(vid):
    global cursor
    v = []
    cursor.execute(f'select * from video_db where vid = {vid}')
    for i in cursor:
        v.append(i)
    if len(v)>0:
        return v
    return 404

# update an existing data
async def update_video_info(vid,record):
    global cursor, connection
    try:
        cursor.execute(f"UPDATE video_db set  title =  '{record['title']}', likes = {record['likes']}, comments = {record['comments']} where vid = {vid}")
        connection.commit()
        return 202
    except:
        return 404

    

# delete an existing video
async def delete_video(vid):
    global connection,cursor
    try:
        cursor.execute(f"DELETE from video_db where vid = {vid}")
        connection.commit()
    except:
        raise HTTP_404_NOT_FOUND

    

# a func to check if video exists or not in the db
def find_video_with_id(vid):
    global cursor
    cursor.execute(f'SELECT 1 FROM video_db WHERE vid = {vid}')
    for i in cursor:
        if i[0] == 1:
            return True
    return False



  