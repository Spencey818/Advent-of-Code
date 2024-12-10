import re

def task_1():
    with open("input.txt", "r") as file:
        data = file.read()
        regex = re.compile(r"mul\((\d+),(\d+)\)")
        matches = regex.findall(data)
        
        total = 0
        for match in matches:
            # Convert strings to integers and multiply
            result = int(match[0]) * int(match[1])
            total += result
        
        print(f"Total sum of multiplications: {total}")


def task_2():
    pass

if __name__ == "__main__":
    task_1()
    task_2()
