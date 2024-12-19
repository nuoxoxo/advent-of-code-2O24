#!bin/bash

lines=()
while read -r line; do
    lines+=("$line")
done

declare -A D
declare -A count

#R=7
#C=11
R=103
C=101
T=100 #5

for line in "${lines[@]}"; do

    read c r dc dr < <(echo "$line" | awk -F'[=, ]' '{print $2,$3,$5,$6}')
    for (( i = 0; i < T; i++ )); do
        rr=$(($r+$dr))
        cc=$(($c+$dc))
        (( r = (r + dr + R) % R ))
        (( c = (c + dc + C) % C ))
        : '
        if (( rr < 0 )); then
            (( rr = R + rr ))
        elif (( rr >= R ));then
            (( rr = rr - R ))
        fi
        (( r = rr ))
        '
        : '
        #(( cc = c + dc ))
        if (( c < 0 )); then
            (( cc = C + cc ))
        elif (( cc >= C ));then
            (( cc = cc - C ))
        fi
        (( c = cc ))
        '
    done
    (( D["$r,$c"]++ ))
done

for rc in "${!D[@]}"; do
    r=${rc%,*}
    c=${rc#*,}
    val=${D["$rc"]}
    if (( r < R / 2 && c < C / 2 )); then
        (( count[0] += val ))
    fi
    if (( r < R / 2 && c > C / 2 )); then
        (( count[1] += val ))
    fi
    if (( r > R / 2 && c < C / 2 )); then
        (( count[2] += val ))
    fi
    if (( r > R / 2 && c > C / 2 )); then
        (( count[3] += val ))
    fi
done

res1=1
for (( i = 0; i < 4 ; i++ )); do
    (( res1 *= count[$i] ))
done
echo "part 1: $res1"
