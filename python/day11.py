from functools import reduce

monkey_rules = [
    (lambda x: x * 5, 11, 3, 4),
    (lambda x: x * x, 2, 6, 7),
    (lambda x: x * 7, 5, 1, 5),
    (lambda x: x + 1, 17, 2, 5),
    (lambda x: x + 3, 19, 2, 3),
    (lambda x: x + 5, 7, 1, 6),
    (lambda x: x + 8, 3, 0, 7),
    (lambda x: x + 2, 13, 4, 0)
]

monkeys = [
    [92, 73, 86, 83, 65, 51, 55, 93],
    [99, 67, 62, 61, 59, 98],
    [81, 89, 56, 61, 99],
    [97, 74, 68],
    [78, 73],
    [50],
    [95, 88, 53, 75],
    [50, 77, 98, 85, 94, 56, 89]
]

big_mod = 11 * 2 * 5 * 17 * 19 * 7 * 3 * 13

counts = [0] * 8

for _ in range(10000):
    for (i, mon) in enumerate(monkeys):
        rule = monkey_rules[i]
        for n in mon:
            n = rule[0](n) % big_mod
            
            if (n % rule[1] == 0):
                monkeys[rule[2]].append(n)
            else:
                monkeys[rule[3]].append(n)
            
            counts[i] += 1
        
        monkeys[i] = []

# print product of two highest counts
print(reduce(lambda x, y: x * y, sorted(counts, reverse=True)[:2]))