import re
from flask import Blueprint, jsonify, abort, request
from ..models import Asbuilt, Crew_leader, Gis_user, db

bp = Blueprint('asbuilts', __name__, url_prefix='/asbuilts')


def gis(id):
    g = (Gis_user.query.get_or_404((Asbuilt.query.get_or_404(id)).gis_user_id)).name
    return g


def crew(id):
    c = (Crew_leader.query.get_or_404(
        (Asbuilt.query.get_or_404(id)).crew_leader_id)).name
    return c


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    asbuilts = Asbuilt.query.all()  # ORM performs SELECT query

    result = []
    for a in asbuilts:

        # build list of asbuilts as dictionaries
        result.append(a.serialize(gis(a.gis_user_id), crew(a.crew_leader_id)))
    return jsonify(result)  # return JSON response


@bp.route('', methods=['POST'])
def create():
    # req body must contain
    if 'work_order' not in request.json or 'gis_user_id' not in request.json or 'crew_leader_id' not in request.json:
        return abort(400)
    # users with ids must exist
    Crew_leader.query.get_or_404(request.json['crew_leader_id'])
    Gis_user.query.get_or_404(request.json['gis_user_id'])
    # construct Asbuilt
    a = Asbuilt(
        crew_leader_id=request.json['crew_leader_id'],
        work_order=request.json['work_order'],
        gis_user_id=request.json['gis_user_id'],
        install_date=request.json['install_date']
    )
    db.session.add(a)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(a.serialize(gis(a.gis_user_id), crew(a.crew_leader_id)))


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a = Asbuilt.query.get_or_404(id)
    try:
        db.session.delete(a)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PUT'])  # UPDATE/PUT
def put(id: int):
    a = Asbuilt.query.get_or_404(id)
    req_wo = request.json['Work Order']
    req_id = request.json['Install Date']

    # check if work order/ install date exists in json
    if req_wo:
        a.work_order = req_wo
    if req_id:
        a.install_date = req_id

    # execute Update statement
    try:
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Asbuilt.query.get_or_404(id)
    #g = Gis_user.query.get_
    return jsonify(a.serialize(gis(id), crew(id)))
