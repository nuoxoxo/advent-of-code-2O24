#!bin/bash

g=()
G=() # for p2
moves=""
crossed=false

while read -r line;do
    if [[ -z "$line" ]];then
        crossed=true
    else
        if $crossed; then
            moves+="$line"
        else
            g+=("$line")
            G+=("$line")
        fi
    fi
done

R=${#g[@]}
C=${#g[0]}
M=${#moves}

for (( r = 0; r < R; r++ ));do
    for ((c=0;c < C; c++ ));do
        if [[ "${g[r]:c:1}" == '@' ]]; then
            sr=$r
            sc=$c
            break
        fi
    done
done

for gg in "${g[@]}";do echo "$gg /g"; done
echo "$moves /moves"
echo "$sr,$sc /sr,sc"
echo "g[$sr][$sc] = ${g[sr]:sc:1} /check"
echo "$M len/moves";echo

r=$sr
c=$sc

declare -A D
D["<"]="0 -1"
D[">"]="0 1"
D["^"]="-1 0"
D["v"]="1 0"

#: '
for (( i = 0; i < $M; i++ ));do
    ar=${moves:$i:1}
    IFS=' ' read -r dr dc <<< "${D["$ar"]}"
    #echo "$ar /ar - $dr,$dc /dr,dc"
    balls=()
    balls+=("$r,$c")
    rr=$r
    cc=$c
    stuck=false
    while true; do
        (( rr = rr + dr ))
        (( cc = cc + dc ))
        [[ $rr -lt 0 || $rr -ge $R || $cc -lt 0 || $cc -ge $C ]] && break
        thing=${g[rr]:cc:1}
        if [[ "$thing" == "." ]]; then
            break
        fi
        if [[ "$thing" == "O" ]]; then
            balls+=("$rr,$cc")
        fi
        if [[ "$thing" == "#" ]]; then
            stuck=true
            break
        fi
    done
    [[ "$stuck" == true ]] && continue
    for (( k = 0; k < ${#balls[@]} - 1; k++ )); do
        IFS=',' read -r br bc <<< "${balls[k+1]}"
        (( rr = br + dr ))
        (( cc = bc + dc ))
        g[rr]="${g[rr]:0:cc}O${g[rr]:cc+1}"
    done
    (( nr = r + dr ))
    (( nc = c + dc ))
    g[nr]="${g[nr]:0:nc}@${g[nr]:nc+1}"
    g[r]="${g[r]:0:c}.${g[r]:c+1}"
    r=$nr
    c=$nc
    for gg in "${g[@]}";do echo "$gg /g"; done; echo
done

p1=0
for (( r = 0; r < R; r++ ));do
    for ((c=0;c < C; c++ ));do
        if [[ "${g[r]:c:1}" == 'O' ]]; then
            (( p1 = p1 + 100 * r + c ))
        fi
    done
done
#'

# part 2

for ((i = 0; i < R; i++)); do
    row=""
    for ((j = 0; j < C; j++)); do
        c="${G[i]:j:1}"
        case "$c" in
            '@') row+="@." ;;
            'O') row+="[]" ;;
            '#') row+="##" ;;
            '.') row+=".." ;;
        esac
    done
    G[i]="$row"
    #G+=("$row")
    echo "$row /row"
done

for (( r = 0; r < R; r++ ));do
    for ((c=0;c < C; c++ ));do
        if [[ "${G[r]:c:1}" == '@' ]]; then
            sr=$r
            sc=$c
            break
        fi
    done
done

for gg in "${G[@]}";do echo "$gg G/init"; done
#echo "$moves /moves"
echo "$sr,$sc /sr,sc"
echo "G[$sr][$sc] = ${G[sr]:sc:1} /check"
echo "$M len/moves";echo

r=$sr
c=$sc

R=${#G[@]}
C=${#G[0]}

for (( i = 0; i < $M; i++ ));do

    ar=${moves:$i:1}
    IFS=' ' read -r dr dc <<< "${D["$ar"]}"
    #echo "$ar /ar - $dr,$dc /dr,dc"
    rr=$r
    cc=$c
    stuck=false
    dq=("$r,$c") # p2
    Q=("$r,$c")

    while [[ ${#dq[@]} -gt 0 ]]; do

        IFS=',' read -r rr cc <<< "${dq[0]}"
        #echo "$rr,$cc /rr,cc"
        dq=("${dq[@]:1}")
        (( rr += dr ))
        (( cc += dc ))
        for cell in "${Q[@]}"; do
            [[ "$cell" == "$rr,$cc" ]] && continue 2
        done

        thing=${G[rr]:cc:1}
        if [[ "$thing" == "[" || "$thing" == "]" ]]; then

            Q+=("$rr,$cc")
            dq+=("$rr,$cc")
            if [[ "$thing" == "[" ]]; then
                Q+=("$rr,$((cc + 1))")
                dq+=("$rr,$((cc + 1))")
            elif [[ "$thing" == "]" ]]; then
                Q+=("$rr,$((cc - 1))")
                dq+=("$rr,$((cc - 1))")
            fi
        elif [[ "$thing" == "#" ]]; then
            stuck=true
            break
        fi
    done

    [[ "$stuck" == true ]] && continue
    while [[ ${#Q[@]} -gt 0 ]]; do

        IFS=',' read -r br bc <<< "${Q[-1]}"
        Q=("${Q[@]:0:${#Q[@]}-1}")
        (( nr = br + dr ))
        (( nc = bc + dc ))
        G[nr]="${G[nr]:0:nc}${G[br]:bc:1}${G[nr]:nc+1}"
        G[br]="${G[br]:0:bc}.${G[br]:bc+1}"
    done

    (( nr = r + dr ))
    (( nc = c + dc ))
    G[nr]="${G[nr]:0:nc}@${G[nr]:nc+1}"
    G[r]="${G[r]:0:c}.${G[r]:c+1}"
    r=$nr
    c=$nc

    for gg in "${G[@]}";do echo "$gg /G"; done; echo

done

p2=0
for (( r = 0; r < R; r++ ));do
    for ((c=0;c < C; c++ ));do
        if [[ "${G[r]:c:1}" == '[' ]]; then
            (( p2 = p2 + 100 * r + c ))
        fi
    done
done

echo "part 1: $p1"
echo "part 2: $p2"
