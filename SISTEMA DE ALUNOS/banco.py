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
        rm INT NOT NULL UNIQUE,
        turma VARCHAR(3) NOT NULL
    )
""")


banco.commit()
banco.close()


def cadastrar_usuario(usuario, senha):
    conexao = sq.connect("alunos.db")
    banco = conexao
    cursor = banco.cursor()

    cursor.execute("""
        INSERT INTO usuarios (usuario, senha)
        VALUES (?, ?)
    """, (usuario, senha))

    banco.commit()
    banco.close()

    banco.close()
def cadastrar_aluno(nome, rm, turma):
    conexao = sq.connect("alunos.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO alunos (nome, rm, turma)
        VALUES (?, ?, ?)
    """, (nome, rm, turma))

    conexao.commit()
    conexao.close()