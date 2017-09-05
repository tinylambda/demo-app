import selectors
import socket

myselector = selectors.DefaultSelector()
keep_running = True


def callback_for_new_data(connection, mask):
    global keep_running
    client_address = connection.getpeername()
    print('read {}'.format(client_address))
    data = connection.recv(1024)
    if data:
        print('received: {!r}'.format(data))
        if 'stop' in data.decode('utf-8'):
            connection.sendall(b'Server will stop')
            keep_running = False
    else:
        print('closing')
        keep_running = False


def callback_for_new_connections(sock, mask):
    new_connection, addr = sock.accept()
    print('accept ({})'.format(addr))
    new_connection.setblocking(False)
    myselector.register(new_connection, selectors.EVENT_READ, callback_for_new_data)


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server_address = ('0.0.0.0', 10000)
    server.bind(server_address)
    server.listen(5)
    myselector.register(server, selectors.EVENT_READ, callback_for_new_connections)

    print('Starting IOLoop instance')
    # without tornado, we just write our own loop ~~
    while keep_running:
        print('waiting for IO ...')
        for key, mask in myselector.select(timeout=1):
            callback = key.data
            callback(key.fileobj, mask)

    print('Stopping...')
    myselector.close()


