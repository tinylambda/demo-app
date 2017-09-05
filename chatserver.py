import socket


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server.settimeout(1)
    server_address = ('0.0.0.0', 10000)
    server.bind(server_address)
    server.listen(5)

    while True:
        print('waiting for the next event...')
        while True:
            try:
                connection, client_address = server.accept()
                try:
                    while True:
                        data = connection.recv(16)
                        if data:
                            print(data)
                        else:
                            break
                except Exception as e:
                    print('Exception', e)
                finally:
                    connection.close()
            except socket.error:
                print('.')

