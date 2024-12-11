import flet as ft
from .componente.identidadeVisual import ESTILO_BOTAO_PRIMARIO, ESTILO_BOTAO_SECUNDARIO, ALINHAMENTO_COLUNA

def DashboardAgenteView(page):
    def meu_mei_click(e):
        print("Iniciando processo de MEI")
        page.go("/atendimento_mei")


    def quero_ser_mei_click(e):
        print("Processo para MEI")
        page.go("/atendimento_nao_mei")

    def consultar_atendimento_click(e):
        print("Consultando atendimento")
        page.go("/consulta_atendimento")

    def sair_click(e):
        print("Saindo...")
        page.go("/")

    return ft.Column(
        controls=[
            ft.Text("Bem vindo - Agente Sebrae", size=30),
            ft.ElevatedButton(
                "1. MEI", 
                on_click=meu_mei_click,
                style=ESTILO_BOTAO_PRIMARIO
            ),
            ft.ElevatedButton(
                "2. Quero ser MEI", 
                on_click=quero_ser_mei_click,
                style=ESTILO_BOTAO_PRIMARIO
            ),
            ft.ElevatedButton(
                "3. Consultar Atendimento", 
                on_click=consultar_atendimento_click,
                style=ESTILO_BOTAO_PRIMARIO
            ),
            ft.ElevatedButton(
                "Sair", 
                on_click=sair_click,
                style=ESTILO_BOTAO_SECUNDARIO
            ),
        ],
        **ALINHAMENTO_COLUNA,
    )