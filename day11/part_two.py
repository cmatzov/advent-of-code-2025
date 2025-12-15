_cache = {}

def main():
    global instructions
    f11 = open("day11/input11.txt")
    input = f11.read().splitlines()
    instructions = {}
    for line in input:
        node, children = line.split(":", 1)
        instructions[node] = children.split()


    def count(node, path, dac, fft):
        key = (node, dac, fft)
        if key in _cache:
            return _cache[(node, dac, fft)]
        if node in path:
            return False

        if node == "dac":
            dac = True
        elif node == "fft":
            fft = True
        elif node == "out":
            return dac and fft

        path.add(node)

        total = sum(count(child, path, dac, fft) for child in instructions[node])
        _cache[key] = total

        path.remove(node)
        return total

    return count("svr", dac=False, fft=False, path=set())

print(main())