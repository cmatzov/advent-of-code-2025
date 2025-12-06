def find_max(arr, max_length):
    max_number = arr[0]
    index = 0
    for i in range(len(arr) - max_length + 1):
        if arr[i] > max_number:
            max_number = arr[i]
            index = i
    return max_number, index

def day3_part2(input):
    final = ""
    result = []
    arr = list(input)
    max_length = 12
    while max_length > 0:
        number, index = find_max(arr, max_length)
        result.append(number)
        max_length -= 1
        arr = arr[index + 1:]
        if len(arr) == max_length:
            result.extend(arr)
            break
    for item in result:
        final += item
    return final

def main():
    f3 = open("day3/input3.txt")
    inputs = f3.read().splitlines()

    total = 0
    for input in inputs:
        total += int(day3_part2(input))
    
    return total

if __name__ == "__main__":
    main()