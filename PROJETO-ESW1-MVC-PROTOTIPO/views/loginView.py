import flet as ft
import sqlite3
from models.usuario import Usuario 
from .componente.identidadeVisual import exibir_logo, ESTILO_BOTAO_PRIMARIO, ALINHAMENTO_COLUNA

def LoginView(page):
    conexao = sqlite3.connect("banco_de_dados.db", check_same_thread=False)
    usuario = Usuario(conexao)

    def on_login(e):
        username = username_input.value
        password = password_input.value

        print(f"Tentando login com: {username}, {password}") 

        role = usuario.validar_credenciais(username, password)
        
        if role:
            print(f"Redirecionando para o dashboard de {role}")  
            if role == "admin":
                page.go("/dashboard_admin")
            elif role == "agente":
                page.go("/dashboard_agente")
        else:
            print("Credenciais inválidas")
            page.snack_bar = ft.SnackBar(ft.Text("Credenciais inválidas!"))
            page.snack_bar.open = True
            page.update()

    username_input = ft.TextField(label="Usuário", width=300)
    password_input = ft.TextField(label="Senha", password=True, width=300)
    login_button = ft.ElevatedButton("Entrar", on_click=on_login, style=ESTILO_BOTAO_PRIMARIO)
    logo = exibir_logo(page.window_width)

    return ft.Column(
        controls=[
            ft.Row(
                controls=[logo],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            username_input,
            password_input,
            ft.Row(
                controls=[login_button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        **ALINHAMENTO_COLUNA,
    )
