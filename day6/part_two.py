test_problem = [ 
    [['1','2','3'], ['3','2','8'], [' ','5','1'], ['6','4',' ']], 
    [[' ','4','5'], ['6','4',' '], ['3','8','7'], ['2','3',' ']], 
    [[' ',' ','6'], ['9','8',' '], ['2','1','5'], ['3','1','4']],
    [['*',' ',' '], ['+',' ',' '], ['*',' ',' '], ['+',' ',' ']]  
]

def main():
    final = 0
    nums = []
    for cell in range(2, -1, -1):
        for column in range(len(test_problem[0]) - 1, -1, -1):
            col = []
            for row in range(len(test_problem)):
                col.append(test_problem[row][column][cell])
            nums.append(col)
    new_list = []
    for item in nums:
        new_list.append(int(str(item[0] + item[1] + item[2])))

    groups = [new_list[i::4] for i in range(len(test_problem[0]))]
    symbols = test_problem[len(test_problem) - 1]
    list_of_symbols = []
    for symbol in symbols[::-1]:
        list_of_symbols.append(symbol[0])
    paired = list(zip(groups, list_of_symbols))
    for tup in paired:
        symbol = tup[1]
        result = 0 if symbol == "+" else 1
        for number in tup[0]:
            if symbol == "*":
                result *= number
            else:
                result += number
        final += result
    print(final)
    
if __name__ == "__main__":
    main()