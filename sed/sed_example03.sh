#!/usr/bin/env sh

# sed ranges

echo "** command 'p; d' **"
echo "** = print and delete **"
cat input1.txt | sed -n 'p; d'
