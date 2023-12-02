#!/usr/bin/env python3

counter = 0
inputs = []
sums = []

with open('input.txt', 'r') as infile:
    for line in infile:
        inputs.append(int(line.strip()))
        
for i in range(len(inputs)):
    if i == 0:
        total = inputs[i] + inputs[i + 1] + inputs[i + 2]
        sums.append(total)
    elif i < len(inputs) - 1:
        total = inputs[i - 1] + inputs[i] + inputs[i + 1]
        sums.append(total)
    else:
        total = inputs[i - 2] + inputs[i - 1] + inputs[i]
        sums.append(total)

for i in range(len(sums)):
    if i == 0:
        continue
    else:
        if sums[i] > sums[i - 1]:
            counter += 1

print (counter)