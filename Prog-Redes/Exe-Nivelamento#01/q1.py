import sys

try:
	n = int(sys.argv[1])
except (IndexError, ValueError):
	while True:
		try:
			n = int(input("Digite um numero inteiro positivo: "))
			break
		except ValueError:
			print("O numero digitado eh invalido.")
			print("!!!Lembre-se o numero digitado deve ser inteiro e Positivo!!!")

print(n)
#tratar o uso de numeros negativos
