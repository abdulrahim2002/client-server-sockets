"""
2024 (C) Abdul Rahim, All rights reserved

Description: A sequential server

v1: only listens to client and logs its 
"""

import socket
import subprocess
import logging

#----------------------------------------------------------
IP = "127.0.0.1" # put the ec2 hostname here
# IP = socket.gethostname()   # so that the socket would be visible to the outside world
# IP = ''                     # specifies that the socket is reachable by any address the machine happens to have.
PORT = 7860
ADDR = (IP, PORT)
SIZE = 1024
CHAR = "utf-8"
#----------------------------------------------------------

logger = logging.getLogger(__name__)
logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def start_server():
    global server
    try:
        logger.info(f"[INITIALISATION] SERVER IP = {IP}\n")
        logger.info("[STARTING] SERVER IS STARTING...")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        logger.info(f"[LISTENING] Server is listening on {IP}:{PORT}")
    except OSError as e:
        logger.fatal(f"[FATAL] Failed to start server, Error: {e}")
        exit(1)

def execute_command(cmd:str):
    # TODO: Execute the supplied command command, capture the output, if success > 0 else > error
    pass

# handle client connection
def handle_client(conn, addr):
    logger.info(f"[SERVER] [NEW CONNECTION] {addr} connected.")
    
    while True:
        try:
            msg = conn.recv(SIZE).decode(CHAR)
            # cilent closed the connection/empty message is only being recieved if connection is closed
            if not msg: 
                break
            else:
                logger.info(f"[Message recieved]{msg}")
        except OSError as e:
            logger.error(f"Connection closed, Error: {e}")
            break

    logger.info(f"[SERVER] [EXITED CONNECTION] {addr} has left.")
    return


def main():
    start_server()

    try:
        while True:
            conn, addr = server.accept()
            handle_client(conn, addr)

    except KeyboardInterrupt:
        logger.debug("Keyboard interrupt, TERMINATING THE SERVER")
        try:
            conn.close()
        except OSError:
            pass
        finally:
            exit(0)

if __name__ == "__main__":
    main()
