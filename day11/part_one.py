def main():
    f11 = open("day11/input11.txt")
    input = f11.read().splitlines()
    instructions = {}
    for line in input:
        key, value = line.split(":", 1)
        instructions[key.strip()] = value.strip().split()

    start = "you"
    path = [start]
    stack = [(start, [start])]
    total = 0
    while stack:
        key, path = stack.pop()
        for forward in instructions[key]:
            if forward == "out":
                total += 1
                continue
            stack.append((forward, path + [forward]))
    return total

print(main())