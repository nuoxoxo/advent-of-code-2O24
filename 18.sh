#!/bin/bash

N=71
END=1023
DIR=("0,1" "1,0" "0,-1" "-1,0")
p1=0

# get all '#'
coors=()
while read -r coor; do
    coors+=("$coor")
done

# prepare grid
declare -A G
for (( r = 0; r < N; r++ )); do
    for (( c = 0; c < N; c++ )); do
        G["$r,$c"]='.'
    done
done

BFS() {
    local -n grid=$1
    local res=""

    unset deque
    Q=("0,0,0")

    unset SEEN
    declare -A SEEN

    while (( ${#Q[@]} > 0 )); do

        local node="${Q[0]}"
        #echo "node/ $node" >&2
        Q=("${Q[@]:1}")

        IFS=',' read -r r c cost <<< "$node"
        if (( r == N-1 && c == N-1 )); then
            res="$cost"
            break
        fi
        if [[ -n "${SEEN["$r,$c"]}" ]]; then
            continue
        fi
        SEEN["$r,$c"]=1

        for d in "${DIR[@]}"; do
            IFS=',' read -r dr dc <<< "$d"
            local rr=$(( r + dr ))
            local cc=$(( c + dc ))
            if (( -1<rr && rr<N && -1<cc && cc<N )) && \
                [[ "${grid["$rr,$cc"]}" != "#" ]]; then
                Q+=("$rr,$cc,$(( cost + 1 ))")
            fi
        done
    done
    echo "$res"
}

gcopy() {
    local -n src=$1 tar=$2
    for key in "${!src[@]}"; do
        tar["$key"]="${src["$key"]}"
    done
}

checker() {
    local -n n=$1 g=$2
    local res=""
    for (( i = 0; i < ${#coors[@]}; i++ )); do
        coor="${coors[i]}"
        IFS=',' read -r C R <<< "$coor"
        g["$R,$C"]="#"
        if (( i == n )); then
            res=$(BFS g)
            break
        fi
    done
    echo "$res"
}

declare -A gg
gcopy G gg
part1=$(checker END gg)
echo "part 1: $part1"

