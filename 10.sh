#!/bin/bash

g=()
while read -r line; do
    g+=("$line")
done

p1=0
p2=0
DIR=("-1,0" "0,1" "1,0" "0,-1")
R=${#g[@]}
C=${#g[0]}
for (( r = 0; r < R; r++ )); do
    #echo "$r - ${g[r]}"
    for (( c = 0; c < C; c++ ));do
        if [[ ${g[r]:c:1} != "0" ]];then
            continue
        fi
        #echo "$r,$c/ ${g[r]:c:1}" 

        unset SEEN
        unset D
        declare -A SEEN # set
        declare -A D # dict

        D["$r,$c"]=1
        SEEN["$r,$c"]=1

        count=0
        Q=("$r,$c") # deque

        while [[ ${#Q[@]} > 0 ]];do
            begin=${Q[0]}
            Q=("${Q[@]:1}") # popleft

            IFS=',' read -r sr sc <<< "$begin"
            prev=${g[sr]:sc:1}

            if [[ $prev == 9 ]]; then
                p2=$((p2 + D["$sr,$sc"]))
                count=$((count + 1))
            fi

            for dir in "${DIR[@]}";do
                IFS=',' read -r dr dc <<< "${dir}"
                rr=$((sr + dr))
                cc=$((sc + dc))

                if (( -1<rr && rr<R && -1<cc && cc<C )) &&\
                [[ ${g[rr]:cc:1} -eq $((prev + 1)) ]]; then
                    if [[ -z ${SEEN["$rr,$cc"]} ]]; then
                        SEEN["$rr,$cc"]=1
                        Q+=("$rr,$cc")
                    fi
                    D["$rr,$cc"]=$(( D["$rr,$cc"] + D["$sr,$sc"] ))
                fi
            done
        done
        p1=$((p1 + count))
    done
done

echo "part 1: $p1"
echo "part 2: $p2"
