from flask import Flask, request, jsonify, render_template
from chatbot_logic import get_response
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/get_response', methods=['POST'])
def get_chatbot_response():
    app.logger.info('Received POST request to /get_response')
    data = request.get_json()
    user_input = data['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
