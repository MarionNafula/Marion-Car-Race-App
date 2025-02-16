from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Driver(db.Model, SerializerMixin):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(100), nullable=False)
    stats = db.relationship('Stat', back_populates='driver')

class Circuit(db.Model, SerializerMixin):
    __tablename__ = 'circuits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Float, nullable=False)
    stats = db.relationship('Stat', back_populates='circuit')

class Stat(db.Model, SerializerMixin):
    __tablename__ = 'stats'
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
    circuit_id = db.Column(db.Integer, db.ForeignKey('circuits.id'), nullable=False)
    best_lap_time = db.Column(db.Float, nullable=False)

    driver = db.relationship('Driver', back_populates='stats')
    circuit = db.relationship('Circuit', back_populates='stats')