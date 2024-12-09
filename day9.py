from itertools import chain

with open('./inputs/day9.txt', 'r') as file:
    input = file.read()
task1 = []
content = []
empty = []
task2 = {}

for i, v in enumerate(input):
    for k in range(int(v)):
        if i % 2 == 0:
            task1.append(i//2)
            content.append(i)
            task2[i] = int(v) * [i//2]
        else:
            task1.append(' ')
            empty.append(i)
            task2[i] = int(v)*[' ']


i = 0
j = len(task1)-1
while i < len(task1):
    while task1[j] == ' ':
        task1.pop(j)
        j -= 1
    while i < len(task1) and task1[i] != ' ':
        i += 1

    if i > j:
        break
    task1[i] = task1.pop(j)
    j -= 1

print(sum(i * v for i, v in enumerate(task1)))


for k in content[::-1]:
    size = len(task2[k])
    for i in empty[:]:
        if i > k:
            break
        space = task2[i].count(' ')
        if space == 0:
            empty.remove(i)
        if size <= space:
            filledBefore = task2[i][:task2[i].index(' ')]
            task2[i] = filledBefore + task2[k] + (space-size)*[' ']
            task2[k] = size*[' ']
            break

l = []
for i in task2:
    l += task2[i]

print(sum(i * v for i, v in enumerate(chain(*task2.values())) if v != ' '))
