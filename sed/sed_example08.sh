#!/usr/bin/env sh

# sed equals and Next command

echo "** option -n and command '=; N; p' **"
echo "** = print line number, append next line, print **"
cat input1.txt | sed -n '=; N; p'
