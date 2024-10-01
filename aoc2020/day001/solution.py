def solve1(inputfile):
    data = open(inputfile, "r").read().splitlines()
    data = [int(d) for d in data]
    for v1 in data:
        v2 = 2020 - v1
        if v2 in data:
            return v1 * v2


def solve2(inputfile):
    data = open(inputfile, "r").read().splitlines()
    data = [int(d) for d in data]
    for v1 in data:
        for v2 in data:
            if data.index(v1) == data.index(v2):
                pass
            v3 = 2020 - v1 - v2
            if v3 in data:
                return v1 * v2 * v3


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
