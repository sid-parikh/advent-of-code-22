import utils
import heapq

data = utils.get_list(12)
data = [list(line.strip()) for line in data]

target = 0
start = 0

for (i, line) in enumerate(data):
    for (j, c) in enumerate(line):
        if (c == 'S'):
            data[i][j] = 'a'
            start = (j, i)
        if (c == 'E'):
            data[i][j] = 'z'
            target = (j, i)

# Dijkstra's
visited = set()
queue = []
ans = float('inf')
size = len(data) * len(data[0])

distances = [[float('inf')] * len(data[0]) for _ in range(len(data))]

heapq.heappush(queue, (0, target[0], target[1]))
while (queue):
    (dist, x, y) = heapq.heappop(queue)
    if ((x, y) in visited):
        continue
    visited.add((x, y))
    distances[y][x] = dist
    
    if x > 0 and ord(data[y][x - 1]) >= ord(data[y][x]) - 1:
        heapq.heappush(queue, (dist + 1, x - 1, y))
    if (x < len(data[0]) - 1 and ord(data[y][x+1]) >= ord(data[y][x]) - 1):
        heapq.heappush(queue, (dist + 1, x + 1, y))
    if (y > 0 and ord(data[y-1][x]) >= ord(data[y][x]) - 1):
        heapq.heappush(queue, (dist + 1, x, y - 1))
    if (y < len(data) - 1 and ord(data[y+1][x]) >= ord(data[y][x]) - 1):
        heapq.heappush(queue, (dist + 1, x, y + 1))

# print shortest distance to any 'a'
dist = float('inf')
for (i, line) in enumerate(distances):
    for (j, d) in enumerate(line):
        if (data[i][j] == 'a'):
            dist = min(dist, d)
print(dist)




    