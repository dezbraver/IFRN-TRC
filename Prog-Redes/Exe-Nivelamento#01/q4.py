#!/usr/bin/env python3
import os
import sys

x, y, r = 1, 0, 0

try:
	n = int(sys.argv[1])
	if n <= 0: raise ValueError
except (ValueError, IndexError):
	print("Argumento de linha de comando invalido ou inexistente.")
	while True:
		try:
			n = int(input("Digite um numero inteiro positivo: "))
			if n <= 0: raise ValueError
			os.system("clear")
			break
		except ValueError:
			os.system("clear")
			print("Valor inserido invalido tente novamente.")

for i in range(0, n):
	r = x + y
	x = y
	y = r
	print(r, end = " ") 
print()
input("Tecle Enter para finalizar o programa...")
os.system("clear")
