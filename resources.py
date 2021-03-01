from dicttoxml import dicttoxml
from flask import request, jsonify, Response
from flask_restful import Resource
from flasgger import swag_from

from models import Driver


class GetReport(Resource):

    @swag_from('swagger_files/report.yml')
    def get(self):
        format_param = request.args.get('format', type=str)
        order_param = request.args.get('order', type=str)
        report = []
        for driver in Driver.select():
            driver_dict = {
                'number': driver.id,
                'name': driver.name,
                'team': driver.team,
                'result': str(driver.result)[3:12]
            }
            report.append(driver_dict)
        if order_param == 'desc':
            report = report[::-1]
        if format_param == 'xml':
            xml_report = dicttoxml(report)
            return Response(xml_report, content_type='text/xml')
        else:
            return jsonify(report)


class GetDriver(Resource):

    @swag_from('swagger_files/drivers.yml')
    def get(self):
        format_param = request.args.get('format', type=str)
        order_param = request.args.get('order', type=str)
        drivers = []
        for driver in Driver.select().order_by(Driver.driver_id):
            driver_dict = {
                'driver_id': driver.driver_id,
                'name': driver.name,
                'team': driver.team
            }
            drivers.append(driver_dict)
        if order_param == 'desc':
            drivers = drivers[::-1]
        if format_param == 'xml':
            xml_drivers = dicttoxml(drivers)
            return Response(xml_drivers, content_type='text/xml')
        else:
            return jsonify(drivers)


class GetDriverId(Resource):

    @swag_from('swagger_files/driver_id.yml')
    def get(self, driver_id):
        format_param = request.args.get('format', type=str)
        driver = Driver.get(Driver.driver_id == driver_id)
        driver_dict = {
            'driver_id': driver.driver_id,
            'name': driver.name,
            'team': driver.team,
            'result': str(driver.result)[3:12]
        }
        if format_param == 'xml':
            xml_drivers = dicttoxml(driver_dict)
            return Response(xml_drivers, content_type='text/xml')
        else:
            return jsonify(driver_dict)
