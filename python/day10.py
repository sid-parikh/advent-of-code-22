import utils
import collections

commands = []
with utils.get_input(10) as f:
    for line in f:
        commands.append(line.strip())
    
sum = 0
cycle = 1
x = 1


spriteL = 1
spriteR = 3

out = ""

for cmd in commands:
    if cmd[0] == 'a':
        num = int(cmd.strip().split(' ')[1])
        if cycle in (20, 60, 100, 140, 180, 220):
            sum += cycle * x
            print(cycle, x, sum)
        if (spriteL <= ((cycle - 1)% 40) <= spriteR):
            out += "#"
        else:
            out += "."
        cycle += 1
        if cycle in (20, 60, 100, 140, 180, 220):
            sum += cycle * x
            print(cycle, x, sum)
        if (spriteL <= ((cycle - 1)% 40) <= spriteR):
            out += "#"
        else:
            out += "."
        cycle += 1
        x += num
        spriteL = x - 1
        spriteR = x + 1
    else:
        if cycle in (20, 60, 100, 140, 180, 220):
            sum += cycle * x
            print(cycle, x, sum)
        if (spriteL <= ((cycle - 1)% 40) <= spriteR):
            out += "#"
        else:
            out += "."
        cycle += 1
    
print(sum)

for (i, n) in enumerate(out):
    if (i) % 40 == 0:
        print()
    print(n, end="")