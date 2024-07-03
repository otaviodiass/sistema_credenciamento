from flet import *
from database.query.cliente import buscar_cliente_nome, buscar_cliente_cpf, buscar_todos_clientes
from database.query.credenciamento import cadastrar_cliente

class TelaBusca(Column):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.label_campo_busca = TextField(label="Nome", width=600, on_change=self.buscar_cliente, on_submit=self.buscar_cliente)
        self.botao_buscar = ElevatedButton(text="Buscar", on_click=self.buscar_cliente)

        self.linha_busca = Row(controls=[self.label_campo_busca, self.botao_buscar], alignment=MainAxisAlignment.CENTER)

        self.controls = [self.linha_busca]
    
    def buscar_cliente(self, event):

        if len(self.controls) > 1:
            self.controls.pop()
            self.update()

        valor = self.label_campo_busca.value

        if valor != '':
            clientes = buscar_cliente_nome(valor)
            if len(clientes) != 0:
                self.monta_tabela(clientes)
    
    def monta_tabela(self, lista_cliente):

        lista_linhas = []

        for c in lista_cliente:
            lista_linhas.append(DataRow(cells=[
                DataCell(Text(c.nome)),
                DataCell(Text(c.cpf)),
                DataCell(Text(c.cidade)),
                DataCell(IconButton(icon=icons.ARROW_FORWARD_ROUNDED, data=c, on_click=lambda e: self.cliente_selecionado(e))),
            ]))

        tabela = DataTable(
            columns=[
                DataColumn(Text('Nome')),
                DataColumn(Text('CPF')),
                DataColumn(Text('Cidade')),
                DataColumn(Text('Selecionar')),
            ]
        )

        for l in lista_linhas:
            tabela.rows.append(l)

        self.controls.append(tabela)
        self.update()
    
    def cliente_selecionado(self, event):
        dados = event.control.data

        self.controls.clear()

        self.label_nome = TextField(label='Nome', width=600)

        self.label_cpf = TextField(label='CPF', width=250)

        self.label_email = TextField(label='Email', width=600)

        self.label_telefone = TextField(label='Telefone', width=250)

        self.label_cidade = TextField(label='Cidade', width=600)

        self.label_empresa = TextField(label='Empresa', width=600)
        
        self.botao_cadastrar = ElevatedButton(text="Cadastrar", data=dados, on_click=self.cadastrar)

        self.botao_imprimir = ElevatedButton(text="Imprimir")

        self.label_nome.value = dados.nome
        self.label_cpf.value = dados.cpf
        self.label_email.value = dados.email
        self.label_telefone.value = dados.telefone
        self.label_cidade.value = dados.cidade
        self.label_empresa.value = dados.empresa

        self.linha_nome_cpf = Row(controls=[self.label_nome, self.label_cpf], alignment=MainAxisAlignment.CENTER)
        self.linha_email_telefone = Row(controls=[self.label_email, self.label_telefone], alignment=MainAxisAlignment.CENTER)
        self.linha_botoes = Row(controls=[self.botao_cadastrar, self.botao_imprimir], alignment=MainAxisAlignment.CENTER)

        self.controls.append(self.linha_nome_cpf)
        self.controls.append(self.linha_email_telefone)
        self.controls.append(self.label_cidade)
        self.controls.append(self.label_empresa)
        self.controls.append(self.linha_botoes)
        self.update()
    
    def cadastrar(self, event):
        dados = event.control.data
        cadastrar_cliente(dados)
