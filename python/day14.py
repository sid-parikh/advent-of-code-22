import utils

lines = utils.get_list(14)

map = [[0] * 2000 for _ in range(200)]

for line in lines:
    line = line.strip().split(' -> ')
        
    i = 0
    while (i + 1 < len(line)):
        
        x1 = int(line[i].split(',')[0])
        y1 = int(line[i].split(',')[1])
        x2 = int(line[i + 1].split(',')[0])
        y2 = int(line[i + 1].split(',')[1])
                
        if (x1 != x2):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                map[y1][x] = 1
        else:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                map[y][x1] = 1
        
        i += 1

# find highest y
for y in range(len(map) - 1, -1, -1):
    if (1 in map[y]):
        break
# fill row with 1s
map[y + 2] = [1] * len(map[y + 2])

def fill(x, y):
    # go down if possible, else down and left, else down and right
    
    if (map[y + 1][x] == 0):
        fill(x, y + 1)
    elif (x > 0 and map[y + 1][x - 1] == 0):
        fill(x - 1, y + 1)
    elif (x + 1 < len(map[y + 1]) and map[y + 1][x + 1] == 0):
        fill(x + 1, y + 1)
    else: 
        map[y][x] = 2
        return False

    return True

while(fill(500, 0)):
    pass

# for row in range(len(map)):
#     for col in range(len(map[row])):
#         print(".#o"[map[row][col]], end='')
#     print()

# print(map[y + 1])

# count sand (2s) in map
print(sum([sum([1 for x in row if x == 2]) for row in map]))