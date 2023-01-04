
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)

def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(
        socket.AF_INET,     # Address Format = (host:hostname/IPv4, port:int)
        socket.SOCK_STREAM  # TCP
    )
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

if __name__ == "__main__":
    main()