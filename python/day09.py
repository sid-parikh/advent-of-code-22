import utils
import collections

queue = collections.deque()
# convert 'U 9', e.g. to 'U','U','U','U','U','U','U','U','U'
with utils.get_input(9) as f:
    for line in f:
        move = line[0]
        amt = int(line.strip()[2:])
        for i in range(amt):
            queue.append(move)


def new_position(leader, follower):
    '''pure function to calculate new position of a follower, based on the leader's current position'''
    # if head is two above tail, move tail up one
    if leader[1] - follower[1] == 2 and leader[0] == follower[0]:
        follower = (follower[0], follower[1] + 1)
    elif leader[1] - follower[1] == -2 and leader[0] == follower[0]:
        follower = (follower[0], follower[1] - 1)
    elif leader[0] - follower[0] == 2 and leader[1] == follower[1]:
        follower = (follower[0] + 1, follower[1])
    elif leader[0] - follower[0] == -2 and leader[1] == follower[1]:
        follower = (follower[0] - 1, follower[1])

    # if they are not touching or diagonal, move tail towards head
    elif (leader[0] - follower[0] >= 2 or leader[0] - follower[0] <= -2 or leader[1] - follower[1] >= 2 or leader[1] -
          follower[1] <= -2):
        # in any other case, move tail diagonally towards head
        if leader[1] > follower[1] and leader[0] > follower[0]:
            follower = (follower[0] + 1, follower[1] + 1)
        elif leader[1] > follower[1] and leader[0] < follower[0]:
            follower = (follower[0] - 1, follower[1] + 1)
        elif leader[1] < follower[1] and leader[0] > follower[0]:
            follower = (follower[0] + 1, follower[1] - 1)
        elif leader[1] < follower[1] and leader[0] < follower[0]:
            follower = (follower[0] - 1, follower[1] - 1)

    return follower


# head
h = (0, 0)
# tails 1 through 9
tails = [(0, 0) for _ in range(9)]

# all the places tail one has visited
seenOne = set()
# all the places tail nine has visited
seenLast = set()

seenOne.add(tails[0])
seenLast.add(tails[8])

# simulate the path
while queue:

    # move head
    match queue.popleft():
        case 'U':
            h = (h[0], h[1] + 1)
        case 'D':
            h = (h[0], h[1] - 1)
        case 'L':
            h = (h[0] - 1, h[1])
        case 'R':
            h = (h[0] + 1, h[1])

    # recalculate tail positions
    tails[0] = new_position(h, tails[0])
    for i in range(1, 9):
        tails[i] = new_position(tails[i - 1], tails[i])

    # add tail positions to sets
    seenOne.add(tails[0])
    seenLast.add(tails[8])

print(len(seenOne))
print(len(seenLast))
