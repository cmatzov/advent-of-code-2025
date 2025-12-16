def convert_input():
    f10 = open("day10/input10.txt")
    machines = [machine for machine in f10.read().splitlines()]
    parsed_data = []

    for line in machines:
        parts = line.split()
        row = []
        for part in parts:
            if part.startswith('[') and part.endswith(']'):
                machine = "".join([char for char in part[1:-1]])
                row.append([machine])
            elif part.startswith('(') and part.endswith(')'):
                numbers = part[1:-1].split(',')
                row.append(tuple(int(num) for num in numbers))
            elif part.startswith('{') and part.endswith('}'):
                numbers = part[1:-1].split(',')
                row.append(list(int(num) for num in numbers))
        parsed_data.append(row)
    return parsed_data

def main():
    machines = convert_input()

    children = []
    for row in range(len(machines)):
        expected = [c for c in machines[row][0][0]]
        current = [char for char in ["." * len(expected)][0]]
        buttons = machines[row][1:-1]
        expected_joltage = machines[row][-1]
        joltage = [0 for _ in expected_joltage]

        stack = [(joltage, current, 0)]
        visited = set()
        min_presses = float('inf')

        while stack:
            curr_joltage, node, presses = stack.pop(0)
            node_tup = tuple(node)

            if node_tup in visited:
                continue
            visited.add(node_tup)

            if node == expected and curr_joltage == expected_joltage:
                min_presses = presses
                break

            for button in buttons:
                node_cp = node[:]

                for index in button:
                    if node_cp[index] == ".": 
                        node_cp[index] = "#" 
                        curr_joltage[index] += 1
                    else:
                        node_cp[index] = "."
                        curr_joltage[index] += 1
                    print(curr_joltage)
                if any(expected_joltage[i] > curr_joltage[i] for i in range(len(expected_joltage))):
                    continue
                stack.append((curr_joltage, node_cp, presses + 1))
        children.append(min_presses)
    return sum(children)

print(main())


# INCOMPLETE