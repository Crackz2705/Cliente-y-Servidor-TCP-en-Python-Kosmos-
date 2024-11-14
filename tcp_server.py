
import socket

def start_server():
    # Configuración del servidor
    server_host = '127.0.0.1'
    server_port = 5000
    
    # Creación del socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)  # Permite hasta 5 conexiones simultáneas
    print(f'Servidor TCP iniciado en {server_host}:{server_port}, esperando conexiones...')

    while True:
        # Acepta una conexión entrante
        client_socket, client_address = server_socket.accept()
        print(f'Conexión establecida con {client_address}')

        while True:
            # Recibe el mensaje del cliente
            message = client_socket.recv(1024).decode()
            if not message:
                break

            print(f'Mensaje recibido: {message}')
            if message.strip().upper() == 'DESCONEXION':
                print(f'Desconexión solicitada por {client_address}')
                client_socket.close()
                break
            elif message.strip().lower() == "hola servidor":
                # Responder "HOLA CLIENTE" solo cuando el mensaje es "hola servidor"
                response = "HOLA CLIENTE"
            else:
                # Responder con el mensaje en mayúsculas en otros casos
                response = message.upper()
            
            client_socket.send(response.encode())

# Ejecuta el servidor
if __name__ == '__main__':
    start_server()
