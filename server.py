import socket #import module socket
 
server_adress=('localhost',5050) #menentukan alamat server
SIZE=1024 #ukuran buffer ketika menerima pesan
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #membuat objek socket
s.bind(server_adress) #bind/mengikat ke alamat server
s.listen(5) #mendengarkan koneksi dari client
 
#menerima pesan terus menerus
while True:
    print("menunggu koneksi")
    client,client_adress=s.accept() #menerima koneksi dari client
    print "connected from : ",client_adress
    while True:
        pesan=raw_input("Anda : ") #memasukan pesan
        client.send(pesan) #mengirim pesan ke client
        pesan=client.recv(1024) #menerima pesan dari client
        print "client:",pesan