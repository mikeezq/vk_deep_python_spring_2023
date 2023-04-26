import argparse
from unittest import TestCase
import threading


from server import start_server, get_common_words
from client import start_client


class TestClientServer(TestCase):
    def test_many_urls(self):
        args = argparse.Namespace(k=7, w=10)
        server_thread = threading.Thread(target=start_server, args=(args,))
        server_thread.start()

        start_client(["1", "test_urls.txt"])
        server_thread.join()

        url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
        most_common_words = get_common_words(args, url)
        assert most_common_words == {"the": 454, "Python": 337, "and": 260, "from": 247, "on": 228, "^": 221, "a": 206}

        url = "https://www.python.org/"
        most_common_words = get_common_words(args, url)
        assert most_common_words == {"Python": 51, ">>>": 24, "and": 21, "the": 18, "to": 16, "is": 11, "for": 11}

        url = "https://docs.python.org/3/tutorial/index.html"
        most_common_words = get_common_words(args, url)
        assert most_common_words == {"and": 42, "Python": 31, "The": 20, "the": 18, "a": 11, "to": 10, "of": 9}
