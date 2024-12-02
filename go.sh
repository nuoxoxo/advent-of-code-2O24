#!/bin/bash

if [ $1 -gt 0 ] && [ $1 -lt 10 ]; then
    #FILENAME="0$1.0"
    FILENAME="$1.0"
elif [ $1 -ge 10 ] && [ $1 -lt 26 ]; then
    FILENAME="$1.0"
else
    echo "arg no good"
    return
fi

URL="https://adventofcode.com/2024/day/$1/input"

if [[ -z "$AOC_SESSION" ]]; then
    read -p "Enter aoc session: " TEMP
    echo "exporting: ${TEMP}"
    export "AOC_SESSION=${TEMP}"
else 
    echo "Session: $AOC_SESSION"
fi

# echo "${URL} \nSession:\n$AOC_SESSION"
curl -H "Cookie: session=$AOC_SESSION" -o ${FILENAME} ${URL}
# export "AOC_SESSION=$AOC_SESSION" # cant do cause we are in a subshell
