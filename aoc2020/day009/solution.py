def solve1(inputfile, offset):
    with open(inputfile, "r") as f:
        data = f.read().splitlines()

    data = [int(d) for d in data]

    for i, value in enumerate(data):
        if i < offset:
            continue
        else:
            subset = data[i - offset : i]
            solutions = 0
            for j in range(len(subset)):
                for k in range(len(subset)):
                    if j == k:
                        continue
                    else:
                        if subset[j] + subset[k] == value:
                            solutions += 1
            if solutions == 0:
                return value


def solve2(inputfile, offset):
    with open(inputfile, "r") as f:
        data = f.read().splitlines()

    data = [int(d) for d in data]
    search = solve1(inputfile, offset)

    for i, value in enumerate(data):
        v = [value]
        for j in range(i + 1, len(data)):
            v.append(data[j])
            if sum(v) == search:
                return min(v) + max(v)
            elif sum(v) > search:
                break
            else:
                continue


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST, 5))
    print(solve2(TEST, 5))

    print("-- SOLUTION --")
    print(solve1(INPUT, 25))
    print(solve2(INPUT, 25))
