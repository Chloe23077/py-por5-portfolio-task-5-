import socket
import random

QUEUE_SIZE = 5

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('', 5000))
    serv.listen(QUEUE_SIZE)
    print("Server is listening port 5000...")

    # always listen for connections
    while True:
        conn, addr = serv.accept()
        print(f'Cntn: {addr}')
        from_client = ''

        while True:
            data = conn.recv(4096)

            # end of data
            if not data:
                break

            from_client += data.decode()
            print(f"Received Question: {from_client}")

            answer = random.choice(responses)
            print(f"answer: {answer}")

            conn.send(f"From server to client : {answer}".encode())

        conn.close()
        print('client disconnected')


if __name__ == '__main__':
    server()
