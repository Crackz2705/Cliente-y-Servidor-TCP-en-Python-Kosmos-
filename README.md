
TCP Server-Client en Python

Este proyecto implementa un servidor y un cliente TCP que se comunican a través de localhost en el puerto 5000.

Requisitos
- Python 3

Instrucciones

1. Ejecutar el Servidor

	1. Abre una terminal.
	2. Navega hasta el directorio donde se encuentra el archivo `tcp_server.py`.
	3. Ejecuta el servidor con el siguiente comando:
  	```bash
   	python tcp_server.py
   	```
	4. El servidor esperará conexiones en `localhost:5000`.

2. Ejecutar el Cliente

	1. Abre otra terminal.
	2. Navega hasta el directorio donde se encuentra el archivo `tcp_client.py`.
	3. Ejecuta el cliente con el siguiente comando:
   	```bash
   	python tcp_client.py
   	```

3. Pruebas Manuales

	Prueba 1: Enviar un mensaje de texto normal

		1. Con el cliente, ingresa un mensaje de texto (por ejemplo, "hola servidor").
		2. Verifica que el servidor responda con el mensaje en mayúsculas (ej., "HOLA CLIENTE").

	Prueba 2: Enviar el mensaje "DESCONEXION"

		1. Con el cliente, ingresa el mensaje "DESCONEXION".
		2. Verifica que el cliente muestra un mensaje de desconexión y se cierra.
		3. El servidor debe cerrar la conexión con el cliente pero debe continuar disponible para recibir nuevas conexiones.

Ejemplo de Interacción
Conexión establecida:
```
Cliente envía: hola servidor
Servidor responde: HOLA CLIENTE
```

Desconexión:
```
Cliente envía: DESCONEXION
Servidor cierra la conexión con el cliente.
```

Notas
- Ejecutar el servidor y el cliente en ventanas de terminal separadas.
- Cada vez que desees probar una nueva conexión después de "DESCONEXION", ejecuta nuevamente `tcp_client.py`.
