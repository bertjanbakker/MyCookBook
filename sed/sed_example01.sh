#!/usr/bin/env sh

# sed ranges

echo "** option -n and command '1,3p' **"
echo "** = print the first three lines of the input **"
cat input1.txt | sed -n '1,3p'
