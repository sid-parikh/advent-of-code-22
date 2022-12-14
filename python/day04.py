# first attempt to do a day straight in python
import utils
import re
with utils.get_input(4) as f:
    starOne = 0
    starTwo = 0
    
    for line in f:
        a = re.split(",|-", line.strip())
        [minA, maxA, minB, maxB] = [int(b) for b in a]
        
        if (minA <= minB and maxA >= maxB):
            starOne += 1
        elif(minB <= minA and maxB >= maxA):
            starOne += 1
        
        if (minB >= minA and maxA >= minB):
            starTwo += 1
        elif (minA >= minB and maxB >= minA):
            starTwo += 1
        
    print(starOne)
    print(starTwo)