
def task_1():
    safe_count = 0
    with open("input.txt", "r") as file:
        data = file.read()
        for line in data.split("\n"):
            values = []
            if len(line) > 0:   
                for value in line.split(" "):
                    values.append(int(value))
                is_increasing = all(values[i] < values[i+1] for i in range(len(values) - 1))
                is_decreasing = all(values[i] > values[i+1] for i in range(len(values) - 1))
                valid_difference = all(1 <= abs(values[i] - values[i+1]) <= 3 for i in range(len(values) - 1))
                
                if (is_increasing or is_decreasing) and valid_difference:
                    safe_count += 1

    print(f"Task 1: {safe_count}")

def task_2():
    pass

if __name__ == "__main__":
    task_1()
    task_2()

