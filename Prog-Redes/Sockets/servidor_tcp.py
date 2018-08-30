#!/usr/bin/env python3
import socket
from collections import deque

host = ""
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((host, port))
	s.listen(1)
	print("Aguardando Conexões...\n")
	while True:
		c = s.accept()
		print("Conectado por:", c[1])
		with c[0] as con:
			l = []
			l = deque(l)
			while True:
				msg = con.recv(512)
				msg = msg.decode("utf-8")
				if msg == "sair": break
				l.append(msg)
				print("Mensagem Recebida:", msg)
				if len(l) > 5:
					l.popleft()
			for i in range(len(l)):
				con.send(l[i].encode("utf-8"))
			con.send("sair".encode("utf-8"))
			con.close()
