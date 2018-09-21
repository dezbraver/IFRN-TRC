#!/usr/bin/env python3
import os, threading, json, requests, socket, sys

def Recebendo(s):
    while True:
        recebido = s.recv(1024)
        recebido = recebido.decode("utf-8")
        recebido = json.loads(recebido)
        if recebido["msg"] == "SAIR": break
        print("{}: {}\n Mensagem: ".format(recebido["nome"], recebido["msg"]), end= "")
    print("Desconectando...")
    s.close()
    print("Finalizando Aplicaçao...")

def Enviando(s, nome):
    print(" Mensagem: ", end="")
    while True:
        msg = input()
        msg = {
                "flag":"MSG",
                "nome":nome,
                "msg":msg
        }
        if msg["msg"] == "SAIR":
                msg = json.dumps(msg)
                msg = msg.encode("utf-8")
                s.send(msg)
                break
        else:
                msg = json.dumps(msg)
                msg = msg.encode("utf-8")
                s.send(msg)

def Token():
    while True:
        matricula = input("Matricula: ")
        senha = input("Senha: ")
        url_token = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"
        dados = {
            "username":matricula,
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
    os.system("clear")
    return token

def RecuperaNome(token):
    url_dados = "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"
    cabecalho = {
            "Authorization":"JWT {}".format(token)
    }
    resposta = requests.get(url_dados, headers=cabecalho)
    resposta = resposta.content.decode("utf-8")
    resposta = json.loads(resposta)
    nome = resposta["nome_usual"]
    print("Logado como ({})".format(nome))
    print("Digite SAIR para finalizar o programa")
    return nome

def Sock():
    host = "localhost"
    port = 50000

    os.system("clear")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        nome = RecuperaNome(Token())
        reg = {
            "flag":"REG",
            "nome":nome,
            "msg":"pacote de registro"
        }
        reg = json.dumps(reg)
        reg = reg.encode("utf-8")
        s.send(reg)
        threading.Thread(target=Recebendo, args=(s,)).start()
        Enviando(s, nome)

Sock()
