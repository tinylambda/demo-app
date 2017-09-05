import errno
import socket
import tornado.ioloop


def connection_ready(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except sock.error as e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        connection.setblocking(0)
