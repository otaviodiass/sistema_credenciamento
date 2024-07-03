from flet import *
import tkinter as tk
from templates.tela_cadastro import TelaCadastro
from templates.tela_busca import TelaBusca
from templates.tela_confirmar import TelaConfirmar
from configuracao import configurar_database

def main(page: Page):

    configurar_database()

    root = tk.Tk()

    monitor_altura = root.winfo_screenheight()
    monitor_largura = root.winfo_screenwidth()

    page.adaptive = True
    page.window_maximized = True
    page.window_height = monitor_altura
    page.window_width = monitor_largura

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Credenciamento"), bgcolor=colors.SURFACE_VARIANT, center_title=True),
                    Row(controls=[
                        ElevatedButton("Buscar Cliente", on_click=lambda _: page.go("/buscar")),
                        ElevatedButton("Confirmar Presença", on_click=lambda _: page.go("/confirmar")),
                        ElevatedButton("Cadastrar", on_click=lambda _: page.go("/cadastrar"))
                    ], alignment=MainAxisAlignment.CENTER)
                ]
            )
        )
        if page.route == "/buscar":
            page.views.append(
                View(
                    "/buscar",
                    [
                        AppBar(title=Text("Buscar Cliente"), bgcolor=colors.SURFACE_VARIANT, center_title=True),
                        TelaBusca(page=page)               
                    ],
                )
            )
        elif page.route == "/confirmar":
            page.views.append(
                View(
                    "/confirmar",
                    [
                        AppBar(title=Text("Confirmar Presença"), bgcolor=colors.SURFACE_VARIANT, center_title=True),
                        TelaConfirmar(page=page)               
                    ],
                )
            )
        elif page.route == "/cadastrar":
            page.views.append(
                View(
                    "/cadastrar",
                    [
                        AppBar(title=Text("Cadastrar"), bgcolor=colors.SURFACE_VARIANT, center_title=True),
                        TelaCadastro(page=page)                   
                    ],
                )
            )
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

app(main)
