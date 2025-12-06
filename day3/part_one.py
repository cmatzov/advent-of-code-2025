def main():
    f3 = open("day3/input3.txt")
    inputs = f3.read().splitlines()

    total = 0
    for input in inputs:
        first = 0
        second = 0
        for i in range(len(list(input)) -1):
            if int(list(input)[i]) > first:
                first = int(list(input)[i])
                index = i
        remaining = list(input)[index:]
        for j in range(1, len(remaining)):
            if int(remaining[j]) > second:
                second = int(remaining[j])
        big = str(first) + str(second)
        total += int(big)
    return total

if __name__ == "__main__":
    main()