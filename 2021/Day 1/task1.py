#!/usr/bin/env python3

inputs = []
counter = 0

with open('input.txt', 'r') as infile:
    for line in infile:
        inputs.append(int(line.strip()))
        
for i in range(len(inputs)):
    if i == 0:
        continue
    else:
        if inputs[i] > inputs[i - 1]:
            counter += 1

print (counter)