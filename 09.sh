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

p1() {

    Q=($(makeQ "$1"))
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
#res=$(makeQ "$line")
res=$(p1 "$line")
echo "part 1:" $res
