#!bin/bash

patterns=()
lines=()
crossed=false

while read -r line;do
    if [[ -z "$line" ]];then
        crossed=true
    else
        if $crossed; then
            lines+=("$line")
        else
            IFS=', ' read -ra patterns <<< "$line"
        fi
    fi
done

: '
for pattern in "${patterns[@]}";do
    echo "$pattern"
done
'

declare -A dict
go () {
    local word=$1
    #echo word "$word" >&2
    if [[ -z $word ]];then
        echo 1
        return
    fi
    if [[ -n ${dict[$word]} ]];then
        echo ${dict[$word]}
        return
    fi
    local here=0
    for pattern in "${patterns[@]}";do
        #echo "$pattern" >&2
        if [[ $word == $pattern* ]];then # startswith
            temp=$(go "${word:${#pattern}}")
            (( here += temp ))
        fi
    done
    dict[$word]=$here
    echo $here
}

godp() {

    local word=$1
    local -n dp=$2
    dp[0]=1
    # idea/ sliding window & memo every substr
    for (( right = 1; right <= ${#word}; right++ )); do
        for pattern in "${patterns[@]}"; do 
            if [[ ${word:right - ${#pattern}:${#pattern}} == "$pattern" ]]; then
                (( dp[right] += dp[right - ${#pattern}] ))
            fi
        done
    done
    echo ${dp[${#word}]}
}

res=0
res2=0

for line in "${lines[@]}";do
    #echo "$line" >&2

    declare -a DP # name has to be different
    temp=$(godp "$line" DP)
    #temp=$(go "$line") # original py soln is slow

    if (( temp > 0 ));then
        (( res++ ))
    fi
    (( res2 += temp ))
done

echo "part 1: $res"
echo "part 2: $res2"

