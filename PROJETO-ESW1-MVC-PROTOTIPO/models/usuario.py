import sqlite3

class Usuario:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
    
    def criar_tabela(self):
        try:
            print("Tentando criar tabela 'usuarios'...")
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                senha TEXT,
                role TEXT
            )
            """)
            self.conexao.commit()
            print("Tabela 'usuarios' criada ou já existente.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela 'usuarios': {e}")
    
    def criar_usuarios_padrao(self):
        self.cursor.execute("SELECT * FROM usuarios WHERE username = ?", ("admin",))
        if not self.cursor.fetchone():
            self.cursor.execute("INSERT INTO usuarios (username, senha, role) VALUES (?, ?, ?)", ("admin", "123", "admin"))
        
        self.cursor.execute("SELECT * FROM usuarios WHERE username = ?", ("agente",))
        if not self.cursor.fetchone():
            self.cursor.execute("INSERT INTO usuarios (username, senha, role) VALUES (?, ?, ?)", ("agente", "456", "agente"))
        
        self.conexao.commit()

    def validar_credenciais(self, username, senha):
        self.cursor.execute("SELECT role FROM usuarios WHERE username = ? AND senha = ?", (username, senha))
        usuario = self.cursor.fetchone()

        if usuario:
            print(f"Usuário {username} encontrado, role: {usuario[0]}")
            return usuario[0]
        else:
            print(f"Credenciais inválidas para o usuário {username}")
        return None
