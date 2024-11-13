from flask import Flask, render_template, request, redirect, url_for
from database import create_table, insert_task, fetch_all_tasks, delete_task, update_task

app = Flask(__name__)

# Cria a tabela 'tasks' ao iniciar a aplicação
create_table("tasks")

@app.route('/')
def index():
    data = fetch_all_tasks()
    return render_template('index.html', data=data)

@app.route('/create', methods=['POST'])
def create():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    insert_task(titulo, descricao)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    id_tarefa = request.form['id']
    delete_task(id_tarefa)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    id_tarefa = request.form['id']
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    update_task(id_tarefa, titulo, descricao)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)
