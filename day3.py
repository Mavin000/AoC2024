import re
file_path = './inputs/day3.txt'

with open(file_path, 'r') as file:
    instructions = re.findall(
        r"mul\(\d+,\d+\)|do\(\)|don't\(\)", file.read())


doMul = True
task1 = 0
task2 = 0
for match in instructions:
    if "mul(" in match:
        numbers = re.findall(r"(\d+)", match)
        task1 += int(numbers[0]) * int(numbers[1])
        if doMul:
            task2 += int(numbers[0]) * int(numbers[1])
    elif "do()" in match:
        doMul = True
    elif "don't()" in match:
        doMul = False


print(task1)
print(task2)
