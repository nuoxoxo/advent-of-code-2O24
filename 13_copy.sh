#!/bin/bash
testing=0 #1
declare -A infile
i=0
while read -r line; do
    if [[ -z "$line" ]];then
        ((i++))
    else
        infile["$i"]+="$line"$'\n'
    fi
done
res=0
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
            echo " getline/$j $line"
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
            (( px = px + 10000000000000 ))
            py=${coor[1]}
            (( py = py + 10000000000000 ))
            P=${coor[@]}
        fi
        (( j++ ))
    done < <(echo "${infile[$i]}");
    if [[ 1 == "$testing" ]]; then
        echo " parsing/A ${A[@]} - $ax,$ay"
        echo " parsing/B ${B[@]} - $bx,$by"
        echo " parsing/P ${P[@]} - $px,$py";echo
    fi
    # apply cramer's rule
    if [[ $bx == 0 ]]; then
        break
    fi
    denom=$(( ax * by - ay * bx))
    if [[ $denom == 0 ]]; then
        break
    fi
    a=$(( (px * by - py * bx) / denom ))
    b=$(( (px - ax * a) / bx ))
    if (( a < 0 || b < 0 )); then
        continue
    fi
    if (( (px * by - py * bx) % denom != 0 || (px - ax * a) % bx != 0 )); then
        continue
    fi
    tmp=$(( 3 * a + b ))
    (( res = res + tmp ))
    echo "res/ $tmp - $a,$b"
done

echo "part 1: $res"

