#!/bin/bash
r1=0
A=""
while read -r line; do
    xmas=$(echo "$line" | grep -o "XMAS" | wc -l)
    samx=$(echo "$line" | grep -o "SAMX" | wc -l)
    r1=$((xmas + samx + r1))
    A+="$line"$'\n' # $ makes a string literal
done
A="${A%$'\n'}" # % rm shortest match of a pattern
IFS=$'\n' read -r -d '' -a lines <<< "$A" 

R=${#lines[@]}
C=${#lines[0]}

r2=0
for ((r = 0; r < R - 2; r++)); do
    for ((c = 0; c < C - 2; c++)); do
        if [[ "${lines[r+1]:c+1:1}" != "A" ]]; then
            continue
        fi
        hi=${lines[r]:c:3}
        lo=${lines[r+2]:c:3}
        sub="${hi:0:1}${hi:2:1}${lo:2:1}${lo:0:1}"
        if [[ "$sub" =~ ^(SSMM|SMMS|MMSS|MSSM)$ ]]; then
            ((r2++))
        fi
    done
done
echo "part 2/try $r2"

#DONE
# get a transposed grid
# get all diagonal lines

#DONE (above)
# get all 3x3 grids ---> no need, we count it in place

# transpose
for (( c = 0; c < C; c++ )); do
    line=""
    for (( r = 0; r < R; r++ )); do
        line+="${lines[r]:c:1}"
    done
    xmas=$(echo "$line" | grep -o "XMAS" | wc -l)
    samx=$(echo "$line" | grep -o "SAMX" | wc -l)
    r1=$((xmas + samx + r1))
done

cur="XMAS"
rev="SAMX"

# dir: \
for (( r = 0; r < R - 3; r++ )); do
    for (( c = 0; c < C - 3; c++ )); do
        # XMAS
        ok=1
        for (( i = 0; i < 4; i++ )); do
            if [[ ${lines[r + i]:c + i:1} != ${cur:i:1} ]]; then
            #if [[ $lines[r + i][c + i] != $cur[i] ]]; then
                ok=0
                break
            fi
        done
        ((r1 += ok))
        # SAMX
        ok=1
        for (( i = 0; i < 4; i++ )); do
            if [[ ${lines[r + i]:c + i:1} != ${rev:i:1} ]]; then
                ok=0
                break
            fi
        done
        ((r1 += ok))
    done
done

# dir: /
for (( r = 0; r < R - 3; r++ )); do
    for (( c = 3; c < C; c++ )); do
        # XMAS
        ok=1
        for (( i = 0; i < 4; i++ )); do
            if [[ ${lines[r + i]:c - i:1} != ${cur:i:1} ]]; then
                ok=0
                break
            fi
        done
        ((r1 += ok))
        # SAMX
        ok=1
        for (( i = 0; i < 4; i++ )); do
            if [[ ${lines[r + i]:c - i:1} != ${rev:i:1} ]]; then
                ok=0
                break
            fi
        done
        ((r1 += ok))
    done
done

echo "part 1: $r1"

