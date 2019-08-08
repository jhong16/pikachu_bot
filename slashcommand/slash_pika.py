import os

from flask import abort, Flask, jsonify, request

app = Flask(__name__)

def is_request_valid(request):
    is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
    is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']
    return is_token_valid and is_team_id_valid

@app.route('/pika', methods=['POST'])
def hello_there():
    if not is_request_valid(request):
        abort(400)
    
    command = request.form['text']
    
    if command == '':
        command = 'pi?'

    return jsonify(
            response_type='in_channel', 
            text=command
    )

@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify(
            response_type='in_channel',
            text='Chu?'
    )