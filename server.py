import socket
import threading
import datetime

mydata = {}

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '$DISCONNECT!!!'
PORT = 80
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    data = conn.recv(2096).decode(FORMAT)
    if("!@#$%^&*(" in data and ")*&^%$#@!" in data):
        x = data[data.index("!@#$%^&*(")+9:data.index(")*&^%$#@!")]
        mydata[str(datetime.datetime.now())] = x
        conn.send("Data set updated".encode(FORMAT))
        print(f"New DataSet : {mydata}")
    else:
        conn.send("<head><title>PeakyToolz</title>".encode(FORMAT))
        conn.send('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"></head>'.encode(FORMAT))
        conn.send("<h1>Data :</h1>".encode(FORMAT))
        conn.send("<hr>".join([f"{key}<br><strong>{mydata[key]}</strong>" for key in mydata]).encode(FORMAT))
        conn.send("<script>setTimeout(function(){window.location.reload(1);}, 5000);</script>".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[SERVER IS LISTENING AT {SERVER}]")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handleClient,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()