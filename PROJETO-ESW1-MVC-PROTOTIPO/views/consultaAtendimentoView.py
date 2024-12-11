import flet as ft
from models.bancoDeDados import BancoDeDados
from .componente.identidadeVisual import ESTILO_BOTAO_PRIMARIO, ALINHAMENTO_COLUNA, ALINHAMENTO_LINHA

def ConsultaAtendimentoView(page):
    banco = BancoDeDados()

    def consultar_atendimentos(e):
        filtro = filtro_select.value
        valor = valor_input.value.strip()

        if not filtro or not valor:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha o filtro e o valor!"))
            page.snack_bar.open = True
            page.update()
            return

        resultados = banco.consultar_atendimentos(valor)

        resultado_list.controls.clear()
        if not resultados:
            page.snack_bar = ft.SnackBar(ft.Text("Nenhum atendimento encontrado."))
            page.snack_bar.open = True
        else:
            for atendimento in resultados:
                resultado_list.controls.append(
                    ft.Text(f"{atendimento['data']} - {atendimento['servico']} - {atendimento['nome']}")
                )
        page.update()

    # Função para limpar os campos
    def limpar_campos(e):
        filtro_select.value = None
        valor_input.value = ""
        resultado_list.controls.clear()
        page.snack_bar = ft.SnackBar(ft.Text("Campos limpos!"))
        page.snack_bar.open = True
        page.update()

    # Campos de entrada e seleção
    filtro_select = ft.Dropdown(
        label="Consultar via",
        options=[ft.dropdown.Option("CPF"), ft.dropdown.Option("CNPJ")],
        width=400,
    )
    valor_input = ft.TextField(label="Digite o valor (CPF ou CNPJ)", width=400)

    # Botões de consulta e limpar (usando estilos)
    consultar_button = ft.ElevatedButton(
        "Consultar", on_click=consultar_atendimentos, style=ESTILO_BOTAO_PRIMARIO
    )
    limpar_button = ft.ElevatedButton(
        "Limpar", on_click=limpar_campos, style=ESTILO_BOTAO_PRIMARIO
    )

    # Área de resultados
    resultado_list = ft.ListView(expand=True)

    # Botão de voltar
    voltar_button = ft.ElevatedButton(
        "Voltar", on_click=lambda e: page.go("/dashboard_agente"), style=ESTILO_BOTAO_PRIMARIO
    )

    # Layout da view (usando alinhamento)
    return ft.Column(
        controls=[
            ft.Row(
                controls=[ft.Text("Consulta de Atendimentos", size=20, weight=ft.FontWeight.BOLD)],
                **ALINHAMENTO_LINHA,
            ),
            filtro_select,
            valor_input,
            ft.Row(
                controls=[consultar_button, limpar_button],
                **ALINHAMENTO_LINHA,
            ),
            ft.Row(
                controls=[voltar_button],
                **ALINHAMENTO_LINHA,
            ),
            ft.Row(
                controls=[resultado_list],
                **ALINHAMENTO_LINHA,
            ),
        ],
        **ALINHAMENTO_COLUNA,
    )
