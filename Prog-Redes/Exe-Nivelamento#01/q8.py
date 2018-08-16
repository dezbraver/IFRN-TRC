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

def Det12(m):
	if len(m[0]) == 1:
		determinante = m[0][0]
	elif len(m[0]) == 2:
		multA = 1
		for i in range(len(m[0])):
			multA *= m[i][i]
		multB = 1
		for i in range(len(m[0])):
			if i == 0:
				multB *= m[i][i+1]
			else:
				multB *= m[i][i-1]
		determinante = multA - multB
	return determinante

def Laplace(matriz):
	determinante = 0
	cofs = []
	lchave = matriz[0]
	matriz.remove(lchave)
	for x in range(len(lchave)):
		mm = []
		for i in range(len(matriz)):
			v = []
			for j in range(len(matriz[0])):
				if j == x:
					pass
				else:
					v.append(matriz[i][j])
			mm.append(v)
		if len(mm) > 2:
			cofs.append(((-1)**(1+(x+1)))*Laplace(mm))
		else:
			cofs.append(((-1)**(1+(x+1)))*Det12(mm))
	for x in range(len(cofs)):
		determinante += lchave[x] * cofs[x]
	return determinante

if c < 3:
	print("Determinante: {}".format(Det12(m)))
else:
	print("Determinante: {}".format(Laplace(m)))
