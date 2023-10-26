#!/usr/bin/env sh

# sed ranges

echo "** command '/red/,/else/s/are/be/' **"
echo "** = substitute 'are' for 'be' from line with 'red' to line with 'else' **"
cat input1.txt | sed '/red/,/else/s/are/be/'
