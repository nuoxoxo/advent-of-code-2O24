#!/bin/bash
r1=0
while read -r line; do
    xmas=$(echo "$line" | grep -o "XMAS" | wc -l)
    samx=$(echo "$line" | grep -o "SAMX" | wc -l)
    r1=$((xmas + samx + r1))

#todo
# get all diagonal lines
# get all 3x3 grids

done
echo "$r1"
echo "$r2"
