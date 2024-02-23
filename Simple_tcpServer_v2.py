from socket import *
import datetime
import time
serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)

def abreSocket():
    serverSocket.bind(("",serverPort))
    serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.

def enviaR1(R1):
    connectionSocket.send(bytes(str(R1), "utf-8"))

def recebeR2():
    msg_R2 = connectionSocket.recv(65000)
    return str(msg_R2,"utf-8")

def fechaSocket():
    connectionSocket.close()

def trocaLetra(letra,chave):
    #nroLetra = ord(letra) + chave
    nroLetra = ord(letra) + chave
    return chr(nroLetra)

def criptDecript(texto,chave,decript):
    textoAlterado = ""
    if (decript): 
        chave = -chave

    for caract in texto:
            textoAlterado += trocaLetra(caract,chave)
    return textoAlterado

def obtemChaveDiffieHellman():
    R1 = (G ** X) % N
    time.sleep(1)
    R2 = recebeR2()
    print ("recebe R2 ", R2, datetime.datetime.now())
    time.sleep(1)
    enviaR1(R1)
    print ("envia R1 ", R1, datetime.datetime.now())
    K = (int(R2) ** X) % N
    print("K1: ", K)
    return K

clientSocket = socket(AF_INET, SOCK_STREAM)
G = 11
N = 23
X = 1250000
K = 3

print ("TCP Server em Execução \n")

abreSocket()
connectionSocket, addr = serverSocket.accept()

K = obtemChaveDiffieHellman()

msgCript = connectionSocket.recv(65000)
msgCriptUnicode = str(msgCript,"utf-8")
msg = criptDecript(msgCriptUnicode, K, True)
print ("Mensagem criptografada recebida: ", msgCriptUnicode)
print ("Mensagem decriptografada : ", msg)

fechaSocket()
