import socket



def Main():
    #codes adapted from https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
    host = "206.87.171.182"
    port = 5000

    mySocket = socket.socket() #create socket point for server
    mySocket.bind((host,port)) #bind host and port

    mySocket.listen(10) #server is listening
    conn, addr = mySocket.accept() #server is acceping any info from client1
    print ("Connection from: " + str(addr))

    mySocket.listen(10) #server if listening
    conn2, addr2 = mySocket.accept() #server is acceping any info from client2

    print ("Connection from: " + str(addr2))
    while True: #infinite loop to constantly receive info
            data = conn.recv(1025).decode() #incoming info from client1 stored in data
            if not data:
                    break
            print ("from connected  user: " + str(data))

            print ("sending: " + str(data))

            conn2.send(data.encode()) #send data back to client2

            data = conn2.recv(1024).decode() #incoming info from client2 stored in data
            if not data:
                    break
            print ("from connected  user: " + str(data))

            print ("sending: " + str(data))
            conn.send(data.encode()) #send data back to client1


    conn.close() #close connection



if __name__ == '__main__':
    Main()
