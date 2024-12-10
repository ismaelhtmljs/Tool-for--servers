import socket
import os
import subprocess
import sys
import threading
import time
from colorama import Fore

server_running = threading.Event()
server_running.set()  # Iniciar el servidor (True) al principi

def limpiador():
    input("Presione cualquier tecla para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def new_window_cmd(command):
    if sys.platform == "win32":  # Si es Windows
        subprocess.Popen(['start', 'cmd', '/K', command], shell=True)
    elif sys.platform == "darwin" or sys.platform.startswith("linux"):  # Si es macOS o Linux
        # En Linux puedes usar 'gnome-terminal' o 'xterm', dependiendo de tu sistema
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])  # Para GNOME Terminal
        subprocess.Popen(['xterm', '-e', command])  # Para Xterm

def handle_command():
    global server_running  # Usamos la variable global
    while True:
        try:
            sierre = input("\nPara cerrar el servidor , cierre la ventana")
            if sierre == "close":
                print("Cerrando servidor...")
                stop_server()
                sys.exit()
            else:
                print("\nOpción no válida. Intente nuevamente.")
        except Exception as e:
            print(Fore.RED + f"Error en el manejo de comandos: {e}")

def handle_client(conn,addr):
    with conn:
        print(f"Conexión establecida con {addr}")
        while True:
            try:
                data = conn.recv(1024)  # Recibe datos del cliente
                if not data:  # Si no hay datos, la conexión se cierra
                    break
                print(f"Datos recibidos de {addr}: {data.decode('utf-8')}")
            except Exception as e:
                print(Fore.RED + f"Error al recibir datos de {addr}: {e}")
                break

def dir():
    directorio = os.getcwd()
    archivos = os.listdir(directorio)

    for archivo in archivos:
        print(archivo)
    limpiador()

def navegar():
    print(Fore.GREEN + "EJEMPLO : C:/Ruta/de/su/archivo")
    path = input("Coloque la ruta en la que desea moverse : ")
    path = path.replace("/","\\")

    # verificar si la direccion existe
    if os.path.exists(path):
        os.chdir(path)
        print(Fore.CYAN + f"Ahora se encuentra en {path}")
        limpiador()
    else: 
        print(Fore.RED + "El directorio no existe. Asegúrate de que la ruta sea correcta.")
        limpiador()

def Separador():
    sepad = Fore.LIGHTYELLOW_EX + "-" * 85 
    print(sepad)

def stop_server():
    server_running.clear()

def notFound():
    print(Fore.RED + "ERROR 404 : no se encontro la opcion que coloco")
    limpiador()

def Program():
    while True:
        print(Fore.GREEN + """
        /// ╔════════════════════════════════════════════════════════════════╗
        /// ║     _______.  ______     ______  __  ___  _______ .___________.║
        /// ║    /       | /  __  \   /      ||  |/  / |   ____||           |║
        /// ║   |   (----`|  |  |  | |  ,----'|  '  /  |  |__   `---|  |----`║
        /// ║    \   \    |  |  |  | |  |     |    <   |   __|      |  |     ║
        /// ║.----)   |   |  `--'  | |  `----.|  .  \  |  |____     |  |     ║
        /// ║|_______/     \______/   \______||__|\__\ |_______|    |__|     ║
        /// ║                                                                ║
        /// ║.___________.  ______ .______                                   ║
        /// ║|           | /      ||   _  \                                  ║
        /// ║`---|  |----`|  ,----'|  |_)  |                                 ║
        /// ║    |  |     |  |     |   ___/                                  ║
        /// ║    |  |     |  `----.|  |                                      ║
        /// ║    |__|      \______|| _|                                      ║
        /// ╚════════════════════════════════════════════════════════════════╝
        
        
                                ,======================.
                                |         TPC         |
                                |.-------------------.|  
                                ||[ _ o . . _ ]_||  
                                |`-------------------'|  
                                || ||  
                                |`-------------------'|  
                                || ||  
                                |`-------------------'|  
                                || ||  
                                |`-------------------'|  
                                ||[=========]| o (@) |  
                                |`---------=='/u\ --- |  
                                |-------_--------------|  
                                | (/) (_) []|  
                                |---==--==----------==|  
                                |||||||||||||||||||||||  
                                |||||||||||||||||||||||  
                                |||||||||||||||||||||||  
                                |||||||||||||||||||||||  
                                |||||||||||||||||||||||  
                                |||||||||||||||||||||||  
                                |||||||||||||||||||||||  
                                |||||||||||||||||||||||  
                                |||||||||||||||||||||||  
                                || ...  
                                |||||||||||||||||||||||  
                                |======================|  
        """)
        print(Fore.LIGHTYELLOW_EX + "\nRECOMENDACION : Primero iniciar en el lado del cliente y luego inciar el servidor\n")
        print("\nRECOMENDACION : Antes de ejecutar el servidor, verifique en que directorio se encuntra, si no se encuentra en el directorio de 'Tool-for-the-serves' tendra que navegar a ese directorio para que funcione el lado del Cliente\n")
        print("Para salir coloque 'exit' ")
        Separador()
        print(Fore.MAGENTA + "# Opcion de Servidores(Servidor) : \n")
        print(Fore.RED + "# [1]Iniciar Servidor TCP #")
        print(Fore.RED + "# [2]Iniciar Servidor UDP #")
        print(Fore.MAGENTA + "\nTest para conexion con los servidores(Cliente) : \n")
        print(Fore.CYAN + "# [3]Conectar con el Servidor TCP #")
        print(Fore.CYAN + "# [4]Conectar con el Servidor UDP #")
        print(Fore.MAGENTA + "\nNavegacion: \n")
        print(Fore.GREEN + "[5] Ver Archivos")
        print(Fore.GREEN + "[6] Moverse de Escritorio")
        Separador()
        respuesta = input("Su Opcion : ")

        # Condición para las opciones
        if respuesta == "1":
            print("[1]Servidor Ipv4")
            print("[2]Servidor Ipv6")
            print("[3]Volver")
            respuesta_2 = input("Su Opcion : ")

            if respuesta_2 == "1":
                host_input = socket.gethostbyname(socket.gethostname())
                port_entry = int(input("Coloque el puerto deseable : "))  # Convertir a int
                listen_num = int(input("¿Cuántas conexiones simultáneas desea que se acepten? : "))  # Convertir a int

                try : 
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCP:
                        TCP.bind((host_input, port_entry))
                        TCP.listen(listen_num)
                        print(f"Esperando conexiones en {host_input}:{port_entry}...")
                        while server_running:  # Mientras el servidor siga en ejecución
                            conn, addr = TCP.accept()  # Acepta una nueva conexión
                            # Crear un hilo para el manejo de comandos
                            command_thread = threading.Thread(target=handle_command)
                            command_thread.start()
                            threading.Thread(target=handle_client, args=(conn, addr)).start()
                        print("Servidor detenido.")

                except Exception as e:
                    print(Fore.RED + f"Error al establecer la conexión: {e}")
                    limpiador()

            elif respuesta_2 == "2":
                host_input = "::1"
                port_entry = int(input("Coloque el puerto deseable : "))  # Convertir a int
                listen_num = int(input("¿Cuántas conexiones simultáneas desea que se acepten? : "))  # Convertir a int

                try:
                    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as TCP:
                        TCP.bind((host_input, port_entry))
                        TCP.listen(listen_num)
                        print(f"Esperando conexiones en {host_input}:{port_entry}...")
            
                        while server_running:  # Mientras el servidor siga en ejecución
                            conn, addr = TCP.accept()  # Acepta una nueva conexión
                            # Crear un hilo para el manejo de comandos
                            command_thread = threading.Thread(target=handle_command)
                            command_thread.start()
                            threading.Thread(target=handle_client, args=(conn, addr)).start()
                        print("Servidor detenido.")
            
                except Exception as e:
                    print(Fore.RED + f"Error al establecer la conexión: {e}")
            elif respuesta_2 == "3":
                limpiador()
            else:
                notFound()

        elif respuesta == "2":
            limpiador()
            print("[1]Servidor Ipv4")
            print("[2]Servidor Ipv6")
            print("[3]Volver")
            respuesta_3 = input("Su Opcion : ")

            if respuesta_3 == "1":
                host_input = socket.gethostbyname(socket.gethostname())
                port_entry = int(input("Coloque el puerto deseable : "))  # Convertir a int
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDP:
                    UDP.bind((host_input, port_entry))
                    print(f"Esperando datos en {host_input}:{port_entry}...")
                    while server_running:  # Mientras el servidor siga en ejecución
                            conn, addr = TCP.accept()  # Acepta una nueva conexión
                            # Crear un hilo para el manejo de comandos
                            command_thread = threading.Thread(target=handle_command)
                            command_thread.start()
                            threading.Thread(target=handle_client, args=(conn, addr)).start()
                            print("Servidor detenido.")

            elif respuesta_3 == "2":
                host_input = socket.gethostbyname(socket.gethostname())
                port_entry = int(input("Coloque el puerto deseable : "))  # Convertir a int

                with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as UDP:
                    UDP.bind((host_input, port_entry))
                    print(f"Esperando datos en {host_input}:{port_entry}...")
                    while server_running:  # Mientras el servidor siga en ejecución
                            conn, addr = TCP.accept()  # Acepta una nueva conexión
                            # Crear un hilo para el manejo de comandos
                            command_thread = threading.Thread(target=handle_command)
                            command_thread.start()
                            threading.Thread(target=handle_client, args=(conn, addr)).start()
                            print("Servidor detenido.")
            elif respuesta_3 == "3":
                limpiador()
            else: 
                notFound()

        elif respuesta == "3":
            new_window_cmd('python3 cliente_window_tcp.py')
            limpiador()

        elif respuesta == "4":
            new_window_cmd('python3 client_window_udp.py')
            limpiador()
        
        elif respuesta == "exit" : 
            print("saliendo")
            time.sleep(0.8)
            for i in range(3):
                print(".", end=" ", flush=True)
                time.sleep(0.5)
            sys.exit()
        
        elif respuesta == "5":
            dir()
        
        elif respuesta == "6":
            navegar()
        
        else:
            notFound()

if __name__ == "__main__":
    Program()