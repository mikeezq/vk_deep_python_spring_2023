import argparse
from unittest import mock

from unittest.mock import AsyncMock

import asyncio
import pytest

from asynctest import patch
from aiounittest import AsyncTestCase
from urls_parser import fetch_urls, fetch_url


class TestUrlsParser(AsyncTestCase):
    async def test_async_parse(self):
        async_mock = AsyncMock()
        with mock.patch("urls_parser.fetch_url", side_effect=async_mock) as mock_fetch_url:
            await fetch_urls(argparse.Namespace(c=5, file="test_urls.txt"))
            assert mock_fetch_url.call_count == 3

        async_mock = AsyncMock()
        with mock.patch("urls_parser.fetch_url", side_effect=async_mock) as mock_fetch_url:
            await fetch_urls(argparse.Namespace(c=10, file="random_urls.txt"))
            assert mock_fetch_url.call_count == 100

    async def test_incorrect_args(self):
        with pytest.raises(FileNotFoundError, match="File test does not exists"):
            await fetch_urls(argparse.Namespace(c=1, file="test"))

    @patch("aiohttp.ClientSession.get")
    async def test_fetch_url(self, mock_get):
        test_url = "http://example.com"
        response_text = "Response Text"

        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.text.return_value = response_text

        mock_get.return_value.__aenter__.return_value = mock_response

        text = await fetch_url(test_url, asyncio.Semaphore(1))
        assert text == response_text
