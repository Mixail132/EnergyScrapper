import os
import fdb
from dotenv import load_dotenv


load_dotenv()
DATABASE = os.getenv("DATABASE_PATH")
DB_CLIENT = os.getenv("DBCLIENT_PATH")


connect = fdb.connect(
    host='localhost',
    database=DATABASE,
    user='sysdba',
    password='masterkey',
    charset="UTF-8",
    fb_library_name=DB_CLIENT
)

cursor = connect.cursor()