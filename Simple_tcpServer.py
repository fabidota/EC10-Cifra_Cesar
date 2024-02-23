from socket import *
# FUNÇÔES
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
        



# Configuração do servidor
serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.

# Configuração da cifra
G = 11
N = 23
x = 1250000

R1 = (G**x) % N

# print ("TCP Server\n")
# connectionSocket, addr = serverSocket.accept()
# sentence = connectionSocket.recv(65000)
#while(True):
received = "ovo"
print ("Received From Client: ", received)
chave = 3
msgCripto = criptDecript(received,chave,False)
print ("Mensagem cripto: ", msgCripto)
print ("Mensagem decripto: ", criptDecript(msgCripto,chave,True))

    

    # capitalizedSentence = sentence.upper() # processamento

    # connectionSocket.send(capitalizedSentence)

    # sent = str(capitalizedSentence,"utf-8")
    # print ("Sent back to Client: ", sent)
    # connectionSocket.close()

    