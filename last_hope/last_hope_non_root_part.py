
import socket
import subprocess
import setproctitle


image_path = "/home/mono/croiss/CHEH.jpg"
commande = ["i3lock", "-pwin", "-i", image_path]


def server():
  host = socket.gethostname()   # get local machine name
  port = 65250  # Make sure it's within the > 1024 $$ <65535 range
  
  while True:  
    s = socket.socket()

    s.bind((host, port))
    s.listen(6)
    c, adress = s.accept()
    
    c.recv(1024).decode('utf-8')
    subprocess.run(["streamer", "-o", image_path])
    subprocess.run(commande)
    c.close()

if __name__ == '__main__':
    server()
