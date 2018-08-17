#!/usr/bin/env python3
import sys

try:
	n = int(sys.argv[1])
	if n < 1:
		raise ValueError
except (IndexError, ValueError):
	print("### O valor inserido nao esta de acordo com as exigencias de entrada, por favor tente novamente \###")
	while True:
		try:
			n = int(input("Digite um numero inteiro positivo: "))
			if n < 1:
				raise ValueError
			break
		except ValueError:
			print("### Por favor, certifique-se de que o valor inserido esta de acordo com as exigencias de entrada e tente novamente \###")

for x in range(1, 11):
	print("{} x {:>2} = {}".format(n, x, (n * x)))
