#!/usr/bin/env sh

# sed Next and Print command

echo "** option -n and command 'N; P' **"
echo "** = append next line, print first line in pattern space **"
cat input1.txt | sed -n 'N; P'
