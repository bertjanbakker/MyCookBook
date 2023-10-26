#!/usr/bin/env sh

# sed equals and next command

echo "** option -n and command '=; n; p' **"
echo "** = print line number, pull in next line, print **"
cat input1.txt | sed -n '=; n; p'
