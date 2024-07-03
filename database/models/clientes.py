from peewee import Model, CharField
from database.database import db

class Cliente(Model):
    nome = CharField()
    cpf = CharField()
    email = CharField()
    telefone = CharField()
    cidade = CharField()
    empresa = CharField()

    class Meta:
        database = db
