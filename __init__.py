from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from langchain_openai import AzureChatOpenAI

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return "Hello world!"

@app.route('/<lang_code>')
def get_translations(lang_code):
    try:
        with open(f'translations/{lang_code}.json', 'r', encoding='utf-8') as file:
            translations = json.load(file)
        return jsonify(translations)
    except FileNotFoundError:
        return jsonify({"error": "Language not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
