from unittest import mock

from unittest.mock import AsyncMock

import pytest

from aiounittest import AsyncTestCase

from urls_parser import fetch_urls


class TestUrlsParser(AsyncTestCase):
    async def test_async_parse(self):
        ret = await fetch_urls([5, "test_urls.txt"])
        assert ret == 3

        async_mock = AsyncMock()
        with mock.patch("urls_parser.fetch_url", side_effect=async_mock) as mock_fetch_url:
            await fetch_urls([10, "random_urls.txt"])
            assert mock_fetch_url.call_count == 100

    async def test_incorrect_args(self):
        with pytest.raises(ValueError, match="First argument must be numeric"):
            await fetch_urls(["test", "test"])

        with pytest.raises(FileNotFoundError, match="File test does not exists"):
            await fetch_urls([1, "test"])
