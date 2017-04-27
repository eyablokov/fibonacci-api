#!/fibonacci/usr/fibonacci/bin/fibonacci/env python3

from unittest import TestCase
from flask import json
from mock import patch
from resources import app


class TestWebResource(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_size_is_negative_number_returns_400(self):
        response = self.client.get('/fibonacci/-1')
        self.assertEqual(response.status_code, 400)

    def test_size_is_negative_number_returns_correct_error_message(self):
        response = self.client.get('/fibonacci/-1')
        error_message = self.retrieve_error_message(response)
        self.assertEqual('Size must be a positive integer. Actual -1', error_message)

    def test_invalid_string_in_path_returns_400(self):
        response = self.client.get('/fibonacci/bad')
        self.assertEqual(response.status_code, 400)

    def test_invalid_string_in_path_returns_correct_error_message(self):
        response = self.client.get('/fibonacci/bad')
        error_message = self.retrieve_error_message(response)
        self.assertEqual('Size must be a positive integer. Actual bad', error_message)

    def test_size_greater_than_upper_boundary_returns_400(self):
        response = self.client.get('fibonacci/1001')
        self.assertEqual(response.status_code, 400)

    def test_size_greater_than_upper_boundary_returns_correct_message(self):
        response = self.client.get('fibonacci/1001')
        error_message = self.retrieve_error_message(response)
        self.assertEqual('Size must be a positive integer <= to 1000. Actual 1001', error_message)

    def test_invalid_path_returns_404(self):
        response = self.client.get('fibonacci/test/1223')
        self.assertEqual(response.status_code, 404)

    def test_invalid_path_returns_json_response(self):
        response = self.client.get('fibonacci/test/1223')
        self.assertEqual(response.content_type, 'application/json')

    def test_size_is_0_returns_200(self):
        response = self.client.get('fibonacci/0')
        self.assertEqual(response.status_code, 200)

    def test_size_is_0_returns_with_empty_list(self):
        response = self.client.get('fibonacci/0')
        response_data = json.loads(response.data)
        fibonacci_list = response_data.get("fibonacci")
        self.assertEqual(len(fibonacci_list), 0)

    def test_size_is_5_returns_200_with_correct_list(self):
        response = self.client.get('fibonacci/5')
        response_data = json.loads(response.data)
        fibonacci_list = response_data.get("fibonacci")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(fibonacci_list[0], 0)
        self.assertEqual(fibonacci_list[1], 1)
        self.assertEqual(fibonacci_list[2], 1)
        self.assertEqual(fibonacci_list[3], 2)
        self.assertEqual(fibonacci_list[4], 3)

    def test_post_to_valid_url_returns_405(self):
        response = self.client.post('fibonacci/0')
        self.assertEqual(response.status_code, 405)

    def test_unhandled_exception_returns__json_response(self):
        response = self.client.post('fibonacci/0')
        self.assertEqual(response.content_type, 'application/json')

    @patch('sequence_generators.fibonacci.generate_sequence')
    def test_get_calls_fibonacci_generator(self, mock_generator):
        self.client.get('fibonacci/0')
        mock_generator.assert_called_with(0)

    def retrieve_error_message(self, response):
        response_data = json.loads(response.data)
        error_message = response_data.get("message")
        return error_message
