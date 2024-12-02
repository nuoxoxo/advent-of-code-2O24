#!/bin/bash

function OK {
    A=("$@")
    N=${#A[@]}
    S=($(printf "%s\n" "${A[@]}" | sort -u | wc -l | tr -d ' '))
    a=($(printf "%s\n" "${A[@]}" | sort -n))
    r=()
    for ((i = N - 1; i > -1; i--)); do r+=("${a[i]}"); done
    if [[ "${A[*]}" == "${a[*]}" || "${A[*]}" == "${r[*]}" ]] && [[ N -eq S ]]; then
        gap=0
        for ((i = 1; i < N; i++ )); do
            diff=$(( A[i] - A[i-1] ))
            diff=${diff#-} # rmv negative sign 
            gap=$((gap < diff ? diff : gap))
            if ((gap > 3)); then
                break
            fi
            done
        if ((0 < gap && gap < 4)); then
            echo 1
            return
        fi
    fi
    echo 0
}

r1=0
r2=0
while read -r line; do
    [[ -z $line ]] && echo "assert False"
    a=($line)
    if [[ $( OK "${a[@]}") -eq 1 ]]; then
        r1=$((r1 + 1))
        r2=$((r2 + 1))
        continue
    fi
    for (( i = 0; i < ${#a[@]}; i++ )); do
        tmp=("${a[@]:0:i}" "${a[@]:i+1}")
        if [[ $( OK "${tmp[@]}") -eq 1 ]]; then
            r2=$((r2 + 1))
            break
        fi
    done
done
echo "part 1: $r1"
echo "part 2: $r2"
