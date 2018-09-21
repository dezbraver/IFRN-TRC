#/usr/bin/env python3
import os, threading, json, requests
from socket import socket

def Recebendo(s):
    while True:
        recebido = s.recv(1024)
        recebido = json.loads(recebido)
        recebido = recebido.decode("utf-8")
        print("{}: {}".format(recebido["nome"], recebido["msg"]))

def Enviando(s, nome):
    while True:
        msg = input("Mensagem: ")
        if msg == "Sair": break
        msg = {
                "nome":nome,
                "msg":msg
        }
        msg = msg.encode("utf-8")
        msg = json.dumps(msg)
        s.send(msg)
    print("Desconectando...")
    s.close()
    input("Tecle Enter para finalizar o programa...")
    print("Finalizando Aplicaçao...")

def Token(usuario, senha):
    while True:
        matricula = input("Matricula: ")
        senha = input("Senha: ")
        url_token = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"
        dados = {
            "username":usuario,
            "password":senha
        }
        token = requests.post(url_token, data=dados)
        if token.status_code == 200:
            token = token.content.decode("utf-8")
            token = json.loads(token)
            token = token["token"]
            break
        else:
            print("Usuario ou senha invalidos")
    return token

def RecuperaNome(token)
    url_dados = "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"
    cabecalho = {
            "Authorization":"JWT {}".format(token)
    }
    resposta = requests.get(url_dados, headers=cabecalho)
    resposta = resposta.content.decode("utf-8")
    resposta = json.loads(resposta)
    nome = resposta["nome_usual"]
    return nome

def Sock():
    host = "localhost"
    port = 50000

    os.system("clear")
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((host, port))
        Enviando(s, RecuperaNome(Token()))
        threading.Thread(target=Recebendo, args=(s,))

Sock()
