#!/bin/bash
L=()
R=()
while read -r l r; do
    L+=("$l")
    R+=("$r")
done

# use printf to print them all out, piping into sort -n
L=($(printf "%s\n" "${L[@]}" | sort -n))
R=($(printf "%s\n" "${R[@]}" | sort -n))

# get the len assuming both lists have the same length
N=${#L[@]}

# DBG
#echo "L: ${L[@]}"
#echo "R: ${R[@]}"

# part 1
A=0
for ((i = 0; i < N; i++)); do
    tmp=$((L[i] - R[i]))
    tmp=$((tmp < 0 ? -tmp : tmp))
    A=$((A + tmp))
done

echo "part 1: $A" 

