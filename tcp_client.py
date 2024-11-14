
import socket

def start_client():
    # Configuración del cliente
    server_host = '127.0.0.1'
    server_port = 5000

    # Creación del socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f'Conectado al servidor en {server_host}:{server_port}')

    while True:
        # Solicitar al usuario que ingrese un mensaje
        message = input("Ingrese un mensaje para el servidor (o 'DESCONEXION' para salir): ")
        client_socket.send(message.encode())

        if message.strip().upper() == 'DESCONEXION':
            print("Cerrando la conexión...")
            break

        # Recibir respuesta del servidor
        response = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {response}")

    client_socket.close()

# Ejecuta el cliente
if __name__ == '__main__':
    start_client()
