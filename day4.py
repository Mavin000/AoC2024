file_path = './inputs/day4.txt'
grid = []
word = 'XMAS'
counter1 = 0
counter2 = 0

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

with open(file_path, 'r') as file:
    for line in file:
        grid.append(line.strip())


def isValid(x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


for x in range(len(grid)):
    for y in range(len(grid[0])):
        for dx, dy in dirs:
            for i in range(0, len(word)):
                if not isValid(x + i * dx, y + i * dy) or grid[x + i * dx][y + i * dy] != word[i]:
                    break
                if i == len(word) - 1:
                    counter1 += 1

print(counter1)


dirs2 = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 'A':
            if any(not isValid(x + dx, y + dy) for dx, dy in dirs2):
                continue
            if ((grid[x - 1][y - 1] == 'M' and grid[x + 1][y + 1] == 'S') or (grid[x - 1][y - 1] == 'S' and grid[x + 1][y + 1] == 'M')) and \
               ((grid[x - 1][y + 1] == 'M' and grid[x + 1][y - 1] == 'S') or (grid[x - 1][y + 1] == 'S' and grid[x + 1][y - 1] == 'M')):
                counter2 += 1


print(counter2)
