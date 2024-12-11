import flet as ft
from models.bancoDeDados import BancoDeDados
from .componente.identidadeVisual import ALINHAMENTO_COLUNA, ALINHAMENTO_LINHA, ESTILO_BOTAO_PRIMARIO, ESTILO_BOTAO_SECUNDARIO

def RelatorioView(page):
    banco = BancoDeDados() 

    def buscar_relatorio(e):
        data = data_input.value.strip()

        if not data:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha a data!"))
            page.snack_bar.open = True
            page.update()
            return

        data_inicio = f"{data} 00:00:00"
        data_fim = f"{data} 23:59:59"

        atendimentos = banco.consultar_atendimentos_por_periodo(data_inicio, data_fim)

        if not atendimentos:
            page.snack_bar = ft.SnackBar(ft.Text("Nenhum atendimento encontrado na data informada!"))
            page.snack_bar.open = True
            relatorio_list.controls.clear()
        else:
            relatorio_list.controls.clear()
            for atendimento in atendimentos:
                relatorio_list.controls.append(
                    ft.Text(
                        f"{atendimento['data']} - {atendimento['nome']} - {atendimento['servico']}",
                        size=16,
                    )
                )
        page.update()

    def voltar(e):
        page.go("/dashboard_admin")

    botao_voltar = ft.ElevatedButton("Voltar", on_click=voltar, style=ESTILO_BOTAO_SECUNDARIO)
    data_input = ft.TextField(label="Data (YYYY-MM-DD)", width=300)
    buscar_button = ft.ElevatedButton("Buscar Relatório", on_click=buscar_relatorio, style=ESTILO_BOTAO_PRIMARIO)
    relatorio_list = ft.ListView(expand=True)

    return ft.Column(
        controls=[
            ft.Text("Relatórios de Atendimentos", size=20, weight=ft.FontWeight.BOLD),
            ft.Row(controls=[data_input], **ALINHAMENTO_LINHA),
            ft.Row(controls=[buscar_button], **ALINHAMENTO_LINHA),
            ft.Row(controls=[botao_voltar], **ALINHAMENTO_LINHA),
            ft.Container(content=relatorio_list, expand=True),
        ],
        **ALINHAMENTO_COLUNA,
    )
