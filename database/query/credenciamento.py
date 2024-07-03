from database.models.credenciamento import Credenciado

def buscar_todos_clientes():
    clientes = Credenciado.select()
    return clientes

def buscar_cliente_nome(nome: str):
    cliente = Credenciado.select().where(Credenciado.nome.contains(nome))
    return cliente

def buscar_cliente_cpf(cpf: str):
    cliente = Credenciado.select().where(Credenciado.cpf == cpf)
    return cliente

def cadastrar_cliente(cliente):
    Credenciado.create(nome=cliente.nome, cpf=cliente.cpf, email=cliente.email, telefone=cliente.telefone, cidade=cliente.cidade, empresa=cliente.empresa)
