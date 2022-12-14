import utils

lines = [[int(c) for c in line.strip()]
         for line in utils.get_input(8).readlines()]

visible = [[False for _ in line] for line in lines]

# set top and bottom rows to true
for i in range(len(lines[0])):
    visible[0][i] = True
    visible[-1][i] = True
# set left and right columns to true
for i in range(len(lines)):
    visible[i][0] = True
    visible[i][-1] = True

biggestLeft = [[0 for _ in line] for line in lines]
biggestRight = [[0 for _ in line] for line in lines]
biggestAbove = [[0 for _ in line] for line in lines]
biggestBelow = [[0 for _ in line] for line in lines]

# calculate the biggest value to the left of each pixel
for (i, line) in enumerate(lines):
    for j in range(1, len(line)):
        biggestLeft[i][j] = max(lines[i][j - 1], biggestLeft[i][j - 1])

# calculate the biggest value to the right of each pixel
for (i, line) in enumerate(lines):
    for j in range(len(line) - 2, -1, -1):
        biggestRight[i][j] = max(lines[i][j + 1], biggestRight[i][j + 1])
        
# calculate the biggest value above each pixel
for j in range(len(lines[0])):
    for i in range(1, len(lines)):
        biggestAbove[i][j] = max(lines[i - 1][j], biggestAbove[i - 1][j])
        
# calculate the biggest value below each pixel
for j in range(len(lines[0])):
    for i in range(len(lines) - 2, -1, -1):
        biggestBelow[i][j] = max(lines[i + 1][j], biggestBelow[i + 1][j])

# set pixels to visible if they are bigger any one of the biggest values
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] > biggestLeft[i][j]:
            visible[i][j] = True
        elif lines[i][j] > biggestRight[i][j]:
            visible[i][j] = True
        elif lines[i][j] > biggestAbove[i][j]:
            visible[i][j] = True
        elif lines[i][j] > biggestBelow[i][j]:
            visible[i][j] = True

    
        
        
# count visible
count = sum(line.count(True) for line in visible)
print(count)


# part two just brute force lol
# iterate entire grid
maxScore = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        # count how many trees are smaller in all diretions
        smallerLeft = 0
        k = j - 1
        while (k >= 0 and lines[i][k] < lines[i][j]):
            smallerLeft += 1
            k -= 1
        if (k >= 0):
            smallerLeft += 1
            
        smallerRight = 0
        k = j + 1
        while (k < len(lines[0]) and lines[i][k] < lines[i][j]):
            smallerRight += 1
            k += 1
        if (k < len(lines[0])):
            smallerRight += 1
    
        smallerAbove = 0
        k = i - 1
        while (k >= 0 and lines[k][j] < lines[i][j]):
            smallerAbove += 1
            k -= 1
        if (k >= 0):
            smallerAbove += 1
            
        smallerBelow = 0
        k = i + 1
        while (k < len(lines) and lines[k][j] < lines[i][j]):
            smallerBelow += 1
            k += 1
        if (k < len(lines)):
            smallerBelow += 1
        
        
        score = smallerLeft * smallerRight * smallerAbove * smallerBelow
        maxScore = max(maxScore, score)
print(maxScore)
        
