import main
import unittest
import os
class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_root_request(self):
        response = self.app.get('/')
        assert response.status_code == 200
        assert "年".encode('utf-8') in response.data
    def test_root_method_not_allowed(self):
        response = self.app.post('/')
        assert response.status_code == 405
    def test_info_response(self):
        sent = dict(year='2019',month='12',members='6',holiday='9',at_least='2',at_holiday='3',continuous='6')
        response = self.app.post('/info', data=sent, follow_redirects=True)
        assert b"excel" in response.data
    def test_info_method_not_allowed(self):
        response = self.app.get('/info?year=2019&month=12&members=6&holiday=9&at_least=2&at_holiday=3&continuous=6')
        assert response.status_code == 405
    def test_result(self):
        response = self.app.get('/result/111')
        assert response.status_code == 200
        assert b"excel" in response.data
    def test_download(self):
        response = self.app.post('/download', data=dict(id='1'))
        assert b"xml" in response.data
        
if __name__ == '__main__':
    unittest.main()