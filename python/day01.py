import utils

# star one
with utils.getInput(1) as f:
    # read file into list of integers
    max = 0
    curr = 0
    for line in f:
        # if line is empty, max = max of max and curr
        if not line.strip():
            max = max if max > curr else curr
            curr = 0
        else:
            curr += int(line)

print(max)

# star two
with utils.getInput(1) as f:
    curr = 0
    nums = []
    for line in f:
        # if line is empty, max = max of max and curr
        if not line.strip():
            nums.append(curr)
            curr = 0
        else:
            curr += int(line)

# sum of top three nums
print(sum(sorted(nums)[-3:]))