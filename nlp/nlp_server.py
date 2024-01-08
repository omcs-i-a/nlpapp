# import nlp_module
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return "Hello, nlp"


@app.route('/correct', methods=['POST'], endpoint="correct-text")
def correct_text():
    data = request.get_json()
    text = data['text']
    corrected_text = text
    return jsonify({'corrected_text': corrected_text})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)