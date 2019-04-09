#!/bin/sh
python badencrypt.py testkeyfile
CT=`cat orig_cipher`
echo "$CT"
python attack.py $CT
MODCT=`cat mod_cipher`
python baddecrypt.py testkeyfile $CT
