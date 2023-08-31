import itertools

def minimize_difference(lst):
    decimals = [int(binary, 2) for binary in lst]

    def find_least_difference(num):
        if len (num) == 2:
            return abs(num[0] - num[1])
        
        min_diff = float('inf')

        for a, b in itertools.combinations(num, 2):
            new_nums = [n for n in num if n not in [a, b]]
            new_nums.append(a + b)
            diff = find_least_difference(new_nums)
            min_diff = min(min_diff, diff)

        return min_diff 
    
    return find_least_difference(decimals)
    
lst = ["0001", "0011", "0101", "1011","1101","1111"]
print(minimize_difference(lst))