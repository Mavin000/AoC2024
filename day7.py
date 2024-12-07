from itertools import product


def eval(values, operators):
    result = values[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += values[i + 1]
        elif op == '*':
            result *= values[i + 1]
        elif op == '||':
            result = int(str(result) + str(values[i + 1]))
    return result


def prod(left, numbers, operations):
    for ops in product(operations, repeat=len(numbers) - 1):
        if left == eval(numbers, ops):
            return True
    return False


with open('./inputs/day7.txt', 'r') as file:
    lines = file.read().splitlines()

result = 0
result2 = 0
operations = ['+', '*']
operations2 = ['+', '*', '||']

for line in lines:
    line = line.strip()
    parts = line.split(':')
    left = int(parts[0].strip())
    numbers = list(map(int, parts[1].strip().split()))
    if prod(left, numbers, operations):
        result += left
    if prod(left, numbers, operations2):
        result2 += left


print(result)
print(result2)
