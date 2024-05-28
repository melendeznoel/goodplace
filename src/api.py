import json
import uuid

from flask import Flask, jsonify, request
from talking_service import TalkingService

flask_api = Flask(__name__)
talking_service = TalkingService()

@flask_api.route('/ship', methods=['POST'])
def create_cruise():
    """Function handles routing"""
    cruise = json.loads(request.data)

    if not data_is_valid(cruise):
        return jsonify({ 'error': 'Invalid properties.' }), 400

    ship_id = uuid.uuid4()

    cruise["id"] = ship_id

    print(cruise)

    ai_response = talking_service.find(cruise["context"])

    response = ai_response.toJSON()

    return response, 200, { 'location': f'/ship/{cruise["id"]}', 'Content-Type':'application/json' }

def data_is_valid(data):
    """Function checks if the data is valid"""
    for key in data.keys():
        if key != 'context':
            return False
    return True

if __name__ == '__main__':
    flask_api.run(port=5000)
