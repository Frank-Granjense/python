#!C:/Users/Administrator/AppData/Local/Programs/Python/Python310/python.exe
from assets import db 
            

print("Content-Type: text/html\n")
d = db.Db("country")
d.query("GovernmentForm", "=", "Republic", "OR")
d.query("Continent", "=", "Africa", "OR")
d.query("LifeExpectancy", "<", "45", "AND")
d.query_order("LifeExpectancy")
d.query_order("Name","DESC")
print(d.list())
#print(d.list())
