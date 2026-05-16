from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# =========================
# CRIAR BANCO AUTOMATICAMENTE
# =========================

def criar_banco():

    conexao = sqlite3.connect('banco.db')

    cursor = conexao.cursor()

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS pecas (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT,
            nome TEXT,
            categoria TEXT,
            quantidade INTEGER,
            minimo INTEGER,
            valor REAL,
            fornecedor TEXT

        )

    ''')

    conexao.commit()
    conexao.close()

# =========================
# ROTAS
# =========================

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

# =========================
# INICIAR SISTEMA
# =========================

if __name__ == '__main__':

    criar_banco()

    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
