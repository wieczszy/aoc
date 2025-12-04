def solve1(inputfile):
    c = 0
    with open(inputfile) as f:
        for line in f.read().splitlines():
            sequence = ''
            bank = list(line)
            sequence += max(bank[:-1])
            n = bank.index(max(bank[:-1]))
            bank.pop(bank.index(max(bank[:-1])))
            sequence += max(bank[n:])
            c += int(sequence)
    return c


def solve2(inputfile):
    c = 0
    with open(inputfile) as f:
        for line in f.read().splitlines():
            sequence = ''
            bank = list(line)
            batteries_needed = 12
            bateries_left = len(bank)
            while bateries_left > batteries_needed + 1 and len(sequence) < 12:
                r = bateries_left - batteries_needed
                subset = bank[:r+1]
                m = max(subset)
                idx = subset.index(m)
                sequence += m
                bank = bank[idx+1:]
                batteries_needed -= 1
                bateries_left = len(bank)
            if len(sequence) < 12:
                sequence += ''.join(bank)
            c += int(sequence)
    return c


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
