import sqlite3

conn = sqlite3.connect("dados.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS atividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    tema TEXT,
    estrategia TEXT,
    resultado TEXT
)
""")

def salvar_atividade(titulo, tema, estrategia, resultado):
    cursor.execute("INSERT INTO atividades (titulo, tema, estrategia, resultado) VALUES (?, ?, ?, ?)",
                   (titulo, tema, estrategia, resultado))
    conn.commit()

def listar_atividades():
    cursor.execute("SELECT * FROM atividades")
    return cursor.fetchall()
