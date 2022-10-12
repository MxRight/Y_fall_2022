# неоптимальный алгоритм, доработать
A = input()
B = input()
dict_of_letter = {i: A.count(i) for i in A}
result = ['I' for i in range(len(A))]

def plagiator2000(A, B, value='first'):
    for num, symbol in enumerate(B):
        if symbol == A[num]:
            if value == 'first':
                result[num] = 'P'
                dict_of_letter[symbol] -= 1
        else:
            if value=='second':
                if A.find(symbol)>=0 and dict_of_letter[symbol] > 0:
                    result[num] = 'S'
                    dict_of_letter[symbol] -= 1
    if value=='first':
        return plagiator2000(A, B, value='second')

plagiator2000(A, B)
print(''.join(result))

"""
A = input()
B = input()
dict_of_letter = {i: A.count(i) for i in A}
result = ['I' for i in range(len(A))]

for num, symbol in enumerate(B):
    if symbol == A[num]:
            result[num] = 'P'
            dict_of_letter[symbol] -= 1

for num, symbol in enumerate(B):
    if symbol != A[num]:
        if A.find(symbol) >= 0 and dict_of_letter[symbol] > 0:
            result[num] = 'S'
            dict_of_letter[symbol] -= 1
print(''.join(result))
"""
