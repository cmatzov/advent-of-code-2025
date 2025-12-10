from shapely.geometry import Polygon

f9 = open("day9/input9.txt")

polygon = Polygon([tuple(int(num) for num in item.split(",")) for item in f9.read().splitlines()])

def main():
    f9 = open("day9/input9.txt")
    grid = [tuple(int(num) for num in item.split(",")) for item in f9.read().splitlines()]
    areas = []
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            x_1, y_1 = grid[i]
            x_2, y_2 = grid[j]

            polygon2 = Polygon([
                (x_1, y_1),
                (x_1, y_2),
                (x_2, y_2),
                (x_2, y_1),
            ])

            if polygon2.within(polygon):
                areas.append((abs(x_1 - x_2) + 1) * (abs(y_1 - y_2) + 1))
    areas.sort(reverse=True)
    print(areas[0])

main()