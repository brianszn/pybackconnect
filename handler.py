import socket

def init_client():
     HOST = 'localhost'
     PORT = 9992

     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.bind((HOST, PORT))

     s.listen()
     print(f"[*] Handler listening on {HOST}:{PORT}")

     conn, addr = s.accept()
     print(f'Conected: {addr}')

     try:
          while True:
              
               cmd = str(input('cmd> '))
                    
               if cmd == 'exit' or cmd == 'quit':
                    conn.close()
                    print(f'[*] Conection closed.  Reason: User quit')
                    break

               elif not cmd:          
                    continue
               
               conn.sendall(cmd.encode())

               output = b''
               conn.settimeout(1)
               try:
                    while True:

                         part = conn.recv(1024)
                         if not part:
                              break
                                   
                         output = output + part
               except:
                    pass
               print(output.decode(errors='ignore'))
     except:
          print(f'[*] Conection closed.  Reason: Die')

if __name__ == "__main__":
     init_client()
