import pyodbc

# Configuração dos parâmetros de conexão
server = 'CPP-077\SQLEXPRESS'  # substitua 'localhost\SQLEXPRESS' pelo nome do servidor do seu SQL Server Express
database = 'CARGACOMPLETA'  # substitua 'NomeDoSeuBancoDeDados' pelo nome do seu banco de dados
username = 'sa'  # substitua 'seu_usuario' pelo nome de usuário do banco de dados
password = '22062011'  # substitua 'sua_senha' pela senha do banco de dados

# String de conexão
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Estabelecendo a conexão
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Exemplo de execução de uma consulta
    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    print(f"Conexão bem-sucedida! Versão do SQL Server: {row[0]}")

    # Fechando a conexão
    conn.close()

except pyodbc.Error as e:
    print(f"Erro ao conectar ao SQL Server: {e}")