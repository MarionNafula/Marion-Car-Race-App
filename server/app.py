from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_migrate import Migrate
from models import db, Driver, Circuit, Stat
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Resources
class DriverResource(Resource):
    def get(self):
        return [driver.to_dict() for driver in Driver.query.all()], 200

    def post(self):
        data = request.json
        new_driver = Driver(**data)
        db.session.add(new_driver)
        db.session.commit()
        return new_driver.to_dict(), 201

class CircuitResource(Resource):
    def get(self):
        return [circuit.to_dict() for circuit in Circuit.query.all()], 200

    def post(self):
        data = request.json
        new_circuit = Circuit(**data)
        db.session.add(new_circuit)
        db.session.commit()
        return new_circuit.to_dict(), 201

class StatResource(Resource):
    def get(self):
        return [stat.to_dict() for stat in Stat.query.all()], 200

    def post(self):
        data = request.json
        new_stat = Stat(**data)
        db.session.add(new_stat)
        db.session.commit()
        return new_stat.to_dict(), 201

# Add routes
api.add_resource(DriverResource, '/drivers')
api.add_resource(CircuitResource, '/circuits')
api.add_resource(StatResource, '/stats')

if __name__ == '__main__':
    app.run(debug=True)
