#!/usr/bin/python3
import socket, threading, json, requests

# Lista de usuarios online
online = []

# Funçao que recebe as mensagens, imprime-as e envia de volta ao cliente um dicionario contendo o tipo da mensagem (flag) cliente que enviou a mensagem como chave e a sua mensagem como valor associado.
def Receber_Retornar(con, cli):
    # Variavel para armazenar o nome do cliente para ser usado depois que ele eh desconectado
    nome = ""
    while True:
        recebido = con.recv(1024)
        if not recebido: break
        recebido = recebido.decode("utf-8")
        # Ex.: recebido = {"flag":"MSG", "nome":"fulano", "msg":"ola, tudo bem?"}
        recebido = json.loads(recebido)
        # Se o cliente enviar SAIR ele envia de volta para fechar a thread de receber dados
        if recebido["msg"] == "SAIR":
            nome = recebido["nome"]
            enviando = json.dumps(recebido)
            enviando = enviando.encode("utf-8")
            con.send(enviando)
        else:
            # No inicio da aplicaçao cliente ele envia a mensagem com flag = REG para ser printada a nova conexao
            if recebido["flag"] == "REG":
                print("REG - Nova Conexao: {}-{}".format(cli, recebido["nome"]))
            else:
                # Caso a flag seja igual a MSG printa a mensagem e a envia para todas as conexoes online
                print("Recebido {}-{}: {}".format(cli,recebido["nome"], recebido["msg"]))
                for conexao in online:
                    enviando = json.dumps(recebido)
                    enviando = enviando.encode("utf-8")
                    conexao.send(enviando)
    # Em caso do cliente desconectar-se sua conexao eh removida da lista de usuarios online
    # e eh printado que o tal cliente se desconectou, logo em seguida encerra-se a conexao
    online.remove(con)
    print("REG - Desconectado: {}-{}".format(cli, nome))
    con.close()

# Funçao que define o socket do servidor adicionando novas conexoes a lista de usuarios online e executando a thread de receber e retornar
def Sock():
    host = "127.0.0.1"
    port = 50000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print("Servidor Ligado!")
        while True:
            con, cli = s.accept()
            online.append(con)
            threading.Thread(target=Receber_Retornar, args=(con, cli)).start()

# Chamada a funçao principal (Sock)
Sock()
