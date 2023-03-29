from flask import Flask
from flask_restx import Api, Resource
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
api = Api(app, doc="/docs")
SECRET_KEY = os.getenv('SECRET_KEY')

@api.route('/hello')
class HelloWorld(Resource): 
    def get(self): 
        return {"message": "Hello World"}




if __name__ == '__main__': 
    app.run()