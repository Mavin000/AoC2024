with open('./inputs/day8.txt', 'r') as file:
    map = file.read().splitlines()


width = len(map[0])
height = len(map)
antennas = []
antinodes = set()
antinodes2 = set()
frequencies = {}

for y, line in enumerate(map):
    for x, char in enumerate(line):
        if char.isalnum():
            antennas.append((x, y, char))

for x, y, freq in antennas:
    if freq not in frequencies:
        frequencies[freq] = []
    frequencies[freq].append((x, y))


for freq, positions in frequencies.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            antinodes2.add((x1, y1))
            antinodes2.add((x2, y2))
            dx = x2 - x1
            dy = y2 - y1

            antinodeX = x2 + dx
            antinodeY = y2 + dy
            if 0 <= antinodeX < width and 0 <= antinodeY < height:
                antinodes.add((antinodeX, antinodeY))
            while 0 <= antinodeX < width and 0 <= antinodeY < height:
                antinodes2.add((antinodeX, antinodeY))
                antinodeX += dx
                antinodeY += dy

            antinodeX = x1 - dx
            antinodeY = y1 - dy
            if 0 <= antinodeX < width and 0 <= antinodeY < height:
                antinodes.add((antinodeX, antinodeY))
            while 0 <= antinodeX < width and 0 <= antinodeY < height:
                antinodes2.add((antinodeX, antinodeY))
                antinodeX -= dx
                antinodeY -= dy


print(len(antinodes))
print(len(antinodes2))
