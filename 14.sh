#!bin/bash

lines=()
while read -r line; do
    lines+=("$line")
done


#R=7
#C=11
R=103
C=101
T=100 #5

# part 2

p2=-1

#: '
robs=()
for line in "${lines[@]}"; do
    read c r dc dr < <(echo "$line" | awk -F'[=, ]' '{print $2,$3,$5,$6}')
    robs+=("$r,$c,$dr,$dc")
done
#'

END=8000
w=0
x=0
y=0
z=0
it=1
maxline=0
for (( i = 0; i < END; i++ )); do
    if (( it % 1000 == 0 )); then
        echo "@ $it" >&2
    fi
    for (( j = 0; j < ${#robs[@]}; j++ )); do
        IFS=',' read -r r c dr dc <<< "${robs[j]}"
        (( r = (r + dr + R) % R ))
        (( c = (c + dc + C) % C ))
        robs[j]="$r,$c,$dr,$dc"
    done

    # inspect w/ maxline

    changed=0
    unset lens
    declare -A lens
    for (( j = 0; j < ${#robs[@]}; j++ )); do
        IFS=',' read -r r _ _ _ <<< "${robs[j]}"
        (( lens[$r]++ ))
    done
    for key in "${!lens[@]}"; do
        val="${lens[$key]}"
        if (( val > maxline )); then
            (( maxline = val ))
            (( changed = 1 ))
        fi
    done
    if (( changed == 1 )); then
        if (( it == 7858 )); then
            # print the sapin: grid
            G=()
            for (( r = 0; r < R; r++ )); do
                row=""
                for (( c = 0; c < C; c++ )); do
                    row+="."
                done
                G+=("$row")
            done
            # shape of sapin
            for rob in "${robs[@]}"; do
                IFS="," read -r r c _ _ <<< "$rob"
                G[r]="${G[r]:0:c}/"${G[r]:(( c + 1 ))}
            done
            # print a reduced section
            sr=$(( R / 7 * 3 ))
            er=$(( R / 5 * 4 ))
            sc=$(( C / 4 ))
            ec=$(( C / 4 * 3 ))
            for (( r = sr; r < er; r++ )); do
                echo "${G[r]:sc:ec-sc}"
            done
        fi
        (( p2 = it ))
        echo "----/ $it" # maxline-led change
    fi

    # inspect w/ counts inside each quadrant

    changed=0
    unset D
    declare -A D
    for rob in "${robs[@]}"; do
        IFS="," read -r r c _ _ <<< "$rob"
        (( D["$r,$c"]++ ))
    done

    unset count
    declare -A count
    for rc in "${!D[@]}"; do
        r=${rc%,*}
        c=${rc#*,}
        if (( r < R / 2 && c < C / 2 - 1 )); then
            (( count[0]++ ))
        fi
        if (( r < R / 2 && c > C / 2 - 1 )); then
            (( count[1]++ ))
        fi
        if (( r > R / 2 && c < C / 2 - 1 )); then
            (( count[2]++ ))
        fi
        if (( r > R / 2 && c > C / 2 - 1 )); then
            (( count[3]++ ))
        fi
    done
    if (( w < count[0] )); then
        (( w = count[0] ))
        changed=1
    fi
    if (( x < count[1] )); then
        (( x = count[1] ))
        changed=1
    fi
    if (( y < count[2] )); then
        (( y = count[2] ))
        changed=1
    fi
    if (( z < count[3] )); then
        (( z = count[3] ))
        changed=1
    fi
    if (( changed == 1 )); then
        if (( it == 7858 )); then
            # print the sapin: grid
            G=()
            for (( r = 0; r < R; r++ )); do
                row=""
                for (( c = 0; c < C; c++ )); do
                    row+="."
                done
                G+=("$row")
            done
            # shape of sapin
            for rob in "${robs[@]}"; do
                IFS="," read -r r c _ _ <<< "$rob"
                G[r]="${G[r]:0:c}/"${G[r]:(( c + 1 ))}
            done
            # print a reduced section
            sr=$(( R / 7 * 3 ))
            er=$(( R / 5 * 4 ))
            sc=$(( C / 4 ))
            ec=$(( C / 4 * 3 ))
            for (( r = sr; r < er; r++ )); do
                echo "${G[r]:sc:ec-sc}"
            done
        fi
        (( p2 = it ))
        echo "quad/ $it" # maxline-led change
    fi
    (( it++ ))
done

# part 1

unset D
declare -A D

unset count
declare -A count

for line in "${lines[@]}"; do

    read c r dc dr < <(echo "$line" | awk -F'[=, ]' '{print $2,$3,$5,$6}')
    for (( i = 0; i < T; i++ )); do
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

p1=1
for (( i = 0; i < 4 ; i++ )); do
    (( p1 *= count[$i] ))
done
echo "part 1: $p1"
echo "part 1: $p1"
