import re


def solve1(inputfile):
    data = open(inputfile, "r").read().split("\n\n")
    data = [d.replace("\n", " ").split(" ") for d in data]
    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
    c = 0
    for passport in data:
        existing_fields = [field.split(":")[0] for field in passport]
        if set(required_fields).issubset(existing_fields):
            c += 1
    return c


def solve2(inputfile):
    data = open(inputfile, "r").read()[:-1].split("\n\n")
    data = [d.replace("\n", " ").split(" ") for d in data]
    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
    c = 0
    for passport in data:
        existing_fields = [field.split(":")[0] for field in passport]
        if set(required_fields).issubset(existing_fields):
            values = [field.split(":")[1] for field in passport]
            passport = dict(zip(existing_fields, values))
            if (
                (1920 <= int(passport["byr"]) <= 2002)
                and (2010 <= int(passport["iyr"]) <= 2020)
                and (2020 <= int(passport["eyr"]) <= 2030)
                and (
                    (
                        passport["hgt"].endswith("cm")
                        and 150 <= int(passport["hgt"][:-2]) <= 193
                    )
                    or (
                        passport["hgt"].endswith("in")
                        and 59 <= int(passport["hgt"][:-2]) <= 76
                    )
                )
                and (re.match(r"#[0-9a-f]{6}", passport["hcl"]))
                and (
                    passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                )
                and (re.match(r"^\d{9}$", passport["pid"]))
            ):
                c += 1
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
