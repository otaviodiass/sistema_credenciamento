from database.models.clientes import Cliente

def buscar_todos_clientes():
    clientes = Cliente.select()
    return clientes

def buscar_cliente_nome(nome: str):
    cliente = Cliente.select().where(Cliente.nome.contains(nome))
    return cliente

def buscar_cliente_cpf(cpf: str):
    cliente = Cliente.select().where(Cliente.cpf == cpf)
    return cliente
