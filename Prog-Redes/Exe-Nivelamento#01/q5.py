#!/usr/bin/env python3
import os

vogais = ["a", "e", "i", "o", "u"]
frase = input("Digite uma frase: ")
nv, nc = 0, 0
os.system("clear")
for caractere in frase:
	if caractere in vogais:
		nv += 1
	elif caractere.isalpha() == False:
		pass
	else:
		nc += 1

print("Nº de Caracteres (Espaços em branco contabilizados): {:>}\nNº de Vogais: {:>}\nNº de Consoantes: {:>}".format(len(frase), nv, nc))
input("Tecle Enter para finalizar o programa...")
os.system("clear")
