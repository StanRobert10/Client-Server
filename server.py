import socket


# Functia pentru progresia aritmetica
def pa(list_of_nr):
    length = len(list_of_nr)
    for i in range(0, length - 1):
        if list_of_nr[i + 1] - list_of_nr[i] != (list_of_nr[1] - list_of_nr[0]):
            return False
    return True


# Functia pentru progresia geometrica
def pg(list_of_nr):
    length = len(list_of_nr)
    for i in range(0, length - 1):
        if list_of_nr[i + 1] / list_of_nr[i] != (list_of_nr[1] / list_of_nr[0]):
            return False
    return True


# Creaza un socket nou pentru aplicatia server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Asocierea socketului server cu adresa si portul clientului
server.bind(("localhost", 4096))
# Declararea numarului maxim de conexiuni posibile
server.listen(1)
# Acceptarea conexiunii si crearea noului socket necesar comunicarii cu clientul
ClientSocket, ClientAddress = server.accept()
print(f"Conexiunea cu clientul {ClientAddress} a fost stabilita!")

Received_Message = ClientSocket.recv(1024).decode()
Continue = Received_Message

while Continue == 'y':
    Received_Message = ClientSocket.recv(1024).decode()

    # In aceast if se realizeaza intreruperea conexiunii dintre client si server si respectiv inchiderea serverului
    if Received_Message == 'n':
        server.close()
        print(f"Conexiunea cu clientul {ClientAddress} a fost intrerupta!")
        break

    # Transformarea numerelor primite de la client intr-o lista pentru a fi folotita in realizarea progresiei
    list_of_numbers = list(map(float, Received_Message.split(",")))

    # Utilizarea functiilor progresiei aritmetice/geometrice
    if pa(list_of_numbers):
        SendMessage = f"A({int(list_of_numbers[1] - list_of_numbers[0])})"
        ClientSocket.send(SendMessage.encode())

    elif pg(list_of_numbers):
        SendMessage = f"G({int(list_of_numbers[1] / list_of_numbers[0])})"
        ClientSocket.send(SendMessage.encode())

    else:
        SendMessage = 'N'
        ClientSocket.send(SendMessage.encode())
