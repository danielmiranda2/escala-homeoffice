from flask import Flask, render_template, redirect, request, url_for, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Dados de exemplo dos usuários
users = {
    'admin': 'senha123'
}

# Dados de exemplo da escala de trabalho
schedule = [
    {"name": "João", "shift": "Manhã", "date": "2024-06-10"},
    {"name": "Maria", "shift": "Tarde", "date": "2024-06-11"},
    {"name": "Pedro", "shift": "Noite", "date": "2024-06-12"},
    {"name": "Ana", "shift": "Manhã", "date": "2024-06-13"},
    {"name": "Carlos", "shift": "Tarde", "date": "2024-06-14"},
    {"name": "Luiza", "shift": "Noite", "date": "2024-06-15"}
]

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('schedule'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('schedule'))
        else:
            flash('Nome de usuário ou senha inválidos.', 'error')
    return render_template('login.html')

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        date = request.form['date']
        shift = request.form['shift']
        name = request.form['name']

        # Verifica se a data já está ocupada
        if any(s['date'] == date for s in schedule):
            flash('Essa data já está ocupada.', 'error')
        else:
            # Atualiza a escala de trabalho
            schedule.append({"name": name, "shift": shift, "date": date})
            flash('A escala de trabalho foi atualizada.', 'success')

    return render_template('schedule.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
