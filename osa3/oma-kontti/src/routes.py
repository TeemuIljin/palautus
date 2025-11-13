from flask import Blueprint, jsonify, request

# Create a Blueprint for the routes
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify(message="Welcome to the Flask application!")

@bp.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    return jsonify(data)

@bp.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    return jsonify(new_data), 201

@bp.route('/api/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    data = {
        "id": data_id,
        "key": "value"
    }
    return jsonify(data)

@bp.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    return jsonify(message=f"Data with id {data_id} has been deleted."), 204