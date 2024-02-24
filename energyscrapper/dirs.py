from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = str(Path(os.getenv("DATABASE_PATH")))
DB_CLIENT = str(Path(os.getenv("DBCLIENT_PATH")))
DB_EXCEL = str(Path(os.getenv("DBEXCEL_PATH")))
