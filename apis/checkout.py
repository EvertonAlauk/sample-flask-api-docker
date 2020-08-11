
from flask import jsonify
from flask_restplus import Namespace
from flask_restplus import Resource

from jsonschema import validate
from schema import schema

api = Namespace('checkout', description='')

@api.route('/')
class CheckoutAPI(Resource):

    def get(self):
        return jsonify({})
