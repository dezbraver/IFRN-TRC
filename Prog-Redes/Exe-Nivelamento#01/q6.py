#!/usr/bin/env python3
import os

l = []

while True:
	try:
		n = float(input("Digite um numero: "))
		if n == 0: break
		l.append(n)
	except ValueError:
		print("O valor inserido eh invalido tente novamente.")
l = sorted(l)
os.system("clear")
for elem in l:
	print("{}".format(elem), end = " //")
print()
input("Tecle Enter para finalizar o programa...")
os.system("clear")
