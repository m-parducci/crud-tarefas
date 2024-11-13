# CRUD de Tarefas

Este projeto é um sistema simples de CRUD (Create, Read, Update, Delete) para gerenciamento de tarefas. Ele permite que o usuário adicione, visualize, edite e exclua tarefas. O sistema foi desenvolvido utilizando Python (Flask), PostgreeSQL, HTML e CSS para o front-end.

## Funcionalidades

- **Adicionar Tarefa**: Permite ao usuário inserir uma nova tarefa com título e descrição.
- **Visualizar Tarefas**: Exibe todas as tarefas cadastradas.
- **Editar Tarefa**: Permite editar o título e a descrição de uma tarefa existente.
- **Excluir Tarefa**: Permite excluir uma tarefa da lista.

## Tecnologias Utilizadas

- **Back-end**: Python, Flask
- **Banco de Dados**: SQLite (ou outro de sua escolha)
- **Front-end**: HTML, CSS
- **Controle de versão**: Git

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/m-parducci/crud-tarefas.git
cd crud-tarefas
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

2. Crie um ambiente virtual:
Se você ainda não tem um ambiente virtual configurado, crie um utilizando o seguinte comando:
```
python -m venv venv
```
3. Ative o ambiente virtual:
- Windows
  ```
  .\venv\Scripts\activate
  ```
- Mac/Linux:
```
source venv/bin/activate

```
4. Instale as dependências:
```
pip install -r requirements.txt

``` 
Configure as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto e adicione suas variáveis de ambiente (como configurações do banco de dados, chaves secretas, etc.). Exemplo:
``` 
SECRET_KEY=seu_valor_secreto
DATABASE_URL=sqlite:///db.sqlite3
``` 
Execute:
```
python app.py
```
O servidor Flask será iniciado e você poderá acessar o aplicativo no navegador, geralmente em http://127.0.0.1:5000/.
