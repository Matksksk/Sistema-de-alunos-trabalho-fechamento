import sqlite3 as sq

conexao = sq.connect("alunos.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
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

cursor.execute("""
CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER NOT NULL UNIQUE,
    nota1 REAL NOT NULL,
    nota2 REAL NOT NULL,
    nota3 REAL NOT NULL,
    nota4 REAL NOT NULL,
    media REAL NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
)
""")
conexao.commit()
conexao.close()


def cadastrar_usuario(usuario, senha):
    conexao = sq.connect("alunos.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
    conexao.commit()
    conexao.close()


def cadastrar_aluno(nome, rm, turma):
    conexao = sq.connect("alunos.db")
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id FROM alunos WHERE rm = ?",
        (rm,)
    )
    aluno=cursor.fetchone()
    if aluno:
        conexao.close()
        return False
    cursor.execute("INSERT INTO alunos (nome, rm, turma) VALUES (?, ?, ?)", (nome, rm, turma))
    conexao.commit()
    conexao.close()
    return True


def listar_alunos():
    conexao = sq.connect("alunos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, rm, turma FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()
    return alunos


def guardar_notas(aluno_id, nota1, nota2, nota3, nota4,media):
    conexao = sq.connect("alunos.db")
    cursor = conexao.cursor()
    media = (nota1 + nota2 + nota3 + nota4) / 4
    cursor.execute(
        "INSERT INTO notas (aluno_id, nota1, nota2, nota3, nota4, media) VALUES (?, ?, ?, ?, ?, ?)",
        (aluno_id, nota1, nota2, nota3, nota4, media)
    )
    conexao.commit()
    conexao.close()


def listar_notas():
    conexao = sq.connect("alunos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT aluno_id, nota1, nota2, nota3, nota4, media FROM notas")
    linhas = cursor.fetchall()
    conexao.close()
    notas = {}
    for linha in linhas:
        notas[linha[0]] = linha[1:]
    return notas


def guardar_notas_lote(notas_por_aluno):
    conexao = sq.connect("alunos.db")
    try:
        cursor = conexao.cursor()
        for aluno_id, (nota1, nota2, nota3, nota4) in notas_por_aluno.items():
            media = (nota1 + nota2 + nota3 + nota4) / 4
            cursor.execute(
                """
                INSERT INTO notas (aluno_id, nota1, nota2, nota3, nota4, media)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(aluno_id) DO UPDATE SET
                    nota1 = excluded.nota1,
                    nota2 = excluded.nota2,
                    nota3 = excluded.nota3,
                    nota4 = excluded.nota4,
                    media = excluded.media
                """,
                (aluno_id, nota1, nota2, nota3, nota4, media)
            )
        conexao.commit()
    except Exception:
        conexao.rollback()
        raise
    finally:
        conexao.close()


def pesquisar_alunos(nome=None, rm=None):
    conexao = sq.connect("alunos.db")
    cursor = conexao.cursor()

    if rm:
        cursor.execute(
            "SELECT * FROM alunos WHERE rm = ?",
            (rm,)
        )

    elif nome:
        cursor.execute(
            "SELECT * FROM alunos WHERE UPPER(nome) LIKE UPPER(?)",
            (f"%{nome}%",)
        )
    else:
        conexao.close()
        return "Aluno não encontrado"
    
    aluno = cursor.fetchone()
    conexao.close()

    if aluno:
        return aluno
    else:
        return "Aluno não encontrado"