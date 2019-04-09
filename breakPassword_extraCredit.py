from hashlib import sha256
import sys

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
	l = list(set(l))
	l = [x[0] for x in l]
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
		x = 'swift,password,84829348943'
		for _ in range(0, 256):
			#x =  sha256(x.encode('utf-8')).hexdigest()
			x = sha256(x).digest()
			
		print(x)	 


def attemptHack(usr, salt):
	print("attemp hack")

def main():
	#makePwdList("words.txt")
	usr = "swift"
	pwd = "password"
	salt = "84829348943" 
	getHash(usr, pwd, salt)
	#print(sol)
	#print(sol == "67986ddf45bd064f4c2eb63258a5269838169da9a35ebb13692a2de22e6a4768")
	#attemptHack(usr, salt)

main()