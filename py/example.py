import openpyxl
from sqlalchemy import create_engine

# Carregar a planilha do Excel
workbook = openpyxl.load_workbook("planilha.xlsx")

# Conectar ao banco de dados MySQL
engine = create_engine("mysql+pymysql://root:root@localhost:3306/auditoria")

# Acessar a primeira planilha
worksheet = workbook.active

# Obter os nomes das colunas
colunas = [cell.value for cell in worksheet[1]]

# Iterar pelas linhas da planilha
for row in worksheet.iter_rows(min_row=2):
    # Obter os valores das células
    valores = [cell.value for cell in row]

    # Criar um dicionário com os dados da linha
    dados = dict(zip(colunas, valores))

    # Inserir os dados no banco de dados
    engine.execute("INSERT INTO auditoria ({}) VALUES ({})".format(", ".join(colunas), ", ".join(["%s"] * len(colunas))), dados)

# Fechar a conexão com o banco de dados
engine.dispose()
