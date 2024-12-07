#!/bin/bash

FILE=1.0
L=()
R=()
while read -r l r; do
    L+=("$l")
    R+=("$r")
done < "$FILE"
L=($(printf "%s\n" "${L[@]}" | sort -n))
R=($(printf "%s\n" "${R[@]}" | sort -n))
N=${#L[@]}
p1=0
p2=0
for ((i = 0; i < N; i++)); do
    tmp=$((L[i] - R[i]))
    tmp=$((tmp < 0 ? -tmp : tmp))
    p1=$((p1 + tmp))
    occur=0
    for r in "${R[@]}"; do
        if [[ "${L[i]}" -eq "$r" ]]; then
            occur=$((occur+1))
        fi
    done
    p2=$((p2+occur*L[i]))
done
echo "part 1: $p1" 
echo "part 2: $p2" 

echo "------2nd way------"

p1=$(paste -d '-' \
    <(tr -s ' ' < "$FILE" | cut -d ' ' -f1 | sort -n) \
    <(tr -s ' ' < "$FILE" | cut -d ' ' -f2 | sort -n) \
    | { p1=0; while read -r l r; do
        diff=$((l - r))
        diff=$(echo "$diff" | tr -d '-')
        p1=$((p1 + diff))
    done; echo "$p1"; })
echo "part 1: $p1"
