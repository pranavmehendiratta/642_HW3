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

# TODO: Print the new encrypted message

try:
    os.remove("mod_cipher")
except:
    print "No such file execption"
cf = open("mod_cipher", "w")
cf.write(ciphertextWithTag)

#print ciphertext.encode("hex") + tag.encode("hex")

