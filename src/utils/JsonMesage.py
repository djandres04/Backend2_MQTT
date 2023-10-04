from flask import jsonify

def message_error(error):
    return jsonify({'message': str(error)}), 500

