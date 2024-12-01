file_path = './inputs/day1.txt'
list1 = []
list2 = []
with open(file_path, 'r') as file:
    for line in file:
        n1, n2 = line.strip().split('   ')
        list1.append(n1)
        list2.append(n2)

list1.sort()
list2.sort()

diff = 0

for i, j in zip(list1, list2):
    diff += abs(int(i) - int(j))

print(diff)

score = 0
j = 0
for i in list1:
    while (int(list2[j]) < int(i)):
        j += 1
    while (int(i) == int(list2[j])):
        score += int(i)
        j += 1


print(score)
