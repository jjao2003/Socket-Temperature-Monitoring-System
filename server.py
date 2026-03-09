import socket
import threading

HOST = "0.0.0.0"
PORT = 55555


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            data = conn.recv(1024).decode("utf-8")

            if not data:
                break

            print(f"[DATA RECEIVED] {addr} -> {data}")

            response = "Temperature received successfully"
            conn.send(response.encode("utf-8"))

        except:
            break

    print(f"[DISCONNECTED] {addr}")
    conn.close()


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER STARTED] Listening on port {PORT}")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )

        thread.start()


if __name__ == "__main__":
    start_server()