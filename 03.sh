#!bin/bash

r1=0
r2=0
ok=1
while read -r line; do
    matches=$(echo "$line" | grep -o 'mul([0-9]\+,[0-9]\+)' | sed 's/mul(//;s/)//')
    for m in $matches; do
        IFS=',' read -r L R <<< "$m"
        #echo "$m"
        r1=$(($L*$R+$r1))
    done
    ### egrep works well, grep works too
    matches=$(grep -oE  "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)" <<< $line)
    #matches=$(egrep -o "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)" <<< $line)
    for m in $matches; do
        if [[ $m == "do()" ]]; then
            ok=1
        elif [[ $m == "don't()" ]]; then
            ok=0
        elif [[ $ok == 1 ]]; then
            sub=$(sed 's/mul(//;s/)//' <<< $m) 
            IFS=',' read -r L R <<< "$sub"
            r2=$(($L*$R+$r2))
        fi
    done
done

echo "part 1: $r1"
echo "part 2: $r2"
