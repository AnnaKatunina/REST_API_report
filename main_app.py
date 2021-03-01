from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from resources import GetReport, GetDriver, GetDriverId

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)
swagger = Swagger(app)

version = 'v1'

api.add_resource(GetReport, f'/api/{version}/report')
api.add_resource(GetDriver, f'/api/{version}/drivers')
api.add_resource(GetDriverId, f'/api/{version}/drivers/<string:driver_id>')


@app.errorhandler(404)
def page_not_found(error):
    return 'Page is not found', 404


@app.errorhandler(500)
def server_error(error):
    return 'Server Error', 500


if __name__ == '__main__':
    app.run(debug=True)
