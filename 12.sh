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

declare -A SEEN

fencing() {

    local v=("$@") # takes in a vector of params
    res=1
    i=0
    while (( i < ${#v[@]} - 1 )); do
        if (( v[i] + 1 != v[i+1] ));then
            (( res++ ))
        fi
        (( i++ ))
    done
    echo "$res"
}

for ((r = 0; r < R; r++)); do
    for ((c = 0; c < C; c++)); do
    if [[ -z "${SEEN[$r,$c]}" ]]; then
        plant="${g[$r]:$c:1}"
        region=()
        Q=()
        Q+=("$r,$c")
        while [[ ${#Q[@]} -gt 0 ]]; do
            current="${Q[0]}"
            Q=("${Q[@]:1}")
            i=${current%,*}
            j=${current#*,}
            if [[ "${g[$i]:$j:1}" != "$plant" || -n "${SEEN[$i,$j]}" ]]; then
                continue
            fi
            SEEN["$i,$j"]=1
            region+=("$i,$j")
            for dir in "${DIR[@]}"; do
                dr=${dir%,*}
                dc=${dir#*,}
                rr=$((i + dr))
                cc=$((j + dc))
                if ((rr >= 0 && rr < R && cc >= 0 && cc < C)) \
                    && [[ -z "${SEEN[$rr,$cc]}" ]]; then
                    Q+=("$rr,$cc")
                fi
            done
        done

        # part 1
        pmt=0
        for item in "${region[@]}"; do
            i=${item%,*}
            j=${item#*,}
            for dir in "${DIR[@]}"; do
                dr=${dir%,*}
                dc=${dir#*,}
                rr=$(( i + dr ))
                cc=$(( j + dc ))
                if (( rr < 0 || rr >= R || cc < 0 || cc >= C )) \
                    || [[ "${g[$rr]:$cc:1}" != "$plant" ]]; then
                    (( pmt++ ))
                fi
            done
        done
        (( p1 += pmt * ${#region[@]} ))

        # part 2
        unset NU ND NL NR
        declare -A NU ND NL NR

        fence=0
        for ij in "${region[@]}"; do
            i=${ij%,*}
            j=${ij#*,}
            #echo "$item,$i,$j" >&2
            if (( i - 1 < 0 )) || [[ "${g[$((i-1))]:$j:1}" != "$plant" ]];then
                NU["$i"]+="$j "
            fi
            if (( i + 1 >= R )) || [[ "${g[$((i+1))]:$j:1}" != "$plant" ]];then
                ND["$i"]+="$j "
            fi
            if (( j - 1 < 0 )) || [[ "${g[$i]:$((j-1)):1}" != "$plant" ]];then
                NL["$j"]+="$i "
            fi
            if (( j + 1 >= C )) || [[ "${g[$i]:$((j+1)):1}" != "$plant" ]];then
                NR["$j"]+="$i "
            fi
        done

        : '
        for key in "${!NU[@]}"; do
            read -ra vals <<< "${NU[$key]}"
            sorted=($(echo "${vals[@]}" | tr ' ' '\n' | sort -n))
            fence=$((fence + $(fencing "${sorted[@]}")))
        done
        for key in "${!ND[@]}"; do
            read -ra vals <<< "${ND[$key]}"
            sorted=($(for n in "${vals[@]}"; do echo "$n"; done | sort -n))
            fence=$((fence + $(fencing "${sorted[@]}")))
        done
        for key in "${!NL[@]}"; do
            read -ra vals <<< "${NL[$key]}"
            sorted=($(for n in "${vals[@]}"; do echo "$n"; done | sort -n))
            fence=$((fence + $(fencing "${sorted[@]}")))
        done
        for key in "${!NR[@]}"; do
            read -ra vals <<< "${NR[$key]}"
            sorted=($(for n in "${vals[@]}"; do echo "$n"; done | sort -n))
            fence=$((fence + $(fencing "${sorted[@]}")))
        done
        '

        for a in "${NU[@]}" "${ND[@]}" "${NL[@]}" "${NR[@]}"; do
            for key in "${!a[@]}"; do
                read -ra vals <<< "${a[$key]}"
                sorted=($(echo "${vals[@]}" | tr ' ' '\n' | sort -n))
                fence=$((fence + $(fencing "${sorted[@]}")))
            done
        done

        ((p2 += fence * ${#region[@]}))

    fi
    done
done

echo "part 1: $p1 - expect/ 1456082 - 140 - 1930"
echo "part 2: $p2 - expect/ 872382 - 80 - 1206"

