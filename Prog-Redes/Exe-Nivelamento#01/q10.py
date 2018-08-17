#!/usr/bin/env python3
import os
from collections import deque

vetor = []
vetor = deque(vetor)
while True:
	try:
		n = int(input("Digite um numero: "))
		if n == 0:
			break
		else:
			if len(vetor) == 5:
				vetor.popleft()
			vetor.append(n)
	except ValueError:
		print("O valor digitado eh invalido, tente novamente.")
os.system("clear")
for elem in vetor:
	print(elem, end = " // ")
print()
