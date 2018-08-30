#!/usr/bin/env python3
import socket
import time

host = ""
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((host, port))
	while True:
		msg = input("Mensagem: ")
		msg = msg.encode("utf-8")
		s.send(msg)
		if msg.decode("utf-8") == "sair": break
	l = []
	while True:
		print("cheguei")
		elem = s.recv(124)
		if not elem: break
		elem1 = ''
		elem1 = elem.decode("utf-8")
		l.append(elem1)
	print(l)
