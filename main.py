'''import os

from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
	return "Hello, World!"

if __name__ == "__main__":
	app.run(debug=False)'''

import csv

def data_entry():
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

def check():
	un = raw_input("Username: ")
	pw = raw_input("Password: ")
	correct = False
	for i, item in enumerate(email):
		if item==un:
			if pw==password[i]:
				#authorized
				correct = True
			else:
				print("GO AWAY!")
	if not correct:
		print("GO AWAY!")
	return correct

def main():
