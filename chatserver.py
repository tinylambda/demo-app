import socket

from tornado.ioloop import IOLoop

keep_running = True
ioloop = IOLoop.instance()


def callback_for_new_data(connection, mask):
    global keep_running
    client_address = connection.getpeername()
    print('read {}'.format(client_address))
    data = connection.recv(1024)
    if data:
        print('received: {!r}'.format(data))
        if 'stop' in data.decode('utf-8'):
            connection.sendall(b'Server will stop')
            ioloop.stop()
    else:
        print('closing')
        ioloop.remove_handler(connection)
        ioloop.close_fd(connection)
        keep_running = False


def callback_for_new_connections(sock, mask):
    new_connection, addr = sock.accept()
    print('accept ({})'.format(addr))
    new_connection.setblocking(False)
    ioloop.add_handler(new_connection, callback_for_new_data, ioloop.READ)


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    # server.settimeout(1)
    server_address = ('0.0.0.0', 10000)
    server.bind(server_address)
    server.listen(5)

    ioloop.add_handler(server, callback_for_new_connections, ioloop.READ)
    print('Starting IOLoop instance')
    ioloop.start()


