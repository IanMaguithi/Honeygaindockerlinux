import socket


def connection_test():
    timeout = 10
    try:
        socket.setdefaulttimeout(timeout)
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "8.8.8.8"
        port = 53
        server_address = (host, port)
        connection.connect(server_address)
    except OSError as error:
        with open("/tmp/output.log", "a") as output:
            output.write(f'{error}')
        return False
    else:
        connection.close()
        return True
