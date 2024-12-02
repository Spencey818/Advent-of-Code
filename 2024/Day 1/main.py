
def task_1():
    row1 = []
    row2 = []
    distances = []
    with open("input.txt", "r") as file:
        data = file.read()
        for line in data.split("\n"):
            if len(line) > 0:
                row1.append(int(line.split("   ")[0]))
                row2.append(int(line.split("   ")[1]))

    row1.sort()
    row2.sort()

    for i in range(len(row1)):
        distances.append(abs(row1[i] - row2[i]))

    print(f"Task 1: {sum(distances)}")


def task_2():
    row1 = []
    row2 = []
    simularity_dict = {
        'value': [],
        'simularity': []
    }
    with open("input.txt", "r") as file:
        data = file.read()
        for line in data.split("\n"):
            if len(line) > 0:
                row1.append(int(line.split("   ")[0]))
                row2.append(int(line.split("   ")[1]))

    for i in range(len(row1)):
        if row1[i] not in simularity_dict['value']:
            simularity_dict['value'].append(row1[i])
            simularity_dict['simularity'].append(row1[i] * row2.count(row1[i]))
        else:
            simularity_dict['simularity'][simularity_dict['value'].index(row1[i])] += row1[i] * row2.count(row1[i])

    print(f"Task 2: {sum(simularity_dict['simularity'])}")
    

if __name__ == "__main__":
    task_1()
    task_2()
