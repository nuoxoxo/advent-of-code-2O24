#!bin/bash
bloc1=""
bloc2=""
crossed=false
while read -r line; do
    if [[ -z "$line" ]]; then
         crossed=true
    else
        if $crossed; then
            bloc2+="$line"$'\n'
        else
            bloc1+="$line"$'\n'
        fi
    fi
done
bloc1="${bloc1%$'\n'}"
bloc2="${bloc2%$'\n'}"
#echo "$bloc1 /---dbg---/ $bloc2"

#DONE
# check if val in set[key]
# sort w/ a set of rules

# STEP/ mimic `defaultdict(set)`, parse the rules

declare -a isafter

insert() {
    local a=$1
    local b=$2
    if [[ ! " ${isafter[$a]} " =~ " $b " ]]; then
        isafter["$a"]+="$b "
    fi
}

while IFS='|' read -r a sorted; do
    insert "$a" "$sorted" 
done <<< "$bloc1"
#for key in "${!isafter[@]}"; do echo "k: $key, set: ${isafter[$key]}";done


# STEP/ sorting
#   bubble sort using isbefore|isafter set from bloc1
r1=0
r2=0
while read -r line; do

    IFS=',' read -ra original <<< "$line"
    N=${#original[@]}
    sorted=("${original[@]}")

    for (( i = 0; i < N; i++ )); do
        for (( j = 0; j < N - i - 1; j++ )); do
            if [[ " ${isafter[${sorted[j + 1]}]} " =~ " ${sorted[j]} " ]]; then
                #echo "swap/"
                n="${sorted[j]}"
                sorted[j]="${sorted[j + 1]}"
                sorted[j + 1]="$n"
            fi
        done
    done

    ok=true
    for (( i = 0; i < N; i++ )); do
        if [[ "${original[$i]}" != "${sorted[$i]}" ]]; then
            ok=false
            break
        fi
    done
    if [[ $ok == true ]]; then
        ((r1 += ${original[N / 2]}))
    else
        ((r2 += ${sorted[N / 2]}))
    fi
done <<< "$bloc2"

echo "part 1: $r1"
echo "part 2: $r2"
