def solve1(inputfile):
    with open(inputfile, "r") as f:
        data = f.read().splitlines()

    program = []

    for line in data:
        instruction = line.split(" ")[0]
        value = int(line.split(" ")[1])
        program.append((instruction, value))

    accumulator = 0
    i = 0
    i_run = []

    while True:
        if i in i_run:
            break
        elif program[i][0] == "acc":
            accumulator += program[i][1]
            i_run.append(i)
            i += 1
        elif program[i][0] == "jmp":
            i_run.append(i)
            i += program[i][1]
        else:
            i += 1

    return accumulator


def solve2(inputfile):
    with open(inputfile, "r") as f:
        data = f.read().splitlines()

    program = []

    for line in data:
        instruction = line.split(" ")[0]
        value = int(line.split(" ")[1])
        program.append((instruction, value))

    for i, line in enumerate(program):
        instruction = line[0]
        value = line[1]
        if instruction == "agg":
            continue
        if instruction == "jmp":
            program[i] = ("nop", value)
        if instruction == "nop":
            program[i] = ("jmp", value)

        accumulator = 0
        j = 0
        j_run = []

        while True:
            if j in j_run:
                program[i] = (instruction, value)
                break
            elif program[j][0] == "acc":
                accumulator += program[j][1]
                j_run.append(j)
                j += 1
            elif program[j][0] == "jmp":
                j_run.append(j)
                j += program[j][1]
            else:
                j += 1
            if j == len(program):
                return accumulator


if __name__ == "__main__":
    TEST = "test.txt"
    INPUT = "input.txt"

    print("-- TEST --")
    print(solve1(TEST))
    print(solve2(TEST))

    print("-- SOLUTION --")
    print(solve1(INPUT))
    print(solve2(INPUT))
