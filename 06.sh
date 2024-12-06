#!/bin/bash

g=()
while IFS= read -r line; do
    g+=("$line")
done

R=${#g[@]}
C=${#g[0]}
for (( r = 0; r < R; r++ )); do
    #echo "${g[r]}"
    for (( c = 0; c < C; c++ )); do
        chr=${g[r]:c:1}
        if [[ $chr == "^" ]]; then
            sr=$r
            sc=$c
        fi
    done
done
echo "start/ $sr,$sc"

declare -a DIR
DIR[0]="-1,0"
DIR[1]="0,1"
DIR[2]="1,0"
DIR[3]="0,-1" # accessing/ dr=$(echo $dir | cut -d ',' -f1)

declare -A SEEN
SEEN["$sr,$sc"]=1 # exists/ if [[ -v SEEN["$nr,$nc"] ]]; then

r=$sr
c=$sc
i=0
while true; do
    dr=$(echo ${DIR[i]} | cut -d ',' -f1)
    dc=$(echo ${DIR[i]} | cut -d ',' -f2)
    ((rr = r + dr))
    ((cc = c + dc))
    if ! (( -1 < rr && rr < R && -1 < cc && cc < C )); then
        echo "part 1: ${#SEEN[@]}"
        break
    fi
    chr=${g[rr]:cc:1}
    if [[ $chr == "#" ]]; then ((i = (i + 1) % 4)) ;
    else
        (( r = rr ))
        (( c = cc ))
        if ! [[ -v SEEN["$r,$c"] ]]; then
            SEEN["$r,$c"]=1
        fi
    fi
done

#TODO
# modify one char at (r,c) then change it back
#   line="${g[r]}"
#   char="${g[r]:c:1}"
#   g[r]="${line:0:c}${REPL}${line:c+1}" # MOD
#   g[r]="${line:0:c}${char}${line:c+1}" # swap it back

r2=0
for coor in "${!SEEN[@]}"; do

    or=$(echo $coor | cut -d ',' -f1)
    oc=$(echo $coor | cut -d ',' -f2)
    line="${g[or]}"
    g[or]="${line:0:oc}#${line:oc+1}"

    r=$sr
    c=$sc
    i=0
    unset visited
    declare -A visited
    visited["$sr,$sc,$i"]=1
    while true; do
        dr=$(echo ${DIR[i]} | cut -d ',' -f1)
        dc=$(echo ${DIR[i]} | cut -d ',' -f2)
        ((rr = r + dr))
        ((cc = c + dc))
        if ! (( -1 < rr && rr < R && -1 < cc && cc < C )); then
            break
        fi
        chr=${g[rr]:cc:1}
        if [[ $chr == "#" ]]; then ((i = (i + 1) % 4)) ;
        else
            (( r = rr ))
            (( c = cc ))
        fi
        if ! [[ -v visited["$r,$c,$i"] ]]; then
            visited["$r,$c,$i"]=1
        else
            (( r2++ ))
            echo "obs/ $or,$oc,$r2" #,${!visited[@]}"
            #for (( r = 0; r < R; r++ ));do;echo"${g[r]}";done;echo
            break
        fi
    done
    g[or]="${line:0:oc}.${line:oc+1}"
done
echo "part 2: $r2"

