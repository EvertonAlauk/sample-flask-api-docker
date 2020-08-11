from flask_restplus import Api

from .checkout import api as checkout

api = Api(title='Checkout', version='1.0', description='API REST for a generic checkout')

api.add_namespace(checkout)