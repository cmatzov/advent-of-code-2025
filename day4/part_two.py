test_case = [                                           # y
    ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'], # 0
    ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'], # 1
    ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'], # 2
    ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'],
    ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'],
    ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'],
    ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'],
    ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
    ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'],
    ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.'],
# x # 0  # 1  # 2 
]

def main():
    f4 = open("day4/input4.txt")
    rows = f4.read().splitlines()

    matrix = [list(row) for row in rows]

    count = 0
    prev_count = -1
    while True:
        prev_count = count
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix)):
                if matrix[row][col] != "@":
                    continue
                neighbours = 0
                for r, c  in [
                    [row - 1, col - 1],
                    [row - 1, col], 
                    [row - 1, col + 1], 
                    [row, col -1], 
                    [row, col + 1], 
                    [row + 1, col - 1], 
                    [row + 1, col], 
                    [row + 1, col + 1]
                ]:
                    if r >= 0 and c >= 0 and r <= len(matrix) - 1 and c <= len(matrix) - 1:
                        if matrix[r][c] == "@":
                            neighbours += 1
                if neighbours < 4:
                    count += 1
                    matrix[row][col] = "x"
        if count == prev_count:
            break
    return count
                            


if __name__ == "__main__":
    print(main())