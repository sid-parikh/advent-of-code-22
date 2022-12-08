import utils
import re
with utils.getInput(5) as f:
    count = 0
    stacksStarOne = [
        list("GFVHPS"),
        list("GJFBVDZM"),
        list("GMLJN"),
        list("NGZVDWP"),
        list("VRCB"),
        list("VRSMPWLZ"),
        list("THP"),
        list("QRSNCHZV"),
        list("FLGPVQJ")
    ]
    stacksStarTwo = [
        list("GFVHPS"),
        list("GJFBVDZM"),
        list("GMLJN"),
        list("NGZVDWP"),
        list("VRCB"),
        list("VRSMPWLZ"),
        list("THP"),
        list("QRSNCHZV"),
        list("FLGPVQJ")
    ]
    for line in f:
        if (count < 10):
            count += 1
            continue
        # okay now moves
        # split at spaces
        split = line.split(" ")
        # take second, fourth, and sixth elements in a tuple
        (amt, fro, to) = (int(split[1]), int(split[3]) - 1, int(split[5]) - 1)
        
        stacksStarOne[to].extend(stacksStarOne[fro][:-amt:-1])
        stacksStarTwo[to].extend(stacksStarTwo[fro][-amt:])
        del stacksStarTwo[fro][-amt:]
        del stacksStarOne[fro][-amt:]
        
    print(''.join(f'{s.pop()}' for s in stacksStarOne))  
    print(''.join(f'{s.pop()}' for s in stacksStarTwo))