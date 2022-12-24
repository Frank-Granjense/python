import mysql.connector

# Publicada em https://github.com/Frank-Granjense/python-mysql/, versão 0.1 (dez/2022)
# Classe em python projetada por Frank Granjense (Discord: frank.sp#8171) e Dinho King (Discord: DinhoKing#2000)
# PS: Este código é Open Source, você pode editar a vontade, fazendo favor citar os nossos nomes e/ou github.
# Nosso whatsapp comercial para contato: +55(11)91269-3318

class Db:
      # Dados para acesso ao banco de dados. Edite só esta parte aqui!
      dbuser = "root"
      dbpass = ""
      dbhost = "127.0.0.1"
      dbbase = "world"

      # Váriáveis do sistema, só mexa a partir daqui se quiser modificar esta classe
      dbtable = ""
      queries_and = []
      queries_or = []
      queries_order = []

      # Função que carrega automaticamente ao chamar esta classe
      def __init__(self, table = ""):
            if(table != ""):
                  self.dbtable = table

      # Função para conectar ao mySql
      def connect(self):
            self.access = mysql.connector.connect(    user=self.dbuser, 
                                                      password=self.dbpass, 
                                                      host=self.dbhost, 
                                                      database=self.dbbase
                                                )

      # Função que lista a busca
      def list(self, query = ""):
            #WHERE AND
            if(len(self.queries_and) > 0):
                  for i in range(len(self.queries_and)):
                        if(query != ""):
                              query += " AND "
                        query += self.queries_and[i]
            #WHERE OR
            if(len(self.queries_or) > 0):
                  query_or = ""
                  for i in range(len(self.queries_or)):
                        if(query_or != ""):
                              query_or += " OR "
                        query_or += self.queries_or[i]
                  query_or = "(" + query_or + ")"
                  if(query != ""):
                        query += " AND " + query_or
            #WHERE se não estiver vazio
            if(query != ""):
                  query = "WHERE " + query
            #ORDER se não estiver vazio
            order = ""
            for i in range(len(self.queries_order)):
                  if(order != ""):
                        order += ", "
                  order += self.queries_order[i]
            query += " ORDER BY " + order
            #conectando ao mySql
            if(self.dbtable != ""):
                  self.connect()
                  cursor = self.access.cursor()
                  cursor.execute("SELECT * FROM {0} {1}".format(self.dbtable, query))
                  result = cursor.fetchall()
            else:
                  result = "Error: table not defined"
            return result

      # Função que adiciona os comandos para a busca
      def query(self, col, sel, value, param = ""):
            q = self.queries_and
            if(param == "OR" or param == "or"):
                  q = self.queries_or
            q.append("`" + col + "` " + sel + " '" + value + "'")

      # Função que adiciona como a busca será ordenada
      def query_order(self, col, order = "ASC"):
            self.queries_order.append("`" + col + "` " + order)
           