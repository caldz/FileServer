import socket
from socket import socket
from typing import Any, Tuple

import FileOp
from socket import *


def read_file_lines(file_path):
    f = open(file_path, 'rb')
    data = f.read(1024)
    print(data)
    f.close()
    return data


class FileClient:
    addr: tuple[Any, Any]
    sock: socket

    def __init__(self):
        pass

    def set_addr(self, server_ip, server_port):
        self.addr = (server_ip, server_port)
        return self

    def upload_file(self, file_path):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self.addr)
        data = read_file_lines(file_path)
        sock.send(data)
        sock.close()
        pass


if __name__ == '__main__':
    target_file = './test_log.txt'
    sc = FileOp.get_server_config()
    FileClient().set_addr(sc['server_ip'], sc['server_port']).upload_file(target_file)
