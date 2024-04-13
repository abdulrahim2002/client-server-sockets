"""
2024 (C) Abdul Rahim, All rights reserved

v1: only listens to client and logs its 
The role of the server is to: 
- recieve the data.json file. 
- Execute report-generator.jar via cmd interface, get the stderr if any.
- If successfull, return the file, else return the error message.
"""

import socket
import logging

#-------------------------------------
IP = '127.0.0.1'
PORT = 7860
ADDR = (IP, PORT)
SIZE = 1024
CHAR = "utf-8"
#-------------------------------------

logger = logging.getLogger(__name__)
logging.basicConfig(filename='client.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def send_message():
    try:
        while True:
            msg = input("Enter your message: ")
            if not msg:
                continue
            else:
                client.sendall(msg.encode(CHAR))
                logger.info(f"Message send: {msg}")
    except KeyboardInterrupt:
        client.close()
        exit(0)

# def recieve_messsage():
#     while True:
#         msg = client.recv(SIZE).decode(CHAR)
#         print(f"[SERVER] {msg}")
#         pass


def start_client():
    """starts the client, initialises the global 'client'"""
    global client
    try:
        logger.info(f"[CONNECTING] Client connecting to server at {IP}:{PORT}")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        logger.info(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    except OSError as e:
        logger.fatal(f"[CONNECTION ERROR] Failed to connect to server at {IP}:{PORT}, Error: {e}")
        exit(1)
        


def main():
    start_client()
    send_message()

if __name__ == "__main__":
    main()