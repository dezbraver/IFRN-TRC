from urllib.request import urlopen
import re
import sys
import os

vetor = []
controle = -1

with urlopen('http://www.servicos.blog.br/listas/lista-de-estados-brasileiros-com-siglas-e-capitais/') as response:
	for line in response:
		line = line.decode('utf-8')
		if re.match("<td>[A-Z][A-Z]</td>", line) != None:
			controle = 3
		if controle > 0:
			vetor.append(line.strip('</td>\n'))
		else:
			continue
		controle -= 1

try:
	n = str(sys.argv[1])
	if re.match("[A-Z][A-Z]", n) == None:
		raise ValueError
except (ValueError, IndexError):
	os.system("clear")
	print("Argumento de linha de comando invalido ou inexistente.")
	while True:
		try:
			n = input("Digite a sigla do estado: ")
			if re.match("[A-Z][A-Z]", n) == None:
				raise ValueError
			elif n not in vetor:
				raise ValueError
			break
		except ValueError:
			os.system("clear")
			print("Por Favor digite uma sigla valida.")

print("Estado: {}\nCapital: {}".format(vetor[vetor.index(n) + 1], vetor[vetor.index(n) + 2]))
input("Tecle Enter para finalizar o programa...")
os.system("clear")
