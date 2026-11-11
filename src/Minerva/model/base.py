import peewee as p

mDB = p.SqliteDatabase("C:\\Users\\Franklin\\Documents\\Programming\\MinervaV2\\minerva.db")

class BaseModel(p.Model):
    class Meta:
        database = mDB