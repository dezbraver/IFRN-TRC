import os

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


