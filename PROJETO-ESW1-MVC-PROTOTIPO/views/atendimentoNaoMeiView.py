import flet as ft
from models.bancoDeDados import BancoDeDados
from .componente.identidadeVisual import ESTILO_BOTAO_PRIMARIO, ALINHAMENTO_COLUNA, ALINHAMENTO_LINHA

def AtendimentoNaoMeiView(page):
    banco = BancoDeDados()

    def salvar_atendimento(e):
        nome = nome_input.value
        cpf = cpf_input.value
        telefone = telefone_input.value
        email = email_input.value
        servico = servico_select.value
        cnpj = cnpj_input.value

        if not nome or not cpf or not servico:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha os campos obrigatórios!"))
            page.snack_bar.open = True
            page.update()
            return

        banco.salvar_atendimento(nome, cpf, cnpj, telefone, email, servico)
        page.snack_bar = ft.SnackBar(ft.Text("Atendimento salvo com sucesso!"))
        page.snack_bar.open = True
        page.go("/dashboard_agente")

    nome_input = ft.TextField(label="Nome", width=400)
    cpf_input = ft.TextField(label="CPF", width=400)
    telefone_input = ft.TextField(label="Telefone", width=400)
    email_input = ft.TextField(label="E-mail (opcional)", width=400)
    cnpj_input = ft.TextField(label="CNPJ (opcional)", width=400)

    servico_select = ft.Dropdown(
        label="Serviços",
        options=[
            ft.dropdown.Option("Dúvidas sobre MEI"),
            ft.dropdown.Option("Dúvidas sobre cursos do SEBRAE"),
            ft.dropdown.Option("Abrir MEI"),
        ],
        width=400,
    )

    salvar_button = ft.ElevatedButton(
        "Salvar atendimento", on_click=salvar_atendimento, style=ESTILO_BOTAO_PRIMARIO
    )
    voltar_button = ft.ElevatedButton(
        "Voltar", on_click=lambda e: page.go("/dashboard_agente"), style=ESTILO_BOTAO_PRIMARIO
    )

    return ft.Column(
        controls=[
            nome_input,
            cpf_input,
            telefone_input,
            email_input,
            cnpj_input,
            servico_select,
            ft.Row(
                controls=[salvar_button, voltar_button],
                **ALINHAMENTO_LINHA,
            ),
        ],
        **ALINHAMENTO_COLUNA,
    )
