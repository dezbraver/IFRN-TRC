import os
from collections import deque

m = []
while True:
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

	try:
		if c != l: raise ValueError
		break
	except ValueError:
		os.system("clear")
		print("Para obter o determinante a matriz deve ser quadrada.")

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

mA = []
mB = []

for i in range(len(m)):
	M = deque(m[i])
	if i > 0:
		M.rotate(-i)
	mA.append(M)

for i in range(len(m)):
	M = deque(m[i])
	if i > 0:
		M.rotate(i)
	mB.append(M)

somadA = 0
somadB = 0

for i in range(len(mA)):
	mult = 1
	for j in range(len(mA)):
		mult *= mA[j][i]
	somadA += mult

for i in range(len(mB)):
	mult = 1
	for j in range(len(mB)):
		mult *= mB[j][i]
	somadB += mult

determinante = somadA - somadB

print("Determinante = {}".format(determinante))
