from collections import defaultdict
file_path = './inputs/day5.txt'

rules = []
updates = []
valid = []
invalid = []
precedence = defaultdict(set)


def validation(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in position and y in position:
            if position[x] >= position[y]:
                return False

    return True


def sort_key(page, update):
    return sum(1 for p in precedence[page] if p in update)


with open(file_path, 'r') as file:
    data = file.read()

sections = data.strip().split("\n\n")
for rule in sections[0].splitlines():
    x, y = map(int, rule.split('|'))
    rules.append((x, y))
for update in sections[1].splitlines():
    updates.append(list(map(int, update.split(','))))

for update in updates:
    if validation(update, rules):
        valid.append(update)
    else:
        invalid.append(update)
result = sum([update[len(update) // 2] for update in valid])


for x, y in rules:
    precedence[y].add(x)

result2 = sum(
    sorted(update, key=lambda page: sort_key(page, update))[len(update) // 2] for update in invalid
)


print(result)
print(result2)
