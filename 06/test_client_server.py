import argparse
from unittest import TestCase
from unittest.mock import patch

from server import handle_request


class TestServer(TestCase):
    @patch('server.socket.socket')
    def test_handle_request(self, mock_socket):
        mock_client_socket = mock_socket.return_value
        mock_client_socket.recv.return_value = b'http://example.com'

        url = "fake-url"
        with patch('requests.get') as mock_get:
            response = mock_get.return_value
            response.text = "Hello, world!"
            handle_request(argparse.Namespace(k=5), url, mock_client_socket)

            mock_get.assert_called_once_with(url, timeout=10)
            mock_client_socket.send.assert_called_with(b'{"Hello,": 1, "world!": 1}')
