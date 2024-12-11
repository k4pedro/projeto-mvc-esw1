import flet as ft
from models.bancoDeDados import BancoDeDados
from .componente.identidadeVisual import ESTILO_BOTAO_PRIMARIO, ALINHAMENTO_COLUNA

def AtendimentoMeiView(page):
    banco = BancoDeDados()

    def salvar_atendimento(e):
        nome = nome_input.value
        cpf = cpf_input.value
        cnpj = cnpj_input.value
        telefone = telefone_input.value
        email = email_input.value
        servico = servico_select.value
        parcelas = parcelas_input.value if servico == "Emitir boleto de parcelamento" else None

        if not nome or not cpf or not servico:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha os campos obrigatórios!"))
            page.snack_bar.open = True
            page.update()
            return

        banco.salvar_atendimento(nome, cpf, cnpj, telefone, email, servico, parcelas)
        page.snack_bar = ft.SnackBar(ft.Text("Atendimento salvo com sucesso!"))
        page.snack_bar.open = True
        page.go("/dashboard_agente")

    nome_input = ft.TextField(label="Nome", width=400)
    cpf_input = ft.TextField(label="CPF", width=400)
    cnpj_input = ft.TextField(label="CNPJ (opcional)", width=400)
    telefone_input = ft.TextField(label="Telefone", width=400)
    email_input = ft.TextField(label="E-mail (opcional)", width=400)

    servico_select = ft.Dropdown(
        label="Serviços",
        options=[
            ft.dropdown.Option("Emitir boleto simples"),
            ft.dropdown.Option("Emitir boleto de parcelamento"),
            ft.dropdown.Option("Alterar informações"),
            ft.dropdown.Option("Emitir certificado"),
            ft.dropdown.Option("Informações sobre nota fiscal"),
            ft.dropdown.Option("Baixar MEI"),
        ],
        width=400,
    )

    parcelas_input = ft.TextField(label="Número de parcelas", width=400, visible=False)

    def atualizar_parcelas_visibilidade(e):
        parcelas_input.visible = servico_select.value == "Emitir boleto de parcelamento"
        page.update()

    servico_select.on_change = atualizar_parcelas_visibilidade

    salvar_button = ft.ElevatedButton(
        "Salvar Atendimento", on_click=salvar_atendimento, style=ESTILO_BOTAO_PRIMARIO
    )
    voltar_button = ft.ElevatedButton(
        "Voltar", on_click=lambda e: page.go("/dashboard_agente"), style=ESTILO_BOTAO_PRIMARIO
    )

    return ft.Column(
        controls=[
            nome_input,
            cpf_input,
            cnpj_input,
            telefone_input,
            email_input,
            servico_select,
            parcelas_input,
            ft.Row(
                controls=[salvar_button, voltar_button],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        **ALINHAMENTO_COLUNA,
    )
