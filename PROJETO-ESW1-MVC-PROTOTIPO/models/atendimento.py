import sqlite3

class Atendimento:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
    
    def criar_tabela(self):
        try:
            print("Tentando criar tabela 'atendimentos'...")
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS atendimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                cnpj TEXT,
                telefone TEXT NOT NULL,
                email TEXT,
                servico TEXT NOT NULL,
                parcelas INTEGER,
                time_data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            self.conexao.commit()
            print("Tabela 'atendimentos' criada ou já existente.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela 'atendimentos': {e}")
    
    def salvar(self, nome, cpf, cnpj, telefone, email, servico, parcelas=None):
        self.cursor.execute("""
            INSERT INTO atendimentos (nome, cpf, cnpj, telefone, email, servico, parcelas)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (nome, cpf, cnpj, telefone, email, servico, parcelas))
        self.conexao.commit()

    def consultar(self, cpf_ou_cnpj):
        resultados = []
        self.cursor.execute("""
            SELECT id, nome, cpf, cnpj, telefone, email, servico, time_data
            FROM atendimentos
            WHERE cpf = ? OR cnpj = ?
        """, (cpf_ou_cnpj, cpf_ou_cnpj))
        atendimentos = self.cursor.fetchall()

        for atendimento in atendimentos:
            resultados.append({
                "id": atendimento[0],
                "nome": atendimento[1],
                "cpf": atendimento[2],
                "cnpj": atendimento[3],
                "telefone": atendimento[4],
                "email": atendimento[5],
                "servico": atendimento[6],
                "data": atendimento[7]
            })
        return resultados
    
    def consultar_por_periodo(self, data_inicio, data_fim):
        resultados = []
        self.cursor.execute("""
            SELECT id,- nome, cpf, cnpj, telefone, email, servico, time_data
            FROM atendimentos
            WHERE time_data BETWEEN ? AND ?
        """, (data_inicio, data_fim))
        atendimentos = self.cursor.fetchall()

        for atendimento in atendimentos:
            resultados.append({
                "id": atendimento[0],
                "nome": atendimento[1],
                "cpf": atendimento[2],
                "cnpj": atendimento[3],
                "telefone": atendimento[4],
                "email": atendimento[5],
                "servico": atendimento[6],
                "data": atendimento[7]
            })
        return resultados