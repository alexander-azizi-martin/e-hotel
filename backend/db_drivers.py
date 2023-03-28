from sqlalchemy.sql.expression import text
from werkzeug.security import generate_password_hash, check_password_hash
import os
import psycopg2
import datetime

# SETUP
secret_key = os.environ.get('SECRET_KEY')
debug = os.environ.get('DEBUG')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
BASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# We need an object oriented way to connect to and communicate with the database.
class Database(object): 
    # Constructor to make a connection to the database and return an object to execute queries with.
    def __init__(self, dbname, user, password, host, port):
        self.connection = psycopg2.connect(dbname = dbname, user = user, password = password, host = host, port = port)
        self.cursor = self.connection.cursor()

    # Methods to close connection and commit changes to the database.
    def close(self):
      self.connection.close()

    def commit(self):
      self.connection.commit()
    
    # Action methods on the database.

    # Method checks whether a user exists and returns 
    # their role if they exist.
    def check_account_and_role(self, username, password): 
      query = self.cursor.execute(f"SELECT * FROM users WHERE username=(%s)", (username,))
      result = query.fetchall()
      if not result: 
        return ["Invalid Username"]
      hashed_pass = tuple[2]
      if check_password_hash(password, hashed_pass):
        user_type = "Customer" if result[3] is None else "Employee"
        return ["Found User", user_type]
    
    # Add methods here as we use them.
    

    


      

      


