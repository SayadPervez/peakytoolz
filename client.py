import socket
import time

FORMAT = 'utf-8'
PORT = 80
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)



def send(msg):
    client = socket.socket()
    client.connect(ADDR)
    message = ("!@#$%^&*("+msg+")*&^%$#@!").encode(FORMAT)
    client.send(message)
    print(f"[RECIEVED MSG] {client.recv(2048).decode(FORMAT)}")
    client.close()

send("Hi")
time.sleep(10)
send("Bye")
time.sleep(10)
send("I HATE SHYAM")