#!/bin/bash

mapfile -t blocs < <(awk -v RS= '{gsub(/\n/, " "); print}')
L=()
K=()

for bl in "${blocs[@]}"; do
    IFS=' ' read -ra lines <<< "$bl"
    if [[ ${lines[0]} == "#####" ]]; then
        L+=("$bl")
    elif [[ ${lines[-1]} == "#####" ]]; then
        K+=("$bl")
    fi
done

getschema() {
    local block=("$@")
    local -a schema
    local res=()
    for line in "${block[@]}"; do
        for (( i = 0 ; i < 6 ; i++ )); do
            [[ ${line:i:1} == "#" ]] && ((schema[$i]++))
        done
    done
    for count in "${schema[@]}"; do
        res+=($(( count - 1 )))
    done
    echo "${res[*]}"
}

res=0
for k in "${K[@]}"; do

    IFS=' ' read -ra arrk <<< "$k"
    schemak=($(getschema "${arrk[@]}"))
    for l in "${L[@]}"; do

        IFS=' ' read -ra arrl <<< "$l"
        schemal=($(getschema "${arrl[@]}"))
        ok=1
        for (( i = 0 ; i < 5 ; i++ )); do
            if (( schemak[i] + schemal[i] > 5 )); then
                ok=0
                break
            fi
        done
        (( res += ok ))
    done
done

echo "res/ $res"
