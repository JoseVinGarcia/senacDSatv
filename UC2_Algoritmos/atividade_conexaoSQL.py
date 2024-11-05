# ATIVIDADE - Integração SQL com Python (VERSÃO MODIFICADA)

# Importando biblioteca
from sqlalchemy import create_engine, text
import os

# Variaveis de conexao com o banco
host = "localhost"
user = "root"
password = "root"
roots = 0

# Função pra conectar o banco
def conecta_banco(b,c):
    try:
        # URL de conexão com o banco, usando SQLAlchemy e PyMySQL
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{b}")

        # Estabelece a conexão
        with engine.connect() as conexao:
            # Query: "Linguagem SQL para selecionar todos os registros da tabela produtos"
            query = c

            # "text(query)" transforma a string da query em um objeto compatível com SQLAlchemy
            # "conexao.execute" executa essa consulta no banco de dados.
            resultados = conexao.execute(text(query))

            for item in resultados:
                print(item[0], item[1], item[2])

    except ImportError as e:
        print(f"Erro: {e}")
    
# Começo do código
os.system("cls")
print("="*30)
print("SQL EXAMINADOR ~~ Por José Vinícius")

bd = input("\n     Digite o nome da base de dados: ")
cd = input("     Agora digite seu comando: ")

# # Chama função que conecta ao banco de dados
# conecta_banco(bd,cd)

while roots==0:
    conecta_banco(bd,cd)
    cmd = input("     Deseja realizar outro comando? S/N: ").upper()
    if cmd == "S":
        cd = input("     Agora digite seu comando: ")
    else:
        roots=1

print("Até mais!")
