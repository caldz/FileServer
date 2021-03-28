import socket
import FileOp


class FileClient:
    def __init__(self):



if __name__ == "__main__":
    target_file = './test_log.txt'
    fc = FileClient()
    sc = FileOp.get_server_config()
    fc.connect(sc['server_ip'],sc['server_port'])
    fc.send_file(target_file)
    fc.close()