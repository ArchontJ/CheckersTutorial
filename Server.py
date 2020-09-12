import socket
from _thread import *
import sys

server = "192.168.8.119"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# liczba okresla liczbe osob podlaczonych
s.listen(2)
print("waiting fpr a connection, Server started")

def threaded_client(conn):
    conn.send(str.encode("connected"))
    reply = ""
    while True:
        try:
            data=conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print ("Receoved: ",reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break



while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
