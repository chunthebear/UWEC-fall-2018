import socket
import csv

#read data file
with open('testfile.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
    # 9 items: ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'position', 'Joined', 'password']
id=[]
first=[]
last=[]
email=[]
gender=[]
ip=[]
position=[]
date=[]
password=[]

#store data separately into lists
for i, item in enumerate(data):
    if i==0:
        continue
    id.append(item[0])
    first.append(item[1])
    last.append(item[2])
    email.append(item[3])
    gender.append(item[4])
    ip.append(item[5])
    position.append(item[6])
    date.append(item[7])
    password.append(item[8])

#check if username and password match or not
def check():
    un = input("Username: ")
    pw = input("Password: ")
    correct = False
    for i, item in enumerate(email):
        if item==un:
            if pw==password[i]:
                #authorized
                correct = True
            #else:
            #    print("Incorrect Password.")
    if not correct:
        print("Incorrect Username or Password.")
    return correct

def Main():
    while True:
        if check(): #only execute when username and password match
            #codes adapted from https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
            host = '206.87.171.182'
            port = 5000

            mySocket = socket.socket() #create socket point for client
            mySocket.connect((host,port)) #connect to server

            message = 2 #input info

            while message != 'q':
                    data = mySocket.recv(1024).decode() #receive info from server
                    print ('Received from server: ' + data)
                    message = input(" -> ") #input info
                    mySocket.send(message.encode()) #send info to server

                    message = 2

            mySocket.close() #close connection

if __name__ == '__main__':
    Main()
