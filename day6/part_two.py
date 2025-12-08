def main():
    f6 = open("day6/input6.txt")
    matrix = [list(row) for row in f6.read().splitlines()]
    operator_indexes = [index for index, operator in enumerate(matrix[-1]) if operator != ' ']
    operators = [matrix[-1][index] for index in operator_indexes]
    inverted_matrix = list(zip(*matrix[:-1]))
    new_matrix = ["".join(t) for t in inverted_matrix]
    tuples = []
    group = []
    final = 0
    for item in new_matrix:
        if item != '    ':
            group.append(int(item))
        else:
            tuples.append(group)
            group = []
    tuples.append(group)
    final_list = list(zip(tuples, operators))
    for tup in final_list:
        operator = tup[1]
        if operator == "*":
            result = 1
        else:
            result = 0
        for item in tup[0]:
            if operator == "*":
                result *= item
            else:
                result += item
        final += result
    print(final)

if __name__ == "__main__":
    main()