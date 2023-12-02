#!/usr/bin/env python3

instructions = {
    'commands' : [],
    'units': []
}

count = 0
distance = 0
aim = 0
depth = 0

with open('input.txt', 'r') as infile:
    for line in infile:
        line = line.split(' ')
        instructions['commands'].append(line[0].strip())
        instructions['units'].append(int(line[1].strip()))

for command in instructions['commands']:
    if command == 'forward':
        distance += instructions['units'][count]
        depth += (aim * instructions['units'][count])
    elif command == 'down':
        aim += instructions['units'][count]
    elif command == 'up':
        aim -= instructions['units'][count]
    count += 1


print(distance * depth)