from aoc_utils import load_input

f = list(map(int, load_input()))

# Found in part 1
target = 57195069
for i, n in enumerate(f):
    total = n
    numbers = [n]

    for m in f[i+1:]:
        if total > target:
            break
        if total == target and len(numbers) >= 2:
            print(min(numbers) + max(numbers))
            exit()

        total += m
        numbers.append(m)