from socket import *
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

msgSemCript = []


# print ("TCP Server\n")
# connectionSocket, addr = serverSocket.accept()
# sentence = connectionSocket.recv(65000)
#while(True):
received = "ovo"
print ("Received From Client: ", received)
for letra in received:
    msgSemCript.append((ord(letra))-3)

print ("Mensagem sem cripto: ", msgSemCript)
    
    

    # capitalizedSentence = sentence.upper() # processamento

    # connectionSocket.send(capitalizedSentence)

    # sent = str(capitalizedSentence,"utf-8")
    # print ("Sent back to Client: ", sent)
    # connectionSocket.close()
