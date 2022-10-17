from itertools import permutations

digits = [1,2,3,4,5,6,7,8,9,0]
digits = [str(x) for x in digits]
for comb in permutations(digits, 10):
    comb = ''.join(comb)
    works = True
    for x in range(1, 11):
        if not(int(comb[:x]) % x == 0):
            works = False
        if x == 10 and works:
            print(comb)
