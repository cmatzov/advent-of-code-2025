def main(starting_point=50, zeros=0):
    f = open("day1/input.txt")
    input_numbers = (f.read()).splitlines()

    for num in input_numbers:
        direction = num[0]
        clicks = int(num[1:])
        for click in range(clicks):
            if direction == "L":
                starting_point -= 1
                starting_point %= 100
            elif direction == "R":
                starting_point += 1
                starting_point %= 100
        
            if starting_point == 0:
                zeros += 1
    return zeros 

if __name__ == "__main__":
    main()