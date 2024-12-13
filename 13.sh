#!/bin/bash

declare -A infile
i=0
while read -r line; do
    if [[ -z "$line" ]];then
        ((i++))
    else
        infile["$i"]+="$line"$'\n'
    fi
done

for i in "${!infile[@]}"; do
    echo "$i/" "${infile[$i]}"
done

