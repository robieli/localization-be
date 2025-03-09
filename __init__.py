from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from langchain_core.messages import HumanMessage, SystemMessage
import model

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
    
@app.route('/llm')
def get_llm():
    lang = request.args.get('lang')
    query = request.args.get('query')
    llm = model.llm
    messages = [
        SystemMessage("You should perform tasks like normal, except for that all of your responses should be in the language of the following ISO 639 code: " + lang + ". Please do not use any markup notation, as your response will be displayed in plain text."),
        HumanMessage(query)
    ]
    return jsonify(llm.invoke(messages).content)

if __name__ == '__main__':
    app.run(debug=True)
