from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import numpy as np

APP = Flask(__name__)
API = Api(APP)

IRIS_MODEL = joblib.load('iris.mdl')


class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('petal_length',location='form')
        parser.add_argument('petal_width',location='form')
        parser.add_argument('sepal_length',location='form')
        parser.add_argument('sepal_width',location='form')

        args = parser.parse_args()  # creates dict

        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array

        out = {'Prediction': IRIS_MODEL.predict([X_new])[0]}

        return out, 200


API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1080',host='0.0.0.0')
