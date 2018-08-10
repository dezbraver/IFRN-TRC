import os
import re
import datetime

while True:
	while True:
		data_alugado = input("Insira a data em que o carro foi alugado (dd/mm/aaaa ou dd-mm-aaaa): ")
		if re.match("[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]", data_alugado) != None or re.match("[0-3][0-9]-[0-1][0-9]-[1-2][0-9][0-9][0-9]", data_alugado) != None:
			data_alugado_l = re.split("[/-]", data_alugado)
			try:
				data_alugado = datetime.date(int(data_alugado_l[2]), int(data_alugado_l[1]), int(data_alugado_l[0]))
				break
			except ValueError:
				os.system("clear")
				print("Data invalida, tente novamente.")
				pass
		else:
			os.system("clear")
			print("Data invalida, tente novamente.")
	while True:
		data_devolvido = input("Insira a data em que o carro foi devolvido (dd/mm/aaaa ou dd-mm-aaaa): ")
		if re.match("[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]", data_devolvido) != None or re.match("[0-3][0-9]-[0-1][0-9]-[1-2][0-9][0-9][0-9]", data_devolvido) != None:
			data_devolvido_l = re.split("[/-]", data_devolvido)
			try:
				data_devolvido = datetime.date(int(data_devolvido_l[2]), int(data_devolvido_l[1]), int(data_devolvido_l[0]))
				break
			except ValueError:
				os.system("clear")
				print("Data invalida, tente novamente.")
		else:
			os.system("clear")
			print("Data invalida, tente novamente.")
	if data_alugado < data_devolvido:
		dias = data_devolvido - data_alugado
		dias = dias.days
		break
	else:
		os.system("clear")
		print("A data de aluguel eh maior que ou igual a data de devoluçao, tente novamente")

while True:
	try:
		km = float(input("insira a quantidade de Km percorrida (ex: 100.55): "))
		break
	except ValueError:
		os.system("clear")
		print("Insira um valor valido.")

total = (60 * dias) + (0.15 * km)
os.system("clear")
print("Data de Aluguel: \t{0:%d-%m-%Y}\nData de Devoluçao: \t{1:%d-%m-%Y}\nTotal a pagar = \tR${2:.2f}".format(data_alugado, data_devolvido, total))
input("Tecle Enter para sair do programa.")
