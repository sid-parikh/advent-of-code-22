# first attempt to do a day straight in python
import utils
import re
with utils.getInput(4) as f:
    starOne = 0
    starTwo = 0
    
    for line in f:
        a = re.split(",|-", line.strip())
        a = [int(b) for b in a]
        
        if (a[0] <= a[2] and a[1] >= a[3]):
            starOne += 1
        elif(a[2] <= a[0] and a[3] >= a[1]):
            starOne += 1
        
        if (a[2] >= a[0] and a[1] >= a[2]):
            starTwo += 1
        elif (a[0] >= a[2] and a[3] >= a[0]):
            starTwo += 1
        
    print(starOne)
    print(starTwo)