import os, threading
from socket import socket

online = []

def Receber(con, cli):
    while True:
        recebido = con.recv(1024)
        recebido = recebido.decode("utf-8")

def Enviar():

def Sock():
    os.system("clear")
    host = "localhost"
    port = 50000

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print("Servidor Ligado!")
        while True:
            con, cli = s.accept()
            online.append(con)
            print("{} se conectou!".format(cli))
            threading.Thread(target=Receber, args=(con, cli))
