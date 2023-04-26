import json
import socket
import concurrent.futures
import argparse

from collections import Counter

import threading

import requests

from bs4 import BeautifulSoup


mutex = threading.Lock()

k = 0


def get_common_words(args, url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.get_text().split()
    words = Counter(words).most_common(args.k)

    most_common_words = {}
    for key, value in words:
        most_common_words[key] = value

    return most_common_words


def handle_request(args, url, client_socket):
    global k

    most_common_words = get_common_words(args, url)

    with mutex:
        k += 1

    client_socket.send(json.dumps(most_common_words, ensure_ascii=False).encode())
    print(f"{k=}")


def start_server(args):
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.w) as executor:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 8000))
        sock.listen(args.w)
        while True:
            client_socket, _ = sock.accept()
            data = client_socket.recv(1024)
            url = data.decode().strip()
            executor.submit(handle_request, args, url, client_socket)


def parse_args():
    args_parser = argparse.ArgumentParser()

    args_parser.add_argument("-w", type=int, default=5, help="workers count")
    args_parser.add_argument("-k", type=int, default=5, help="most common words count")

    return args_parser.parse_args()


if __name__ == '__main__':
    parser = parse_args()
    start_server(parser)
