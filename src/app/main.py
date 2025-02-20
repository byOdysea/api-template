from flask import Blueprint, request

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def main_route():
    return Response.success('main'), 200