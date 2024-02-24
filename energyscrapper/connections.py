import os
import fdb
import dirs

DATABASE = dirs.DATABASE
DB_CLIENT = dirs.DB_CLIENT

connect = fdb.connect(
    host='localhost',
    database=DATABASE,
    user='sysdba',
    password='masterkey',
    charset="UTF-8",
    fb_library_name=DB_CLIENT
)

cursor = connect.cursor()