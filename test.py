import unittest

from main_app import app


class FlaskTestCase(unittest.TestCase):

    def test_report(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/report?format=json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'{"number":1,"name":"Sebastian Vettel","team":"FERRARI","result":"01:04.415"}'
                        in response.data)

    def test_drivers(self):
        tester = app.test_client(self)
        response = tester.get('api/v1/drivers?format=xml')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'<driver_id type="str">BHS</driver_id><name type="str">Brendon Hartley</name>'
                        b'<team type="str">SCUDERIA TORO ROSSO HONDA</team></item><item type="dict">' in response.data)

    def test_drivers_id(self):
        tester = app.test_client(self)
        response = tester.get('api/v1/drivers/MES?format=json')
        self.assertEqual(response.status_code, 200)
        print(response.data)
        self.assertTrue(b'{"driver_id":"MES","name":"Marcus Ericsson","team":"SAUBER FERRARI","result":"01:13.265"}'
                        in response.data)


if __name__ == '__main__':
    unittest.main()
