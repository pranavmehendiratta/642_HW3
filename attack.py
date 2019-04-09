# CS 642 University of Wisconsin
#
# usage: attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys
import Crypto.Cipher.AES
import hashlib

# Grab ciphertext from first argument
ciphertextWithTag = (sys.argv[1]).decode("hex")

if len(ciphertextWithTag) < 16+16+32:
  print "Ciphertext is too short!"
  sys.exit(0)

iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[:len(ciphertextWithTag)-32]
tag = ciphertextWithTag[len(ciphertextWithTag)-32:]

# TODO: Modify the input so the transfer amount is more lucrative to
# the recipient
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

origTextBytes = origText.encode("hex")
origIntText = int(origTextBytes, 16)

newTextBytes = newText.encode("hex")
newIntText = int(newTextBytes, 16)

origiv = ciphertextWithTag[:16]
origivBytes = origiv.encode("hex")
origivInt = int(origivBytes, 16)

origCtInt = origIntText ^ origivInt
newivInt = origCtInt ^ newIntText

newivList = list(hex(newivInt))
newivBytes = ''.join(newivList[2:len(newivList) - 1])
newivText = newivBytes.decode("hex")

newTag = hashlib.sha256(newpt).digest()

# TODO: Print the new encrypted message
output = newivText.encode("hex") + ciphertext[16:].encode("hex") + newTag.encode("hex") 
#print output 

f = open("testkeyfile", 'r' )
key = f.readline()
key = key[:32].decode("hex")
f.close()

# Grab ciphertext from first argument
ciphertextWithTag = (output).decode("hex")

if len(ciphertextWithTag) < 16+16+32:
    print "Ciphertext is too short!"
    sys.exit(0)

iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[:len(ciphertextWithTag)-32]
tag = ciphertextWithTag[len(ciphertextWithTag)-32:]
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, IV=iv )
plaintext = cipher.decrypt( ciphertext[16:] )

# Check the tag
if tag.encode("hex") != hashlib.sha256(plaintext).hexdigest():
    print "Invalid tag!"
else:
    print "Verified message:"
    print plaintext
