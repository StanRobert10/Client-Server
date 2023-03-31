import socket
import os

# Crearea unui socket nou pentru aplicatia de server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectarea socketului creat la adresa si portul clientului
server.connect(("localhost", 4096))

# Trimiterea unui mesaj catre server pentru a incepe procesul
Continue = 'y'
server.send(Continue.encode())

# Loop-ul pentru parcurgerea repetata a progresiei
while Continue == 'y':

    # Trimiterea numerelor catre server pentru a fi efectuat calculul progresiei
    Message = input("Introduceti numerele necesare progresiei separate prin virgule, exemplu: 1,2,3,4,5,6\n:")
    server.send(Message.encode())

    # Primirea mesajului de la server server cu rezultatul progresiei si afisarea mesajului
    Message = server.recv(1024).decode()
    print(Message)

    # Optiunea de a repeta procesul si curatarea terminalului
    Continue = input("\nDoriti sa repetati procesul? y/n  ")
    os.system("cls")
    if Continue == 'n':
        server.send(Continue.encode())
