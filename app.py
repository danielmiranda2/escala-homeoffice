from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo da escala de trabalho
schedule = [
    {"name": "João", "shift": "Manhã"},
    {"name": "Maria", "shift": "Tarde"},
    {"name": "Pedro", "shift": "Noite"},
    {"name": "Ana", "shift": "Manhã"},
    {"name": "Carlos", "shift": "Tarde"},
    {"name": "Luiza", "shift": "Noite"}
]

@app.route("/")
def index():
    return render_template("index.html", schedule=schedule)

if __name__ == "__main__":
    app.run(debug=True)
