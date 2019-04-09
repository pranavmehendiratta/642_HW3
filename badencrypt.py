# CS 642 University of Wisconsin
#
# WARNING:
# Do not use this encryption functionality, it has security vulnerabilities!
#
# Your job is to find and understand the problems
#
# usage: badencrypt.py keyfile
#

import sys
import os
import Crypto.Cipher.AES
import hashlib

print "########################################################"
print "######################Encrypt###########################"
print "########################################################"

f = open(sys.argv[1], 'r')
key = f.readline()
key = key[:32].decode("hex")
f.close()

message = \
"""AMOUNT: $  100.00
Originating Acct Holder: Swift
Orgininating Acct #82675-5823954

I authorized the above amount to be transferred to the account #78561-1848 
held by a UW-Student at the National Bank of the Cayman Islands.
"""

iv = os.urandom(16)
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC, IV=iv)
ciphertext = cipher.encrypt(message).encode("hex")
tag = hashlib.sha256(message).hexdigest()
# print iv.encode("hex")
# print ciphertext
# print tag


print message[:16]
print len(message)
print "iv -> " + str(iv) + ", len: " + str(len(str(iv)))
print "encoded iv -> " + iv.encode("hex") + ", len: " + str(len(str(iv.encode("hex"))))
print "ciphertext -> " + ciphertext + ", len: " + str(len(ciphertext))
print "tag -> " + tag

try:
    os.remove("orig_cipher")
except:
    print "No such file execption"
cf = open("orig_cipher", "w")
cf.write(iv.encode("hex") + ciphertext + tag)
