#!/usr/bin/env sh

# sed ranges

echo "** command '2,3s/are/be/' **"
echo "** = substitute 'are' for 'be' on lines 2 and 3 **"
cat input1.txt | sed '2,3s/are/be/'
