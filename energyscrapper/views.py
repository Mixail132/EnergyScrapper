import sqlalchemy as db


path='/C:/Users/Ev/Documents/Python/EnergyScrapper/ENERGY.GDB'
db_uri='firebird+firebird://SYSDBA:masterkey@localhost:3050/ENERGY.GDB'
engine=db.create_engine(db_uri, echo=True)

connection = engine.connect()
metadata = db.MetaData()
impuls4 = db.Table(['impuls4'], metadata, autoload=True, autoload_with=engine)
query = db.select([impuls4])