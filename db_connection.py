import psycopg2

# Interacting with the database in an object oriented manner. Creating a 
# class to ensure that a connection state is stored and any required 
# and supporting method, such as close and commit are encapsulated.
class DBConnection:
  def __init__(self, dbname, user, password, host, port, schema):
    self.connection = psycopg2.connect(dbname = dbname, user = user, password = password, host = host, port = port)
    self.cursor = self.connection.cursor()
  
  def close(self):
    self.connection.close()

  def commit(self):
    self.connection.commit()

# To create a new connection to a database.
def newConnection(dbname, user, password, host, port, schema):
  connection = DBConnection(dbname, user, password, host, port, schema)
  return connection