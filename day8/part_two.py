import math

f8 = open("day8/input8.txt")
boxes_locations = [[int(location) for location in box.split(",")] for box in f8.read().splitlines()]

parent = list(range(len(boxes_locations)))

def calculate_distance(a, b):
    distance = math.sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2) + pow((a[2] - b[2]), 2))
    return distance

def shortest_distance(arr):
    return sorted(arr, key=lambda x: x[0])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def main():
    distances = []
    for i in range(len(boxes_locations)):
        for j in range(i + 1, len(boxes_locations)):
            distance = tuple((calculate_distance(boxes_locations[i], boxes_locations[j]), i, j))
            distances.append(distance)
    boxes = shortest_distance(distances)
    circuits = []
    for box in boxes:
        circuits.append([box[1], box[2]])

    size = [1] * len(boxes_locations)

    for a, b in circuits:
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            parent[rootB] = rootA
            size[rootA] += size[rootB]
            last_connected = (a, b)
    
    print(boxes_locations[last_connected[0]][0] * boxes_locations[last_connected[1]][0])

if __name__ == "__main__":
    main()