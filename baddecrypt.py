# CS 642 University of Wisconsin
#
# WARNING:
# Do not use this encryption functionality, it has security vulnerabilities!
#
# Your job is to find and understand the problems
#
# usage: baddecrypt.py keyfile ciphertext
#

import sys
import Crypto.Cipher.AES
import hashlib

print "########################################################"
print "######################Decrypt###########################"
print "########################################################"

f = open( sys.argv[1], 'r' )
key = f.readline()
key = key[:32].decode("hex")
f.close()

# Grab ciphertext from first argument
ciphertextWithTag = (sys.argv[2]).decode("hex")

if len(ciphertextWithTag) < 16+16+32:
  print "Ciphertext is too short!"
  sys.exit(0)

####### Put this in attack.py ###########

origpt = \
"""AMOUNT: $  100.00
Originating Acct Holder: Swift
Orgininating Acct #82675-5823954

I authorized the above amount to be transferred to the account #78561-1848 
held by a UW-Student at the National Bank of the Cayman Islands.
"""

newpt = \
"""AMOUNT: $ 9999.00
Originating Acct Holder: Swift
Orgininating Acct #82675-5823954

I authorized the above amount to be transferred to the account #78561-1848 
held by a UW-Student at the National Bank of the Cayman Islands.
"""

origText = origpt[:16]
newText = newpt[:16]

print "origpt len: " + str(len(origpt))
print "newpt len: " + str(len(newpt))

print origText
print newText

origTextBytes = origText.encode("hex")
origIntText = int(origTextBytes, 16)

newTextBytes = newText.encode("hex")
newIntText = int(newTextBytes, 16)

print "origTextBytes: " + origTextBytes + ", origIntText: " + str(origIntText)
print "newTextBytes: " + newTextBytes + ", newIntText: " + str(newIntText)

origiv = ciphertextWithTag[:16]
origivBytes = origiv.encode("hex")
origivInt = int(origivBytes, 16)

print "origivBytes: " + origivBytes + ", origivInt: " + str(origivInt)

origCtInt = origIntText ^ origivInt
newivInt = origCtInt ^ newIntText

newivList = list(hex(newivInt))
newivBytes = ''.join(newivList[2:len(newivList) - 1])
newivText = newivBytes.decode("hex")

print "newivBytes -> " + newivBytes
print "newivText -> " + newivText

newTag = hashlib.sha256(newpt).digest() 
print "newTag len: " + str(len(newTag))
####### Put this in attack.py ##########

iv = ciphertextWithTag[:16]
iv = newivText

ciphertext = ciphertextWithTag[:len(ciphertextWithTag)-32]

tag = ciphertextWithTag[len(ciphertextWithTag)-32:]
tag = newTag

cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, IV=iv )
plaintext = cipher.decrypt( ciphertext[16:] )

#for i in range(len(newpt)):
#    print str(i) + ": " + plaintext[i] + ", " + newpt[i] 

if plaintext == newpt:
    print "same"
else:
    print "different"

#print "plaintext: " + plaintext
newT1 = hashlib.sha256(plaintext).hexdigest() 
#print "Orig: " + newpt
newT2 = hashlib.sha256(newpt).hexdigest() 
#
print "T1 : " + newT1
print "T2 : " + newT2

if newT1 == newT2:
    print "T1 and T2 are same"
else:
    print "T1 and T2 are different"

#
#print str(len(newpt))
#print str(len(plaintext))
#
print "1. " + tag.encode("hex")
print "2. " + hashlib.sha256(plaintext).hexdigest()
# Check the tag

if tag.encode("hex") != hashlib.sha256(plaintext).hexdigest():
   print "Invalid tag!"
else:
   print "Verified message:"
   print plaintext
