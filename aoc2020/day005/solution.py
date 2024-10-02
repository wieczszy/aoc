def traverse(L, d):
    if d == "F" or d == "L":
        return L[: len(L) // 2]
    else:
        return L[len(L) // 2 :]


def solve1(inputfile):
    with open(inputfile, "r") as f:
        data = [l.strip() for l in f.readlines()]

    ids = []

    for bpass in data:
        row, col = None, None

        rows = list(range(128))
        cols = list(range(8))

        for c in bpass[:7]:
            rows = traverse(rows, c)
            if len(rows) == 1:
                row = rows[0]

        for c in bpass[7:]:
            cols = traverse(cols, c)
            if len(cols) == 1:
                col = cols[0]

        ids.append(row * 8 + col)

    return max(ids)


def solve2(inputfile):
    with open(inputfile, "r") as f:
        data = [l.strip() for l in f.readlines()]

    ids = []

    for bpass in data:
        row, col = None, None

        rows = list(range(128))
        cols = list(range(8))

        for c in bpass[:7]:
            rows = traverse(rows, c)
            if len(rows) == 1:
                row = rows[0]

        for c in bpass[7:]:
            cols = traverse(cols, c)
            if len(cols) == 1:
                col = cols[0]

        ids.append(row * 8 + col)

    ids.sort()

    for i in range(len(ids) - 1):
        if ids[i + 1] - ids[i] > 1:
            return ids[i + 1] - 1


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
