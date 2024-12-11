#!/bin/bash

test=1 #0
a=()
read -r line
IFS=' ' read -ra a <<< "$line"
echo "nums/ ${a[@]}";echo

if [[ $test == 1 ]]; then
    for n in "${a[@]}"; do
        echo "item/ $n"
    done
fi

trimleading0 () {

    local n="$1"
    n="${n#"${n%%[!0]*}"}"
    n="${n:-0}"
    echo "$n"
}

both_parts () {

    local a=("${@:1:$#-1}")
    local b="${@: -1}"

    #if [[ $test == 1 ]]; then
        echo "param/a - ${a[@]}"
        echo "param/b - $b"
    #fi
    declare -A Counter
    for key in "${a[@]}"; do
        Counter["$key"]=$(( ${Counter["$key"]:-0} + 1 ))
    done
    if [[ $test == 1 ]]; then
        for key in "${!Counter[@]}"; do
            echo "Counter/ $key: ${Counter[$key]}"
        done
    fi
    B=0

    while true; do
        if [[ $B == $b ]]; then
            break
        fi

        declare -A tmp
        for key in "${!Counter[@]}"; do
        #for n in "${a[@]}"; do
            val=${Counter[$key]}
            #if [[ $n == 0 ]]; then
            if [[ $key == 0 ]]; then
                tmp["1"]=$(( ${tmp["1"]:-0} + $val ))
                #A+=("1")
            #elif [[ $(( ${#n} % 2 )) == 0 ]]; then
            elif [[ $(( ${#key} % 2 )) == 0 ]]; then
                L=$(trimleading0 "${key:0:$(( ${#key} / 2 ))}")
                R=$(trimleading0 "${key:$(( ${#key} / 2 ))}")
                tmp["$L"]=$(( ${tmp["$L"]:-0} + $val ))
                tmp["$R"]=$(( ${tmp["$R"]:-0} + $val ))
                #N=${#n}
                #L=$(trimleading0 "${n:0:$(( ${#n} / 2 ))}")
                #R=$(trimleading0 "${n:$(( ${#n} / 2 ))}")
                #A+=("$L")
                #A+=("$R")
            else
                x2024=$(( $key * 2024 ))
                tmp["$x2024"]=$(( ${tmp["$x2024"]:-0} + $val ))
                #t=($(( $n * 2024 )))
                #t=${t#"${t%%[!0]*}"}
                #A+=("$t")
            fi
        done
        (( B++ ))
        # lets copy
        unset Counter
        for key in "${!tmp[@]}"; do
            Counter["$key"]="${tmp["$key"]}"
        done
        unset tmp
        if [[ $test == 1 ]]; then
            echo "count/ $B --- size/ ${#Counter[@]}"
        fi
    done
    echo "final/ ${#Counter[@]}"
    pbc=0
    ebc=0
    res=0
    for key in "${!Counter[@]}"; do
        pbc=$(printf "%s + %s\n" "$pbc" "${Counter["$key"]}" | bc)
        ebc=$( echo "$ebc + ${Counter["$key"]}" | bc )
        (( res+=Counter["$key"] ))
        ### diff/ ways to compute the same thing
    done
    echo "printf/bc $pbc"
    echo "echo/bc $ebc"
    echo "res/ $res"
}

#both_parts "${a[@]}" "25"
both_parts "${a[@]}" "75"


### deprecated

deprecated_p1 () {
    local a=("${@}")
    local b=0
    while true; do
        if [[ $b == 25 ]]; then
            break
        fi
        local A=()
        for n in "${a[@]}"; do
            if [[ $n == 0 ]]; then
                A+=("1")
            elif [[ $(( ${#n} % 2 )) == 0 ]]; then
                N=${#n}
                L=$(trimleading0 "${n:0:$(( ${#n} / 2 ))}")
                R=$(trimleading0 "${n:$(( ${#n} / 2 ))}")
                A+=("$L")
                A+=("$R")
            else
                t=($(( $n * 2024 )))
                t=${t#"${t%%[!0]*}"}
                A+=("$t")
            fi
        done
        (( b++ ))
        # copy a list
        unset a
        a=("${A[@]}")
        unset A
        echo "count/ $b --- size/ ${#a[@]}"
    done
    echo "final/ ${#a[@]}"
    #echo "${a[@]}"
}

# deprecated_p1 "${a[@]}"

