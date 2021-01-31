import socket
import time

targetport = 3003
dictionary = {}
username = "Jannis"#input("dein Name")

def discover():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("discovering")
    server = ("10.0.2.189", 3053)
    
    connection = s.connect(server)
    
    discover = "DISCOVER"
    encoded = discover.encode("utf8")
    s.sendall(encoded)
    print("sent")
    
    s.shutdown(socket.SHUT_WR)
    time.sleep(0.1)

    encoded = s.recv(4096)
    print("recieved")
    
    list = encoded.decode("utf8")
    print(len(list))
    print(list)
    lines = list.splitlines()
    
    for item in lines:
        name, _, ip = (item.rpartition(' '))
        dictionary[name] = ip

    print(dictionary.keys())
    print("discovered")
    
    s.close()


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    discover()
    
    key = input("mit wem willst du schreiben? \n")
    targetip = dictionary[key]
    print(targetip)
    
    target = (targetip, targetport)
    print(target)
    
    text = input("Gib deine Nachricht ein \n")
    message = username + "\n" + text

    s.connect(target)
    encoded = message.encode("utf8")
    s.sendall(encoded)
    s.close()
