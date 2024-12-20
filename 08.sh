#!/bin/bash

g=()
mapfile -t g
printf "%s\n" "${g[@]}"

declare -A A  
R=${#g[@]}
C=${#g[0]}

for (( r = 0; r < R; r++ )); do
    for (( c = 0; c < C; c++ )); do
        char=${g[r]:c:1}
        if [[ "$char" != "." ]]; then
            A["$char"]+="($r,$c) "
        fi
    done
done
#for k in "${!A[@]}"; do echo "dbg/ key $k, set: ${A[$k]}";done

declare -A btw
declare -A ALL
for atn in "${!A[@]}"; do
    coor="${A["$atn"]}"
    #echo; echo "$atn - $coor" # ok/

    for tup in $coor; do
        tup=${tup//[()]/}
        sr=${tup%,*}
        sc=${tup#*,}
        #echo; echo "sr,sc/ $sr, $sc" # ok/
        for cmp in $coor; do
            cmp=${cmp//[()]/}
            er=${cmp%,*}
            ec=${cmp#*,}
            if [[ "$sr" == "$er" && "$sc" == "$ec" ]]; then
                continue
            fi
            #echo "er,ec/ $er, $ec" # ok/
            dr=$(( er - sr ))
            dc=$(( ec - sc ))
            # PART 1
            rr=$(( sr - dr ))
            cc=$(( sc - dc ))
            if (( -1 < rr && rr < R && -1 < cc && cc < C )); then
                btw["($rr,$cc)"]=1
            fi
            rr=$(( er + dr ))
            cc=$(( ec + dc ))
            if (( -1 < rr && rr < R && -1 < cc && cc < C )); then
                btw["($rr,$cc)"]=1
            fi
            # PART 2
            t=0
            while true; do
                changed=false
                rr=$(( er + dr * t ))
                cc=$(( ec + dc * t ))
                if (( -1 < rr && rr < R && -1 < cc && cc < C )); then
                    ALL["($rr,$cc)"]=1
                    changed=true
                fi
                rr=$(( sr - dr * t ))
                cc=$(( sc - dc * t ))
                if (( -1 < rr && rr < R && -1 < cc && cc < C )); then
                    ALL["($rr,$cc)"]=1
                    changed=true
                fi
                if [[ "$changed" == false ]]; then
                    break
                fi
                (( t++ ))
            done
        done
    done
done
#for k in "${!btw[@]}";do echo"dbg/ key $k, set: ${btw[$k]}";done

echo "part 1/ ${#btw[@]}"
echo "part 2/ ${#ALL[@]}"

