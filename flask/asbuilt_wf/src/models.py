from datetime import datetime
from xmlrpc.client import DateTime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships


class Asbuilt(db.Model):
    __tablename__ = 'asbuilts'
    pk_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    work_order = db.Column(db.String(128), unique=False, nullable=False)
    install_date = db.Column(db.DateTime, nullable=False)
    crew_leader_id = db.Column(
        db.Integer, db.ForeignKey('crew_leaders.pk_id'), nullable=False)
    gis_user_id = db.Column(
        db.Integer, db.ForeignKey('gis_users.pk_id'), nullable=False)

    def __init__(self, work_order: str, crew_leader_id: int, gis_user_id: int, install_date: datetime):
        self.work_order = work_order
        self.crew_leader_id = crew_leader_id
        self.gis_user_id = gis_user_id
        self.install_date = install_date

    def serialize(self, gis_name, cl_name):
        return {
            'id': self.pk_id,
            'work order': self.work_order,
            'install date': self.install_date.isoformat(),
            'gis user': gis_name,
            'crew leader': cl_name
        }


class Gis_user(db.Model):
    __tablename__ = 'gis_users'
    pk_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


class Crew_leader(db.Model):
    __tablename__ = 'crew_leaders'
    pk_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
