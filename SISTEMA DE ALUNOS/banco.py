import sqlite3 as sq

conexao = sq.connect("alunos.db")
banco = conexao
cursor = banco.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ra TEXT NOT NULL UNIQUE,
        nota1 REAL,
        nota2 REAL
    )
""")
banco.commit()
banco.close()