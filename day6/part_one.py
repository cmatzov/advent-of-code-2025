test_problem = [
        [ 123, 328,  51, 64 ],
        [ 45, 64,  387, 23 ], 
        [ 6, 98,  215, 314 ],
        [ "*", "+", "*", "+" ]  
]


def main():
    f6 = open("day6/input6.txt")
    problem = [list(row.split()) for row in f6.read().splitlines()]
    final = 0
    for i in range(len(problem[0])):
        numbers_to_calculate = [row[i] for row in problem[:-1]]
        symbol = problem[len(problem) - 1][i]
        if symbol == "*":
            result = 1
        else:
            result = 0
        for number in numbers_to_calculate:
            if symbol == "*":
                result *= int(number) 
            else:
                result += int(number)
        final += result
    print(final)

if __name__ == "__main__":
    main()