def main():
    f2 = open("day2/input2.txt")
    input_ranges = [ id_range for id_range in (f2.read()).split(",")]

    tot = 0
    for id_range in input_ranges:
        numbers = [id_range.split("-")[0], id_range.split("-")[1]]
        for number in range(int(numbers[0]), int(numbers[1]) + 1):
            number_str = str(number)
            invalid = False
            for i in range(2, len(number_str) + 1):
                if len(number_str) % i == 0:
                    part_size = len(number_str) // i
                    chunks = [number_str[j:j+part_size] for j in range(0, len(number_str), part_size)] ## stack overflow
                    if len(set(chunks)) == 1:
                        invalid = True
                        break
            if invalid:
                tot += number
    return tot

if __name__ == "__main__":
    main()