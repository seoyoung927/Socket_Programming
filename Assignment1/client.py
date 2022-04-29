from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input('Input lowercase/uppercase sentence:')
    if(message.islower()):
        break
    elif(message.isupper()):
        break
    print("Message should be lowercase or uppercase.")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()