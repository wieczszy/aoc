def solve1(inputfile):
    c = 0
    with open(inputfile) as f:
        R = f.read().split(',')
        for r in R:
            x = int(r.split('-')[0])
            y = int(r.split('-')[1])
            ids = [str(x) for x in list(range(x, y + 1))]
            for id in ids:
                if len(id) % 2 == 0:
                    n = len(id) // 2
                    b, e = id[:n], id[n:]
                    if b == e:
                        c += int(id)
    return c


def solve2(inputfile):
    c = 0
    with open(inputfile) as f:
        R = f.read().split(',')
        for r in R:
            x = int(r.split('-')[0])
            y = int(r.split('-')[1])
            ids = [str(x) for x in list(range(x, y + 1))]
            for id in ids:
                for i in range(2, len(id) + 1):
                    if len(id) % i == 0:
                        n = len(id) // i
                        y = [id[j:j+n] for j in range(0, len(id), n)]
                        if len(set(y)) == 1:
                            c += int(id)
                            break
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
