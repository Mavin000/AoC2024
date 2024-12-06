with open('./inputs/day6.txt', 'r') as file:
    map = file.read()
grid = [list(line) for line in map.strip().split("\n")]
guardPos = None
direction = None
directions = ['^', '>', 'v', '<']
rows = len(grid)
cols = len(grid[0])
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell in "><v^":
            guardPos = (x, y)
            g2 = (x, y)
            direction = cell
            d2 = cell
            grid[y][x] = '.'
            break
    if guardPos:
        break


def simulate(grid, startPosition, startDirection):
    visited = set()
    x, y = startPosition
    dir = startDirection
    visited.add((x, y, direction))

    directions = ['^', '>', 'v', '<']

    while True:
        if dir == '^':
            nextStep = (x, y - 1)
        elif dir == '>':
            nextStep = (x + 1, y)
        elif dir == 'v':
            nextStep = (x, y + 1)
        elif dir == '<':
            nextStep = (x - 1, y)

        if not (0 <= nextStep[0] < cols and 0 <= nextStep[1] < rows):
            break

        if grid[nextStep[1]][nextStep[0]] == '#':
            dir = directions[(directions.index(dir) + 1) % 4]
        else:
            x, y = nextStep
            if (x, y, dir) in visited:
                return (visited, True)
            visited.add((x, y, dir))

    return (visited, False)


loops = set()

visitedTrueTimeline = simulate(grid, guardPos, direction)[0]

print(len(visitedTrueTimeline))

for x, y, _ in visitedTrueTimeline:
    if (x, y) != g2 and grid[y][x] == '.':
        grid[y][x] = '#'

        if simulate(grid, g2, d2)[1]:
            loops.add((x, y))

        grid[y][x] = '.'

print(len(loops))
