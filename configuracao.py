from database.database import db
from database.models.clientes import Cliente
from database.models.credenciamento import Credenciado

def configurar_database():
    db.connect()
    db.create_tables([Cliente, Credenciado])