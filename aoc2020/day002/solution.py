def solve1(inputfile):
    data = open(inputfile, "r").read().splitlines()
    valid = 0
    for d in data:
        policy = d.split(":")[0].split(" ")
        password = d.split(":")[1].strip()
        min_rep = int(policy[0].split("-")[0])
        max_rep = int(policy[0].split("-")[1])
        req_letter = policy[1]
        c = password.count(req_letter)
        if min_rep <= c <= max_rep:
            valid += 1
    return valid


def solve2(inputfile):
    data = open(inputfile, "r").read().splitlines()
    valid = 0
    for d in data:
        policy = d.split(":")[0].split(" ")
        password = d.split(":")[1].strip()
        idx1 = int(policy[0].split("-")[0]) - 1
        idx2 = int(policy[0].split("-")[1]) - 1
        req_letter = policy[1]
        x1 = password[idx1] == req_letter
        x2 = password[idx2] == req_letter
        if x1 ^ x2:
            valid += 1
    return valid


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
