def solve1(inputfile):
    c = 0
    with open(inputfile) as f:
        x = f.read().split('\n\n')
        fresh = x[0].split('\n')
        fresh = [y.split('-') for y in fresh]
        fresh = [range(int(y[0]), int(y[1])+1) for y in fresh]
        available = x[1].split('\n')
        available = [int(x) for x in available]

    for item in available:
        for r in fresh:
            if item in r:
                c += 1
                break

    return c


def solve2(inputfile):
    with open(inputfile) as f:
        x = f.read().split('\n\n')
        fresh = x[0].split('\n')
        fresh = [y.split('-') for y in fresh]
        fresh = [range(int(y[0]), int(y[1])+1) for y in fresh]
        fresh = sorted(fresh, key=lambda r: r.start)
        
        merged = [fresh[0]]

        for r in fresh[1:]:
            if r.start <= merged[-1].stop:
                merged[-1] = range(merged[-1].start, max(merged[-1].stop, r.stop))
            else:
                merged.append(r)

    return sum([len(m) for m in merged])


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
