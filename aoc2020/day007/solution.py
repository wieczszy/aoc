def get_rules(inputfile):
    with open(inputfile, "r") as f:
        data = f.read().splitlines()
    data = [d.replace("bags", "bag").replace("bag", "") for d in data]
    data = [d.replace(".", "").split("contain") for d in data]
    data = [[d[0].strip(), d[1].split(",")] for d in data]

    rules = {}

    for line in data:
        bag = line[0]
        rules[bag] = {}
        for element in line[1]:
            e = element.strip()
            if e == "no other":
                rules[bag] = 0
            else:
                quantity = int(e.split(" ")[0])
                color = " ".join(e.split(" ")[1:])
                rules[bag][color] = quantity

    return rules


def search(rules, bag, search_value):
    if rules[bag] == 0:
        return 0
    if search_value in rules[bag].keys():
        return 1
    else:
        r = 0
        for k in rules[bag].keys():
            r += search(rules, k, search_value)
        if r > 0:
            return 1
        else:
            return 0


def count(rules, bag):
    if rules[bag] == 0:
        return 0
    else:
        c = 0
        for k in rules[bag].keys():
            c1 = count(rules, k) * rules[bag][k]
            c += rules[bag][k] + c1
        return c


def solve1(inputfile):
    rules = get_rules(inputfile)
    c = 0
    for bag in rules.keys():
        c += search(rules, bag, "shiny gold")
    return c


def solve2(inputfile):
    rules = get_rules(inputfile)
    return count(rules, "shiny gold")


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
