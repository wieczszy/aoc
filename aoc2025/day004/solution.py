def solve1(inputfile):
    ans = 0
    M = []
    with open(inputfile) as f:
        for line in f.readlines():
            row = [0] + [1 if c == '@' else 0 for c in line] + [0]
            M.append(row)
    cols = len(M[0])
    M = [[0] * cols] + M + [[0] * cols]
    rows = len(M)
            
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if M[c][r]:
                s = sum([
                    M[c-1][r-1],
                    M[c-1][r],
                    M[c-1][r+1],
                    M[c][r-1],
                    M[c][r+1],
                    M[c+1][r-1],
                    M[c+1][r],
                    M[c+1][r+1]
                    ])
                if (s < 4):
                    ans += 1
    return ans


def solve2(inputfile):
    ans = 0
    M = []
    with open(inputfile) as f:
        for line in f.readlines():
            row = [0] + [1 if c == '@' else 0 for c in line] + [0]
            M.append(row)
    cols = len(M[0])
    M = [[0] * cols] + M + [[0] * cols]
    rows = len(M)

    while True:
        sans = ans
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if M[c][r]:
                    s = sum([
                        M[c-1][r-1],
                        M[c-1][r],
                        M[c-1][r+1],
                        M[c][r-1],
                        M[c][r+1],
                        M[c+1][r-1],
                        M[c+1][r],
                        M[c+1][r+1]
                        ])
                    if s < 4:
                        ans += 1
                        M[c][r] -= 1
        if sans == ans:
            break
    return ans


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"


    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))


    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
