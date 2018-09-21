#!/usr/bin/python3
import socket, threading, json, requests

# Lista de usuarios online
online = []

# Funçao que recebe as mensagens, imprime-as e envia como resposta um dicionario contendo 
# o cliente que enviou a mensagem como chave e a sua mensagem como valor associado.
def Receber_Retornar(con, cli):
    nome = ""
    while True:
        recebido = con.recv(1024)
        if not recebido: break
        recebido = recebido.decode("utf-8")
        # Ex.: recebido = {"nome":"fulano", "msg":"ola, tudo bem?"}
        recebido = json.loads(recebido)
        if recebido["msg"] == "SAIR":
            nome = recebido["nome"]
            enviando = json.dumps(recebido)
            enviando = enviando.encode("utf-8")
            con.send(enviando)
        else:
            if recebido["flag"] == "REG":
                print("REG - Nova Conexao: {}-{}".format(cli, recebido["nome"]))
            else:
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

# Funçao que define o socket do servidor adicionando novas conexoes a lista de usuarios online
# printando que o usuario (cli) se conectou e executando a thread para receber e devolver as
# mensagens
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
            #print("{} se conectou!!!".format(cli))
            threading.Thread(target=Receber_Retornar, args=(con, cli)).start()

# Execuçao da funçao principal (Sock)
Sock()
