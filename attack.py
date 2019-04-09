# CS 642 University of Wisconsin
#
# usage: attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys

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

# TODO: Print the new encrypted message
print ciphertext.encode("hex") + tag.encode("hex")
