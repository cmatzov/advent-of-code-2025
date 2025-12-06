test_ranges = [ "3-5", "16-20", "10-14", "12-18" ]

f5 = open("day5/input5.txt")
ingredient_ranges = list(f5.read().splitlines())

def main():
    count  = 0
    rows = [(int(a), int(b)) for a, b in (row.split("-") for row in ingredient_ranges)]
    rows.sort(key=lambda x: x[0])
    new_list = []
    for i in range(len(rows)):
        if not new_list:
            new_list.append(rows[i])
            continue
        prev = new_list[-1]
        curr = rows[i]
        if prev[1] >= curr[0]:
            new_list[-1] = (prev[0], max(prev[1], curr[1]))
        else:
            new_list.append(rows[i])

    for ingredient_range in new_list:
        count += (ingredient_range[1] - ingredient_range[0]) + 1

    return count

if __name__ == "__main__":
    print(main())