#!/bin/bash

testing=0 #1
print_cramer_a_b=0 #1

declare -A infile
i=0
while read -r line; do
    if [[ -z "$line" ]];then
        ((i++))
    else
        infile["$i"]+="$line"$'\n'
    fi
done

Cramer () {
    local ax=("$1")
    local ay=("$2")
    local bx=("$3")
    local by=("$4")
    local px=("$5")
    local py=("$6")
    if [[ $bx == 0 ]]; then
        echo "0"
        return
    fi

    denom=$(( ax * by - ay * bx))
    if [[ $denom == 0 ]]; then
        echo "0"
        return
    fi

    a=$(( (px * by - py * bx) / denom ))
    b=$(( (px - ax * a) / bx ))
    if (( a < 0 || b < 0 )); then
        echo "0"
        return
    fi
    if (( (px * by - py * bx) % denom != 0 || (px - ax * a) % bx != 0 )); then
        echo "0"
        return
    fi
    if [[ 1 == "$print_cramer_a_b" ]]; then
        echo "res/ $(( 3*a + b )) - $a,$b" >&2
    fi
    echo "$(( 3 * a + b ))"
}

p1=0
p2=0
for i in "${!infile[@]}"; do
    
    if [[ 1 == "$testing" ]]; then
        echo "$i/ ${infile[$i]}"
    fi
    j=0
    while IFS= read -r line; do
        if [[ -z "$line" ]]; then
            break
        fi
        if [[ 1 == "$testing" ]]; then
            echo " getline/$j $line" >&2
        fi
        coor=($(grep -oE '[0-9]+' <<< "$line"))
        if [[ $j == 0 ]]; then
            ax=${coor[0]}
            ay=${coor[1]}
            A=${coor[@]}
        elif [[ $j == 1 ]];then
            bx=${coor[0]}
            by=${coor[1]}
            B=${coor[@]}
        else
            px=${coor[0]}
            #(( px = px + 10000000000000 ))
            py=${coor[1]}
            #(( py = py + 10000000000000 ))
            P=${coor[@]}
        fi
        (( j++ ))
    done < <(echo "${infile[$i]}");
    if [[ 1 == "$testing" ]]; then
        echo " parsing/A ${A[@]} - $ax,$ay" >&2
        echo " parsing/B ${B[@]} - $bx,$by" >&2
        echo " parsing/P ${P[@]} - $px,$py" >&2;echo
    fi
    # apply cramer's rule
    c1=$(Cramer "$ax" "$ay" "$bx" "$by" "$px" "$py")
    c2=$(Cramer "$ax" "$ay" "$bx" "$by" "$((px+10000000000000))" "$((py+10000000000000))")
    (( p1 = p1 + c1 ))
    (( p2 = p2 + c2 ))
done

echo "part 1: $p1"
echo "part 2: $p2"

