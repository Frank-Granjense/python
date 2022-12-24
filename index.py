#!C:/Users/Administrator/AppData/Local/Programs/Python/Python310/python.exe
from assets import db 

print("Content-Type: text/html\n")
d = db.Db("tabela")

d.query("campo1", "=", "busca1", "AND")
d.query("campo2", "=", "busca2", "AND")
d.query("campo3", "<", "3", "OR")
d.query_order("campo1", "ASC")
d.query_order("campo3", "DESC")
print(d.list())
