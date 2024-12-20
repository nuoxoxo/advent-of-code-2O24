#!/bin/bash

mapfile -t g
printf "%s \n" "${g[@]}"

INF=1000000
R=${#g[@]}
C=${#g[0]}
declare -A dp

for (( r = 0; r < R; r++ ));do
    for ((c=0;c < C; c++ ));do
        case "${g[r]:c:1}" in
            S) sr=$r; sc=$c ;;
            E) er=$r; ec=$c ;;
        esac
        dp["$r,$c"]=$INF
    done
done

echo "$sr,$sc - $er,$ec"
dp["$sr,$sc"]=0

Q=("$sr,$sc")
D=("-1,0" "1,0" "0,-1" "0,1")

while [[ ${#Q[@]} -gt 0 ]]; do
    IFS=',' read -r r c <<< "${Q[0]}"
    Q=("${Q[@]:1}")
    for d in "${D[@]}"; do
        IFS=',' read -r dr dc <<< "$d"
        rr=$((r + dr))
        cc=$((c + dc))
        if ((-1<rr && rr<R && -1<cc && cc<C)) \
            && [[ "${g[rr]:cc:1}" != "#" ]]; then
            if (( dp["$rr,$cc"] > dp["$r,$c"] + 1 )); then
                (( dp["$rr,$cc"] = dp["$r,$c"] + 1 ))
                Q+=("$rr,$cc")
            fi
        fi
    done
done

raw=${dp["$er,$ec"]}
echo "end/nocheat $raw"

abs() {
    (( $1 < 0 )) && echo $(( $1 * -1 )) || echo $1
}

p1=0
sec2=0
sec4=0
s12=0
for (( r = 0; r < R; r++ ));do
    for ((c=0;c < C; c++ ));do
        if [[ "${g[r]:c:1}" == "#" ]]; then
            continue
        fi
        bound=2
        for ((dr = -bound; dr < bound + 1; dr++)); do
            for ((dc=-bound; dc < bound+1; dc++)); do
                if (( $(abs $dr) + $(abs $dc) != bound )); then
                    continue
                fi
                rr=$((r + dr))
                cc=$((c + dc))
                if ((-1<rr && rr<R && -1<cc && cc<C)) \
                && [[ "${g[rr]:cc:1}" != "#" ]]; then
                    (( diff = dp["$rr,$cc"] - dp["$r,$c"] ))
                    if (( diff == 2 + bound )); then
                        (( sec2++ ))
                    elif (( diff == 4 + bound )); then
                        (( sec4++ ))
                    elif (( diff == 12 + bound )); then
                        (( s12++ ))
                    elif (( diff >= 100 + bound )); then
                        (( p1++ ))
                    fi
                fi
            done
        done
    done
done
echo "sec2/14 $sec2"
echo "sec4/14 $sec4"
echo "s12/3 $s12"
echo "p1/ $p1"

p2=0
sec50=0
sec72=0
F=("-1,1" "1,1" "1,-1" "-1,-1")
B=20
for (( r = 0; r < R; r++ ));do
    for ((c=0;c < C; c++ ));do
        if [[ "${g[r]:c:1}" == "#" ]]; then
            continue;
        fi
        for (( bound = 0; bound < B + 1; bound++ )); do
            for (( dr = 0; dr < bound + 1; dr ++ )); do
                dc=$(( bound - dr ))
                unset SEEN
                declare -A SEEN
                for f in "${F[@]}"; do
                    IFS=',' read -r factr factc <<< "$f"
                    rr=$((r + dr * factr))
                    cc=$((c + dc * factc))
                    if ((-1<rr && rr<R && -1<cc && cc<C)) \
                    && [[ "${g[rr]:cc:1}" != "#" ]] \
                    && [[ -z ${SEEN["$rr,$cc"]} ]]; then
                        SEEN["$rr,$cc"]=1
                        (( diff = dp["$rr,$cc"] - dp["$r,$c"] ))
                        if (( diff == 50 + bound )); then
                            (( sec50++ ))
                        elif (( diff == 72 + bound )); then
                            (( sec72++ ))
                        elif (( diff >= 100 + bound )); then
                            (( p2++ ))
                        fi
                    fi
                done
            done
        done
    done
    : '
    if (( sec50 > 0 || sec72 > 0 )); then
        echo "32/ $sec50 - 22/ $sec72 - $r,$c"
    fi
    '
done

echo "sec50/32 $sec50"
echo "sec72/22 $sec72"
echo "p2/ $p2"

