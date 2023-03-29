from flask import Flask
from flask_restx import Api, Resource
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
api = Api(app, doc="/")
SECRET_KEY = os.getenv('SECRET_KEY')

@api.route('/all_hotels')
class Hotels(Resource):
    def get(self): 
        return {"message": 'Hotels'}

@api.route('/hotel_chain/<int:id>')
class Hotel_Chain(Resource): 
    def get(self, id): 
        return {"message": f"Getting hotel chain with id {id}"}

    def post(self, id): 
        return {"message":  f"Adding hotel chain with id {id}"}

    def delete(self, id): 
        return {"message":  f"Deleting hotel chain with id {id}"}

@api.route('/hotel_chain/all_hotels/<int:id>')
class Hotel_Chain(Resource): 
    def get(self, id): 
        return {"message": f"Getting all hotels associated with hotel chain {id}"}



@api.route('/hotel/<int:id>')
class Hotels(Resource): 
    def get(self, id): 
        return {"message": f"Getting hotel with id {id}"}

    def post(self, id): 
        return {"message":  f"Adding hotel with id {id}"}

    def delete(self, id): 
        return {"message":  f"Deleting hotel with id {id}"}

if __name__ == '__main__': 
    app.run(debug=True)