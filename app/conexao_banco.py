import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error

load_dotenv()

senha =os.getenv("senha")

def conecta_banco():
    try:
        conn = psycopg2.connect(
            user="postgres",
            password= senha,
            host="localhost",
            port="5432",
            database="db_biblioteca")
        
        print("<< Banco de dados CONECTADO >>")

        return conn
    except Error as e:
        print(f"Ocorreu um erro ao tentar conectar ao banco de dados: {e}")   

def encerra_conexao(conn):
    if conn:
        conn.close()
        print("<< Conexão com o banco ENCERRADA >>")


