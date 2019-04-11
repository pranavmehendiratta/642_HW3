from hashlib import sha256
import binascii
import sys
import time

'''
combMAX = {
	"a" : ["a", "A", "@", "4", "^"],
	"b" : ["b", "B", "8", "6"],
	"c" : ["c", "C", "(", "[", "{", "<"],
	"d" : ["d", "D", ")", "]", "}"],
	"e" : ["e", "E", "3", "}"],
	"f" : ["f", "F"],
	"g" : ["g", "G", "6", "9","&"],
	"h" : ["h", "H", "#"],
	"i" : ["i", "I", "|", "1", "!", ":", ";", "7", "/", "\\"],
	"j" : ["j", ";", "?"],
	"k" : ["k", "K"],
	"l" : ["l", "L", "|", "1", "/". "\\"],
	"m" : ["m", "M"],
	"n" : ["n", "N"],
	"o" : ["o", "O", "0"],
	"p" : ["p", "P", "9", "?"],
	"q" : ["q", "Q", "9", "0"],
	"r" : ["r", "R"],
	"s" : ["s", "S", "$", "2", "5"],
	"t" : ["t", "T", "7", "|", "/", "\\"],
	"u" : ["u", "U"],
	"v" : ["v", "V"],
	"w" : ["w", "W"],
	"x" : ["x", "X", "+", "%", "*"],
	"y" : ["y", "Y"],
	"z" : ["z", "Z", "2", "7", ">"]
}
'''
'''
combMID = {
	"a" : ["a", "A", "@", "4"],
	"b" : ["b", "B", "8", "6"],
	"c" : ["c", "C", "(", "["],
	"d" : ["d", "D"],
	"e" : ["e", "E", "3"],
	"f" : ["f", "F"],
	"g" : ["g", "G", "6", "9"],
	"h" : ["h", "H", "#"],
	"i" : ["i", "I", "|", "1", "!"],
	"j" : ["j", "J", ";"],
	"k" : ["k", "K"],
	"l" : ["l", "L", "|", "1"],
	"m" : ["m", "M"],
	"n" : ["n", "N"],
	"o" : ["o", "O", "0"],
	"p" : ["p", "P"],
	"q" : ["q", "Q", "9", "0"],
	"r" : ["r", "R"],
	"s" : ["s", "S", "$", "5"],
	"t" : ["t", "T", "7", "|"],
	"u" : ["u", "U"],
	"v" : ["v", "V"],
	"w" : ["w", "W"],
	"x" : ["x", "X", "*"],
	"y" : ["y", "Y"],
	"z" : ["z", "Z", "2"]
}
'''
#combMIN
comb = {
	"a" : ["a", "A", "@"],
	"b" : ["b", "B"],
	"c" : ["c", "C"],
	"d" : ["d", "D"],
	"e" : ["e", "E"],
	"f" : ["f", "F"],
	"g" : ["g", "G"],
	"h" : ["h", "H", "#"],
	"i" : ["i", "I", "1", "!"],
	"j" : ["j", "J"],
	"k" : ["k", "K"],
	"l" : ["l", "L"],
	"m" : ["m", "M"],
	"n" : ["n", "N"],
	"o" : ["o", "O", "0"],
	"p" : ["p", "P"],
	"q" : ["q", "Q"],
	"r" : ["r", "R"],
	"s" : ["s", "S", "$"],
	"t" : ["t", "T"],
	"u" : ["u", "U"],
	"v" : ["v", "V"],
	"w" : ["w", "W"],
	"x" : ["x", "X"],
	"y" : ["y", "Y"],
	"z" : ["z", "Z"]
}


def generateCombinations(word):
	l = []
	count = 0
	n1 = []
	n1.append((word, count))
	while count < 4:
		n2 = []
		for i in range(0, len(n1)):
			n2 += change1(n1[i][0], n1[i][1])
		l += n2
		n1 = n2
		count += 1
	l = [x[0][0:len(x[0])-1] for x in l]
	l = list(set(l))
	return l

def change1(word, count):
	l = []
	count += 1
	if count > 4:
		return l
	else:
		for i in range(0, len(word)):
			if word[i] in comb:
				var = comb[word[i]]
				for j in range(0, len(var)):
					w = word[:i] + var[j] + word[i + 1:]
					l.append((w, count))
		l = list(set(l))
		return l

#file generated is too large not worth it
def makePwdList(filename):
	file = open(filename, "r")
	pwdFile = open("pwdFile.txt", "w+")
	l = file.readlines()
	pwds = []
	i = 0
	for w in l:
		i += 1
		pwds = generateCombinations(w)
		for pwd in pwds:
			pwdFile.write(pwd)
		print(str(i)+ "/"+ str(len(l)))

def getHash(usr, pwd, salt):
		#x = 'swift,password,84829348943'
		x = usr + "," + pwd + "," + salt 
		for _ in range(0, 256):
			x = sha256(x).digest()
		return x.encode('hex')	 

def breakUP(filename):
	file = open(filename, "r")
	l = file.readlines()
	files = []
	i = 1
	c = 0
	nFile = "words" + str(i) + ".txt"
	files.append(nFile)
	wFile = open(nFile, "w+")
	for w in l:
		wFile.write(w)
		c  += 1
		if c % 10000 == 0:
			nFile = "words" + str(i) + ".txt"
			wFile = open(nFile, "w+")
			i += 1
			files.append(nFile)
	return files
			



def attemptHack(usr, salt, files):
	s = open("progress.txt", "w+")
	for file in files:
		f = open(file, "r")
		l = f.readlines()
		for w in l:
			pwds = generateCombinations(w)
			for pwd in pwds:
				h = getHash(usr, pwd, salt)
				#if h == "d9015e035aaed42e3834c0d8ccb614d211a9aecc13440792c4d3d6256924f809": #TESTING
				if h == "1ca6004d870d5c9dcf2ffd231046a9015072a518c708040a02bf8b5b3a4e18b2":
					return pwd
			print("."),
		print(" ")
		s.write(file)
		print(file)

	return None

def main():
	'''
	TESTING
	usr = "swift"
	#pwd = "Adv!cE$"
	salt = "84829348943" 
	#x = getHash(usr, pwd, salt)
	#print(x)
	'''
	usr = "zifan"
	salt = "8934029034"
	filename = "words.txt"
	fileList = breakUP(filename)
	
	sol = attemptHack(usr, salt, fileList)
	if sol is None:
		print("__FAILURE__")
	else:
		print("SUCCESS : pwd = ", sol)
	

main()

