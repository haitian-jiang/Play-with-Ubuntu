#!/bin/bash
while true
do
    echo "CPU: " > .powertmp
    s-tui -t | grep -o  "package-0: [0-9]*\.[0-9]\b" | grep -o --color=never "[0-9]*\.[0-9]\b" >> .powertmp
    echo -e "W  \tGPU: " >> .powertmp
    nvidia-smi | grep -o "[0-9]*W / 250W" | grep -o --color=never "^[0-9]*W" >> .powertmp
    echo "  " >> .powertmp
    awk BEGIN{RS=EOF}'{gsub(/\n/,"");print}' .powertmp > .power
    printf "\r$(cat .power)"
    rm .power; rm .powertmp
    sleep 0.5
done
https://blog.csdn.net/hjxhjh/article/details/17264739
