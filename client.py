import socket
import threading

def receive_messages(sock):
    """Function to constantly listen for data from the server."""
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                print("\n[Server shut down]")
                break
            print(f"\n[SERVER]: {message}")
            print("[YOU]: ", end="") # Keep the prompt visible
        except:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Use your specific IP
    server_ip = '172.20.10.3'
    port = 55555

    try:
        client_socket.connect((server_ip, port))
        print(f"Connected to server at {server_ip}")

        # Start a background thread to receive messages
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        # Main loop to send messages from the terminal
        while True:
            msg = input("[YOU]: ")
            if msg.lower() == 'exit':
                break
            client_socket.sendall(msg.encode('utf-8'))

    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()
        print("Client closed.")

if __name__== "__main__":
    start_client()