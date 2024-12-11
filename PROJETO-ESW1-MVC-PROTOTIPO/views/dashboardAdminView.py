import flet as ft
from .componente.identidadeVisual import ESTILO_BOTAO_PRIMARIO, ESTILO_BOTAO_SECUNDARIO, ALINHAMENTO_COLUNA, ALINHAMENTO_LINHA

def DashboardAdminView(page):
    def go_to_relatorio(e):
        page.go("/relatorio")

    def logout(e):
        page.go("/")

    botao_atendimentos = ft.ElevatedButton("Consultar Relatorio", on_click=go_to_relatorio, style=ESTILO_BOTAO_PRIMARIO)
    botao_logout = ft.ElevatedButton("Sair", on_click=logout, style=ESTILO_BOTAO_SECUNDARIO)

    return ft.Column(
        controls=[
            ft.Text("Dashboard", size=30, weight=ft.FontWeight.BOLD),
            ft.Row(
                controls=[
                    botao_atendimentos,
                ],
                **ALINHAMENTO_LINHA
            ),
            ft.Row(
                controls=[
                    botao_logout,
                ],
                **ALINHAMENTO_LINHA
            ),
        ],
        **ALINHAMENTO_COLUNA,
    )
