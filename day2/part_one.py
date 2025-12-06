def main():
    f2 = open("day2/input2.txt")
    input_ranges = [ id_range for id_range in (f2.read()).split(",")]

    sum = 0
    for id_range in input_ranges:
        numbers = [id_range.split("-")[0], id_range.split("-")[1]]
        for number in range(int(numbers[0]), int(numbers[1]) + 1):
            number_str = str(number)
            if len(number_str) % 2 == 0:
                first_half = (number_str[:len(number_str) // 2])
                second_half = (number_str[(len(number_str) // 2):])
                if first_half == second_half:
                    sum += number
    return sum


if __name__ == "__main__":
    main()