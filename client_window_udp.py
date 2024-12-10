import socket
from colorama import Fore

def window_client_UDP():
    print("[1]Conectar con Servidor Ipv4")
    print("[2]Conectar con Servidor Ipv6")
    respuesta_cliente = input(": ")

    if respuesta_cliente == "1":
        # Entrada de la IP y el puerto
        host_entry = input(Fore.GREEN + "Coloque la IP del servidor: ")
        port_entry = input(Fore.LIGHTYELLOW_EX + "Coloque el puerto del servidor: ")

        # Verificar si el cliente rellenó los campos
        if not host_entry or not port_entry:
            print(Fore.RED + "Error: Debes completar ambos campos (IP y puerto).")
            return
        
        # Convertir el puerto a entero y validar
        try:
            port_entry = int(port_entry)
            if port_entry < 1 or port_entry > 65535:
                print(Fore.RED + "Error: El puerto debe ser un número entre 1 y 65535.")
                return
        except ValueError:
            print(Fore.RED + "Error: El puerto debe ser un número válido.")
            return
        
        # Crear el socket para el cliente
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            # Conectar al servidor
            server.connect((host_entry, port_entry))
            print(Fore.CYAN + f"Conectado al servidor {host_entry}:{port_entry}")

            # Enviar mensaje de conexión exitosa
            server.sendall(b"Conexion exitosa")  # Asegúrate de enviar los datos como bytes

            # Recibir respuesta del servidor
            response = server.recv(1024)  # Recibe hasta 1024 bytes del servidor
            print(Fore.YELLOW + f"Respuesta del servidor: {response.decode('utf-8')}")

        except ConnectionRefusedError:
            print(Fore.RED + "Error: No se pudo conectar al servidor.")
        except Exception as e:
            print(Fore.RED + f"Se produjo un error: {e}")
        finally:
            # Cerrar la conexión
            server.close()
            print(Fore.MAGENTA + "Conexión cerrada.")

    elif respuesta_cliente == "2":
        # Entrada de la IP y el puerto
        host_entry = input(Fore.GREEN + "Coloque la IP del servidor: ")
        port_entry = input(Fore.LIGHTYELLOW_EX + "Coloque el puerto del servidor: ")

        # Verificar si el cliente rellenó los campos
        if not host_entry or not port_entry:
            print(Fore.RED + "Error: Debes completar ambos campos (IP y puerto).")
            return
        
        # Convertir el puerto a entero y validar
        try:
            port_entry = int(port_entry)
            if port_entry < 1 or port_entry > 65535:
                print(Fore.RED + "Error: El puerto debe ser un número entre 1 y 65535.")
                return
        except ValueError:
            print(Fore.RED + "Error: El puerto debe ser un número válido.")
            return

        # Crear el socket para el cliente
        server = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

        try:
            # Conectar al servidor
            server.connect((host_entry, port_entry))
            print(Fore.CYAN + f"Conectado al servidor {host_entry}:{port_entry}")

            # Enviar mensaje de conexión exitosa
            server.sendall(b"Conexion exitosa")  # Asegúrate de enviar los datos como bytes

            # Recibir respuesta del servidor
            response = server.recv(1024)  # Recibe hasta 1024 bytes del servidor
            print(Fore.YELLOW + f"Respuesta del servidor: {response.decode('utf-8')}")

        except ConnectionRefusedError:
            print(Fore.RED + "Error: No se pudo conectar al servidor.")
        except Exception as e:
            print(Fore.RED + f"Se produjo un error: {e}")
        finally:
            # Cerrar la conexión
            server.close()
            print(Fore.MAGENTA + "Conexión cerrada.")

# Llamada a la función
window_client_UDP()
