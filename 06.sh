#!/bin/bash

g=()
while IFS= read -r line; do
    g+=("$line")
done

#sr=-1
#sc=-1
R=${#g[@]}
C=${#g[0]}
for (( r = 0; r < R; r++ )); do
    #echo "${g[r]}"
    for (( c = 0; c < C; c++ )); do
        chr=${g[r]:c:1}
        #echo "char/ $chr"
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
SEEN["$sr,$sc"]=1 #"$sr,$sc" # exists/ if [[ -v SEEN["$nr,$nc"] ]]; then
r=$sr
c=$sc
i=0
while true; do
    dr=$(echo ${DIR[i]} | cut -d ',' -f1)
    dc=$(echo ${DIR[i]} | cut -d ',' -f2)
    #echo "dir/delta - $dr,$dc"
    ((rr = r + dr))
    ((cc = c + dc))
    #echo "dir/next - $rr,$cc"
    if ! (( -1 < rr && rr < R && -1 < cc && cc < C )); then
        echo "SEEN/ ${!SEEN[@]}"
        echo "p1/end ${#SEEN[@]}"
        break
    fi
    chr=${g[rr]:cc:1}
    if [[ $chr == "#" ]]; then
        ((i = (i + 1) % 4))
    else
        (( r = rr ))
        (( c = cc ))
        if [[ -n SEEN["$r,$c"] ]]; then
            SEEN["$r,$c"]=1 #"$r,$c"
        fi
        #echo "dir/curr - $r,$c"
        #echo "SEEN/ ${#SEEN[@]} - ${!SEEN[@]}"
        #echo "SEEN/ ${#SEEN[@]}"
    fi
    #echo "dir/curr - $r,$c"
done


