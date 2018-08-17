#!/usr/bin/env python3
import os

m = []
mt = []

while True:
	try:
		c = int(input("Digite o numero de colunas: "))
		if c <= 0: raise ValueError
		break
	except ValueError:
		os.system("clear")
		print("O valor informado nao eh valido, tente novamente.")

while True:
	try:
		l = int(input("Digite o numero de linhas: "))
		if l <= 0: raise ValueError
		break
	except ValueError:
		os.system("clear")
		print("O valor informado nao eh valido, tente novamente.")

os.system("clear")
for linha in range(0, l):
	lista = []
	for coluna in range(0, c):
		while True:
			try:
				n = float(input("Digite o valor em lin({}) col({}): ".format((linha + 1), (coluna + 1))))
				break
			except ValueError:
				print("O valor informado deve ser um numero, tente novamente.")
		lista.append(n)
	m.append(lista)

for i in range(len(m[0])):
	vetor = []
	for j in range(len(m)):
		vetor.append(m[j][i])
	mt.append(vetor)

os.system("clear")
print("Matriz:")
for i in range(len(m)):
        for j in range(len(m[0])):
                print("{:^10}".format(m[i][j]), end = "//")
        print()

print("\nTransposta:")
for i in range(len(mt)):
	for j in range(len(mt[0])):
		print("{:^10}".format(mt[i][j]), end = "//")
	print()

input("Tecle Enter para finalizar o programa...")
