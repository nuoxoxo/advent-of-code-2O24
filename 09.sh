#!bin/bash

makeQ () {
    local line=$1
    local curr=0
    local res=()
    i=0
    while (( i < ${#line} )); do
        num=${line:$i:1}
        j=0
        if (( i % 2 == 0 )); then
            while (( j < num )); do
                res+=("$curr")
                (( j++ ))
            done
            (( curr++ ))
        else
            while (( j < num )); do
                res+=(".")
                (( j++ ))
            done
        fi
        (( i++ ))
    done
    echo "${res[@]}"
}

p2() {

    local Q=($(makeQ "$1"))
    echo "B/init ${Q[*]}" >&2 # init

    local N=${#Q[@]}
    echo "len/ $N" >&2

    local SPACE=()
    declare -A IDS
    local highest=-1

    local i=0
    while :; do
        if [[ ${Q[i]} == "." ]]; then
            local count=0
            local spaceleft=$i
            while (( i < N )) && [[ ${Q[i]} == "." ]]; do
                (( count++ ))
                (( i++ ))
            done
            if (( count != 0 )); then
                SPACE+=("$spaceleft,$count")
            fi
            if (( i >= N )); then
                break
            fi
        else
            local count=0
            local spaceleft=$i
            local curr=${Q[i]}
            while (( i < N )) && [[ ${Q[i]} == $curr ]]; do
                (( count++ ))
                (( i++ ))
            done
            if (( count != 0 )); then
                IDS[$curr]="$spaceleft,$count"
            fi
            highest=$curr  # Track the highest value
            if (( i >= N )); then
                break
            fi
        fi
    done

    # moving tiles
    while (( highest > -1 )); do
        IFS=',' read -r IDleft IDsize <<< "${IDS[$highest]}"
        for i in "${!SPACE[@]}"; do
            IFS=',' read -r spaceleft spacesize <<< "${SPACE[$i]}"
            if (( spaceleft > IDleft )); then
                break
            fi

            if (( IDsize == spacesize )); then
                IDS[$highest]="$spaceleft,$IDsize"
                SPACE[$i]="$(( spaceleft + IDsize )),0"
                break
            fi
            if (( IDsize < spacesize )); then
                IDS[$highest]="$spaceleft,$IDsize"
                SPACE[$i]="$(( spaceleft + IDsize )),$((spacesize - IDsize))"
                break
            fi
        done
        (( highest-- ))
    done

    local res=0
    for key in "${!IDS[@]}"; do
        IFS=',' read -r L N <<< "${IDS[$key]}"
        for (( i = L; i < L + N; i++ )); do
            (( res += i * key ))
        done
    done
    echo "$res"
}

p1() {

    local Q=($(makeQ "$1"))
    echo "A/init ${Q[*]}" >&2 # init

    i=0
    while (( i < ${#Q[@]} ));do
        if [[ ${Q[i]} == "." ]];then
            Q[i]=${Q[-1]}
            unset 'Q[-1]'
        else
            (( i++ ))
        fi
    done

    echo "A/last ${Q[*]}" >&2 # end state

    local res=0
    for idx in "${!Q[@]}"; do
        (( res += idx * Q[idx] ))
    done
    echo "$res"
}

read -r line

res1=$(p1 "$line")
echo "part 1:" $res1

res2=$(p2 "$line");echo

echo "part 1:" $res1 "shouldbe/ 1928 - 6258319840548"
echo "part 2:" $res2 "shouldbe/ 2858 - 6286182965311"
