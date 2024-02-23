from socket import *
import datetime
serverName = "172.20.10.3"
serverPort = 1300

def abreSocket():
    clientSocket.connect((serverName, serverPort))

def fechaSocket():
    clientSocket.close()

def enviaR2(R2):
    clientSocket.send(bytes(str(R2), "utf-8"))

def recebeR1():
    msg_R1 = clientSocket.recv(65000)
    return str(msg_R1,"utf-8")

def trocaLetra(letra,chave):
    nroLetra = ord(letra) + chave
    return chr(nroLetra)

def criptDecript(texto,chave,decript):
    textoAlterado = ""
    if (decript): 
        chave = -chave

    for caract in texto:
            textoAlterado += trocaLetra(caract,chave)
    return textoAlterado

def obtemChaveDiffieHellmann():
    R2 = (G ** Y) % N
    enviaR2(R2)
    print ("enviou R2 ", R2, datetime.datetime.now())
    R1 = recebeR1()
    print ("recebeu R1 ", R1, datetime.datetime.now())
    K = (int(R1) ** Y) % N
    print("K: ", K)
    return K

clientSocket = socket(AF_INET, SOCK_STREAM)
G = 11
N = 23
Y = 1340000

abreSocket()

K = obtemChaveDiffieHellmann()

msg = input("Mande uma mensagem: ")
msgCript = criptDecript(msg, K, False)
print ("Mensagem original: ", msg)
print ("Mensagem criptografada enviada: ", msgCript)
clientSocket.send(bytes(msgCript, "utf-8"))

fechaSocket()
