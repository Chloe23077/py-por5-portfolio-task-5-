import socket


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 5000))
    question = input("Ask the magic 8-ball!!!: ")
    sock.send(question.encode())

    from_server = sock.recv(4096)
    sock.close()

    print("Magic 8-Ball's answer: ", from_server.decode())


if __name__ == '__main__':
    client()
