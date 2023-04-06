from sqlalchemy.sql.expression import text
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import psycopg2
import datetime

load_dotenv()

# SETUP
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

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

    # Method checks whether a user exists and returns their role if they exist.
    def check_account_and_role(self, username, password): 
      query = self.cursor.execute(f"SELECT * FROM users WHERE username=(%s)", (username,))
      result = query.fetchall()
      if not result: 
        return ["Invalid Username"]
      hashed_pass = tuple[2]
      if check_password_hash(password, hashed_pass):
        user_type = result[3]
        return ["Found User", user_type]
    
    # Add methods here as we use them.
    def search(**kwargs): 
      pass

    def get_all_hotels(): 
      pass

    def get_hotel(id): 
      pass

    def get_all_hotel_chains(): 
      pass

    def get_hotel_chain(id): 
      pass


db = Database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

    


      

      


