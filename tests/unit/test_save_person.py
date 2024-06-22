import unittest
from unittest.mock import patch
import json
from save_person.app import lambda_handler


class TestLambdaFunction(unittest.TestCase):

    @patch('save_person.app.load_body')
    def test_internal_server_error(self, mock_load_body):
        mock_load_body.side_effect = Exception("Simulated Exception")
        event = {
            'body': 'invalid_json'
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 500)
        body = json.loads(response['body'])
        self.assertEqual(body['message'], 'Server failed')


if __name__ == '__main__':
    unittest.main()
