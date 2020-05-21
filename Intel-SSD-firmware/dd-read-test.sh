#!/bin/bash
for i in {1..5}
do
    dd if=/dev/zero of=tmp.txt bs=1G count=1
    rm tmp.txt
done
