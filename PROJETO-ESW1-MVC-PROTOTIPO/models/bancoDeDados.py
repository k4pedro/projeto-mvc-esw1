import sqlite3
from .usuario import Usuario
from .atendimento import Atendimento

class BancoDeDados:
    def __init__(self):
        self.conexao = sqlite3.connect("banco_de_dados.db", check_same_thread=False)
        self.usuario_model = Usuario(self.conexao)
        self.atendimento_model = Atendimento(self.conexao)
        self.usuario_model.criar_tabela()
        self.atendimento_model.criar_tabela()
        self.usuario_model.criar_usuarios_padrao()

    def salvar_usuario(self, username, senha, role):
        self.usuario_model.cursor.execute("""
            INSERT INTO usuarios (username, senha, role) VALUES (?, ?, ?)
        """, (username, senha, role))
        self.conexao.commit()   

    def salvar_atendimento(self, nome, cpf, cnpj, telefone, email, servico, parcelas=None):
        self.atendimento_model.salvar(nome, cpf, cnpj, telefone, email, servico, parcelas)

    def consultar_atendimentos(self, cpf_ou_cnpj):
        return self.atendimento_model.consultar(cpf_ou_cnpj)
    
    def consultar_atendimentos_por_periodo(self, data_inicio, data_fim):
        return self.atendimento_model.consultar_por_periodo(data_inicio, data_fim)

    def fechar_conexao(self):
        self.conexao.close()
