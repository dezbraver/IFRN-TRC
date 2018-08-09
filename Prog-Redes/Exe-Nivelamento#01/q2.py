import re
import datetime

while True:
	#try:
	data_alugado = input("Insira a data em que o carro foi alugado (dd/mm/aaaa ou dd-mm-aaaa)")
	if re.match("[0-3][0-9][/-][0-1][0-9][/-][1-2][0-9][0-9][0-9]", data_alugado) != None:
		#fazer os ifs para limitar o dia mês e ano
		print(data_alugado)
		#break
		#data_alugado_lista = re.split("[/-]", data_alugado)
		#if len(data_alugado_l) == 3:
#
#data_devolvido = input("Insira a data em que o carro foi devolvido (dd/mm/aaaa ou dd-mm-aaaa)")
#km_percorridos = input("Insira a quantidade de Km Percorrida")
#
#try:
