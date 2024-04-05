import os
import openpyxl
from sqlalchemy import create_engine

archive = os.path.abspath("./Auditoria ISO 17799.xlsx")
workbook = openpyxl.load_workbook(archive)
engine = create_engine("mysql+pymysql://root:root@localhost:3306/auditoria")
worksheet = workbook.active

coluns = [cell.value for cell in worksheet[1]]

print(coluns)
