import socket 
host = '192.168.3.100' 
port = 80
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(10) 
while True:
    con, cliente = serv_socket.accept() 
    print('conectado' )
    with open("index.html",'rb') as index:
        con.send(index.read())
    print("aguardando mensagem")
    recebe = con.recv(1024) 
    print("mensagem recebida: "+ recebe)