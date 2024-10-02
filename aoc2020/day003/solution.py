def solve1(inputfile):
    with open(inputfile, "r") as f:
        data = f.read().split()
    data = [d * 1000 for d in data]
    c = 0
    y, x = 0, 0
    while y < len(data) - 1:
        y += 1
        x += 3
        if data[y][x] == "#":
            c += 1
    return c


def solve2(inputfile):
    with open(inputfile, "r") as f:
        data = f.read().split()
    data = [d * 1000 for d in data]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    r = 1
    for s in slopes:
        y, x = 0, 0
        c = 0
        while y < len(data) - 1:
            y += s[1]
            x += s[0]
            if data[y][x] == "#":
                c += 1
        r *= c
    return r


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
