from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from dotenv import load_dotenv
import os
import json

load_dotenv()
app = Flask(__name__)
api = Api(app, doc="/docs")
SECRET_KEY = os.getenv('SECRET_KEY')
app.config['SWAGGER_UI_REQUEST_HEADERS'] = {'Content-Type': 'application/json'}

# To specify schema of api payload.
input_model = api.model('InputModel', {
    'key': fields.String(required=True, description='Example key'),
})

@api.route('/all_hotels')
class Hotels(Resource):
    def get(self): 
        data = request.get_json()
        print(data)
        to_return = jsonify({"message": 'Hotels', "request": data})
        return to_return

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

@api.route('/hotel/search')
class HotelSearch(Resource): 
    def get(self): 
        data = request.get_json()
        return {"message": f"Searching for hotels with provided parameters"}

if __name__ == '__main__': 
    app.run(debug=True)