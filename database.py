import psycopg2
from psycopg2 import sql, Error
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configura as variáveis de ambiente
DATABASE_CONFIG = {
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "taskdb")
}

# Função genérica para obter conexão
def get_connection():
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Gerenciador de contexto para o cursor do banco de dados
class DatabaseConnection:
    def __enter__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
            print(f"Erro ao executar operação: {exc_val}")
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()

# Função para criar uma tabela, caso não exista
def create_table(table_name):
    with DatabaseConnection() as cur:
        query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS {table} (
                id SERIAL PRIMARY KEY,
                titulo VARCHAR(100) NOT NULL,
                descricao VARCHAR(100)
            );
        """).format(table=sql.Identifier(table_name))
        cur.execute(query)
        print(f"Tabela '{table_name}' verificada/criada com sucesso.")

# Função para inserir um registro
def insert_task(titulo, descricao, table="tasks"):
    with DatabaseConnection() as cur:
        query = sql.SQL("INSERT INTO {table} (titulo, descricao) VALUES (%s, %s)").format(
            table=sql.Identifier(table))
        cur.execute(query, (titulo, descricao))
        print("Tarefa inserida com sucesso.")

# Função para obter todos os registros
def fetch_all_tasks(table="tasks"):
    with DatabaseConnection() as cur:
        query = sql.SQL("SELECT * FROM {table}").format(table=sql.Identifier(table))
        cur.execute(query)
        return cur.fetchall()

# Função para excluir uma tarefa pelo ID
def delete_task(task_id, table="tasks"):
    with DatabaseConnection() as cur:
        query = sql.SQL("DELETE FROM {table} WHERE id = %s").format(table=sql.Identifier(table))
        cur.execute(query, (task_id,))
        print(f"Tarefa com ID {task_id} excluída com sucesso.")

#Função para atualizar um dado da tabela pelo ID
def update_task(task_id, titulo, descricao, table="tasks"):
    with DatabaseConnection() as cur:
        query = sql.SQL("UPDATE {table} SET titulo = %s, descricao = %s WHERE id = %s").format(table=sql.Identifier(table))
        cur.execute(query, (titulo, descricao, task_id))
        print(f"Item da tabela {task_id} alterado com sucesso")