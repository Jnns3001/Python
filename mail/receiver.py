import socket


port = 3003
username = "Jannis"



def register():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("register")
    server = ("10.0.2.189", 3053)
    
    connection = s.connect(server)
    
    reg = "REGISTER\n%s" % username
    
    encoded = reg.encode("utf8")
    s.sendall(encoded)
    
    print("sent")
    
    s.close()
    
register()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))
s.listen()

while True:
    print("listening")
    connection, address = s.accept()

    encoded = connection.recv(4096)
    connection.close()

    message = encoded.decode("utf8")


    print(message)