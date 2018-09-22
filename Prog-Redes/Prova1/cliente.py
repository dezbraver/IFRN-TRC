#!/usr/bin/env python3
import os, threading, json, requests, socket

# Funçao que recebe as mensagens (se a mensagem eh SAIR ele desconecta e encerra o programa) se nao ele printa quem esta logado e printa todas as mensagens armazenadas no servidor
def Recebendo(s, nome):
    while True:
        recebido = s.recv(1024)
        recebido = recebido.decode("utf-8")
        recebido = json.loads(recebido)
        if len(recebido) > 0:
            if recebido[0]["msg"] == "SAIR": break
            else:
                os.system("clear")
                print("Logado como ({})".format(nome))
                for mensagem in range(len(recebido)):
                    print("{}: {}".format(recebido[mensagem]["nome"], recebido[mensagem]["msg"]))
                print("\nDigite SAIR e tecle enter para finalizar o programa.\n\tMensagem: ", end = "")
        else:
            pass
    print("Desconectando...")
    s.close()
    print("Finalizando Aplicaçao...")

# Funçao que printa quem esta logado e envia as mensagens. Sua execuçao eh encerrada quando o usuario digita SAIR
def Enviando(s, nome):
    print("Logado como ({})".format(nome))
    print("\tMensagem: ", end="")
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

# Funçao que recupera o token de acesso do par usuario/senha do suap se nao conseguir retornar o token printa que o usuario eh invalido
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

# Funçao que retorna o nome usual do usuario se o mesmo obtiver o token com sucesso pois precisa do token em seus parametros
def RecuperaNome(token):
    url_dados = "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"
    cabecalho = {
            "Authorization":"JWT {}".format(token)
    }
    resposta = requests.get(url_dados, headers=cabecalho)
    resposta = resposta.content.decode("utf-8")
    resposta = json.loads(resposta)
    nome = resposta["nome_usual"]
    return nome

# Funçao principal que cria o socket e o conecta ao servidor, envia mensagem de registro ao servidor indicando o nome de quem esta se conectando, inicia a thread de recebimento e  executa a funçao de envio
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
        threading.Thread(target=Recebendo, args=(s,nome)).start()
        Enviando(s, nome)

# Chamada a funçao principal
Sock()
