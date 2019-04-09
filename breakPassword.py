import hashlib
import sys
import random

def bruteForce(usr, salt):
	'''
	u = "user"
	p = "12345"
	s = "999999"
	'''

	for pwd in range(0, 1000000000):
		t = usr + ',' + str(pwd) + ',' + salt
		x =  hashlib.sha256(t.encode('utf-8')).hexdigest() 
		if x == "d90b8f91e1c4befcdfdc48c7dac3bcc28cd817ae5a6ef4b1e20b7e19cecd27b1":
			print("x = ", x) 
			print("usr = ", usr, "  pwd = ", pwd, "  salt = ", salt)
			sys.exit()
		if pwd % 1000000 == 0:
			print(pwd//1000000)

	print("pwd = ", pwd)
	print("EXITING")
	sys.exit()

def randomized(usr, salt):
	c = 0
	while True:
		c += 1
		pwd = random.randrange(0,1000000000)
		t = usr + ',' + str(pwd) + ',' + salt
		x =  hashlib.sha256(t.encode('utf-8')).hexdigest() 
		if x == "d90b8f91e1c4befcdfdc48c7dac3bcc28cd817ae5a6ef4b1e20b7e19cecd27b1":
			print("c = ", c)
			print("x = ", x, "  ","pwd = ", pwd)
			break
		if c % 100000 == 0:
			print(c//100000)
		elif c >= 10000000000:
			print("c = ", c)
			print("EXITING")
			sys.exit()

def main():
	usr = "swift"
	salt = "8329942093"
	
	pwd = "587452345"
	t = usr + ',' + pwd + ',' + salt
	x =  hashlib.sha256(t.encode('utf-8')).hexdigest() 
	print("testing :")
	print(x)
	if x == "d90b8f91e1c4befcdfdc48c7dac3bcc28cd817ae5a6ef4b1e20b7e19cecd27b1":
		print("Solved: pwd = ", pwd)
		sys.exit()
	'''	
	if len(sys.argv) == 1:
		bruteForce(usr, salt)
	elif len(sys.argv) == 2:
		if sys.argv[1] == "b":
			bruteForce(usr, salt)
		elif sys.argv[1] == "r":
			randomized(usr, salt)
		else:
			print("b - bruteforce & r - randomized")
	else:
		print("Only 2 arguments please")
	'''

main()