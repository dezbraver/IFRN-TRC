# /usr/bin/env python3
import socket, threading, json, requests

online = []

# Funçao que recebe as mensagens, imprime-as e envia como resposta um dicionario contendo 
# o cliente que enviou a mensagem como chave e a sua mensagem como valor associado.
def ReceberRetornar(con, cli):
    while True:
        recebido = con.recv(1024)
        if not recebido: break
        # Ex.: recebido = {"nome":"fulano", "msg":"ola, tudo bem?"}
        recebido = json.loads(recebido)
        recebido = recebido.decode("utf-8")
        print("Recebido{} ({}): {}".format(cli,recebido["nome"], recebido["msg"]))
        enviando = recebido.encode("utf-8")
        for conexao in online:
            enviando = json.dumps(enviando)
            conexao.send(enviando)
    # Em caso do cliente desconectar-se sua conexao eh removida da lista de usuarios online
    # e eh printado que o tal cliente se desconectou, logo em seguida encerra-se a conexao
    online.remove(con)
    print("{} se Desconectou!!!".format(cli))
    con.close()

# Funçao que define o socket do servidor adicionando novas conexoes a lista de usuarios online
# printando que o usuario (cli) se conectou e executando a thread para receber e devolver as
# mensagens
def Servidor():
    host = "127.0.0.1"
    port = 50000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print("Servidor Ligado!")
        while True:
            con, cli = s.accept()
            online.append(con)
            print("{} se conectou!!!".format(cli))
            threading.Thread(target=Receber_Retornar, args=(con, cli))

# Execuçao da funçao principal (Sock)
Servidor()
