#!/usr/bin/bash

# The input json file from CrUX
INP=$1
echo $INP

filebase="${INP##*/}"
EXT="${filebase##*.}"
FILE="${filebase%.*}"
OUTP=$FILE.txt

jq '.[].origin' $INP | tr -d '"' >& $OUTP
