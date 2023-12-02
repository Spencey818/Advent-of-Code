#!/usr/bin/env python 3

def get_inputs():
    with open('input.txt', 'r') as inFile:
        inputs = inFile.readlines()
    return inputs
 

def challenge(inputs):
    nums = []
    for line in inputs:
        
        for letter in line:
            if letter.isdigit():
                num1 = str(letter)

        for letter in line[::-1]:
            if letter.isdigit():
                num2 = str(letter)

        nums.append(int(f'{num2}{num1}'))
    return sum(nums)

if __name__ == '__main__':
    inputs = get_inputs()
    answer = challenge(inputs)
    print(answer)
