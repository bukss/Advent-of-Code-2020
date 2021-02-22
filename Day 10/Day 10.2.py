from aoc_utils import load_input

adapters = [0] + list(map(int, load_input()))
adapters += [max(adapters) + 3]
adapters = sorted(adapters)
cont_configurable_adapters = "".join(list(map(str, [adapters[j+1] - n for j, n in enumerate(adapters[:-1])]))).split("3")
cont_configurable_adapters = list(map(list, filter(bool, cont_configurable_adapters)))

# v is the # of unique partitions of a set of k size in which all subsets have length <= 3  
MAGIC_NUMBERS = {
    1: 1,
    2: 2,
    3: 4,
    4: 7
}

p = 1
for subset in cont_configurable_adapters:
    p *= MAGIC_NUMBERS[len(subset)]

print(p)
