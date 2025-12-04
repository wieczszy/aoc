def solve1(inputfile):
    M = 100
    idx = 50
    c = 0

    with open(inputfile) as f:
        for line in f.read().splitlines():
            x = int(line[1:])
            if line.startswith('R'):
                idx += x
                idx = idx % M
            else:
                idx -= x
                idx = idx % M
            c += (idx == 0)
    return c


def solve2(inputfile):
    M = 100
    idx = 50
    c = 0

    with open(inputfile) as f:
        for line in f.read().splitlines():
            x = int(line[1:])
            if line.startswith('R'):
                c += x // M
                idx += x % M 
                c += (idx >= M)
                idx -= M * (idx >= M)
            else:
                c += x // M - (idx == 0) 
                idx -= x % M 
                c += idx < 0
                idx += M * (idx < 0)
                c += (idx == 0)
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
