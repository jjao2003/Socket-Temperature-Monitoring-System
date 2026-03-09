import socket
import threading
import random
import time


def receive_messages(sock):
    """Function to constantly listen for data from the server."""
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                print("\n[Server shut down]")
                break
            print(f"\n[SERVER]: {message}")
        except:
            break


def send_temperature(sock):
    """Generate and send random temperature data every 5 seconds."""
    while True:
        try:
            temperature = round(random.uniform(20.0, 35.0), 2)  # random temp
            message = f"TEMP:{temperature}°C"

            sock.sendall(message.encode('utf-8'))
            print(f"[SENT]: {message}")

            time.sleep(5)

        except:
            break


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server IP and Port
    server_ip = '172.20.10.3'
    port = 55555

    try:
        client_socket.connect((server_ip, port))
        print(f"Connected to server at {server_ip}")

        # Thread to receive server messages
        threading.Thread(
            target=receive_messages,
            args=(client_socket,),
            daemon=True
        ).start()

        # Thread to send temperature data
        threading.Thread(
            target=send_temperature,
            args=(client_socket,),
            daemon=True
        ).start()

        # Optional: allow manual commands
        while True:
            msg = input("[YOU]: ")
            if msg.lower() == "exit":
                break
            client_socket.sendall(msg.encode('utf-8'))

    except Exception as e:
        print(f"Connection error: {e}")

    finally:
        client_socket.close()
        print("Client closed.")


if __name__ == "__main__":
    start_client()