from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Credenciado(Model):
    nome = CharField()
    cpf = CharField()
    email = CharField()
    telefone = CharField()
    cidade = CharField()
    empresa = CharField()
    data_credenciamento = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
