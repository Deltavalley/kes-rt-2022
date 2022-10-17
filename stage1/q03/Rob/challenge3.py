from itertools import permutations

nums = '123456'
for comb in permutations(nums, 6):
    first_term = int(comb[0] + comb[1])
    second_term = int(comb[2] + '5' + comb[3])
    third_term = int(comb[4] + '4' + comb[5])
    if (second_term - first_term) == (third_term - second_term):
        print(first_term, second_term, third_term)
        print('Multiplies to', (first_term * second_term * third_term))
        print('\n')
