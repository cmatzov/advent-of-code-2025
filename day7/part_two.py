def main():
    f7 = open("day7/input7.txt")
    matrix = [list(row) for row in f7.read().splitlines()]

    starting_point = len(matrix[0]) // 2
    beams = {starting_point: 1}

    for row_idx in range(2, len(matrix), 2):
        for beams_idx, beams_count in list(beams.items()):
            if matrix[row_idx][beams_idx] == "^":
                beams[beams_idx - 1] = beams.get(beams_idx - 1, 0) + beams_count
                beams[beams_idx + 1] = beams.get(beams_idx + 1, 0) + beams_count
                del beams[beams_idx]

    return sum(beams.values())


if __name__ == "__main__":
    print(main())

# Мерси Данчо