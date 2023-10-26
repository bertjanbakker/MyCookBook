#!/usr/bin/env sh

# sed Next and Delete command

echo "** command 'N; D' **"
echo "** = append next line, delete first line in pattern space **"
cat input1.txt | sed 'N; D'
