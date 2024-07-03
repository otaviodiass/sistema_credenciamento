from flet import *
from database.query.credenciamento import cadastrar_cliente

class TelaCadastro(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.label_nome = TextField(label='Nome', width=600)

        self.label_cpf = TextField(label='CPF', width=250)

        self.label_email = TextField(label='Email', width=600)

        self.label_telefone = TextField(label='Telefone', width=250)

        self.label_cidade = TextField(label='Cidade', width=600)

        self.label_empresa = TextField(label='Empresa', width=600)

        self.botao_cadastrar = ElevatedButton(text="Cadastrar", on_click=self.cadastrar)

        self.botao_imprimir = ElevatedButton(text="Imprimir")

        self.linha_nome_cpf = Row(controls=[self.label_nome, self.label_cpf], alignment=MainAxisAlignment.CENTER)
        self.linha_email_telefone = Row(controls=[self.label_email, self.label_telefone], alignment=MainAxisAlignment.CENTER)
        self.linha_botoes = Row(controls=[self.botao_cadastrar, self.botao_imprimir], alignment=MainAxisAlignment.CENTER)

        self.controls = [self.linha_nome_cpf, self.linha_email_telefone, self.label_cidade, self.label_empresa, self.linha_botoes]
    
    def cadastrar(self, event):
        nome = self.label_nome.value
        cpf = self.label_cpf.value
        email = self.label_email.value
        telefone = self.label_telefone.value
        cidade = self.label_cidade.value
        empresa = self.label_empresa.value

        dados = {'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone, 'cidade': cidade, 'empresa': empresa}
        cadastrar_cliente(dados)

