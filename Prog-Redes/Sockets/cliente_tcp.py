#!/usr/bin/env python3
import socket

host = ""
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((host, port))
	l = []
	while True:
		msg = input("Mensagem: ")
		msg = msg.encode("utf-8")
		s.send(msg)
		if msg.decode("utf-8") == "close": break
	while True:
		elem = s.recv(512)
		elem = elem.decode("utf-8")
		if elem == "close": break
		l.append(elem)
	print(l)
