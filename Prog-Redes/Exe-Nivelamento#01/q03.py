#!/usr/bin/env python3
import os

l = []

while True:
	try:
		n = int(input("Digite um numero: "))
		if n == 0: break
		l.append(n)
	except ValueError:
		print("O valor inserido eh invalido tente novamente.")

soma = 0
for elem in l:
	soma = soma + elem
try:
	media = soma / len(l)
	maior = max(l)
	menor = min(l)
	os.system("clear")
	print("Maior numero: {:>}\nMenor numero: {:>}\nMedia: {:>}".format(maior, menor, media))
	input("Tecle Enter para finalizar o programa...")
	os.system("clear")
except ZeroDivisionError:
	os.system("clear")
	print("Nao existem numeros a serem tratados.")
	input("Tecle Enter para finalizar o programa...")
	os.system("clear")
