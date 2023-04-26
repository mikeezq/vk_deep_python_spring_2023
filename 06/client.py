import socket
import concurrent.futures
import sys


def send_request(url):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8000))
    s.send(url.encode())
    common_words = s.recv(1024).decode()
    s.close()
    print(common_words)


def start_client(args):
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(args[0])) as executor:
        for url in open(args[1], "r"):
            executor.submit(send_request, url)


if __name__ == '__main__':
    args = sys.argv[1:]
    start_client(args)
