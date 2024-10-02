def solve1(inputfile):
    with open(inputfile, "r") as f:
        data = f.read().split("\n\n")
    data = [d.replace("\n", "") for d in data]
    data = [[c for c in d] for d in data]
    data = [set(d) for d in data]
    return sum([len(d) for d in data])


def solve2(inputfile):
    with open(inputfile, "r") as f:
        data = f.read().split("\n\n")
    data = [d.strip().split("\n") for d in data]
    score = 0
    for group in data:
        ans = "".join(group)
        freq = [(c, ans.count(c)) for c in set([ch for ch in ans])]
        score += sum([1 if f[1] == len(group) else 0 for f in freq])
    return score


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
