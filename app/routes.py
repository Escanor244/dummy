from flask import Blueprint, request, jsonify
from app.service import PrefixService

# Predefined word list
word_list = ["bonfire", "cardio", "case", "bonsai"]
prefix_service = PrefixService(word_list)

prefix_blueprint = Blueprint('prefix_api', __name__)

@prefix_blueprint.route('/prefixes', methods=['GET'])
def get_prefixes():
    keywords = request.args.get('keywords', '')
    if not keywords:
        return jsonify({"error": "No keywords provided"}), 400

    keywords_list = [k.strip() for k in keywords.split(',')]
    response = prefix_service.get_prefixes(keywords_list)
    return jsonify(response)
