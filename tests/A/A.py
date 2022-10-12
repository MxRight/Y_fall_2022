from time import perf_counter

def main(A, B):
    dict_of_letter = {i: A.count(i) for i in A}
    result = ['I' for i in range(len(A))]
    for num, symbol in enumerate(B):
        if symbol == A[num]:
            result[num] = 'P'
            dict_of_letter[symbol] -= 1
    for num, symbol in enumerate(B):
        if symbol != A[num]:
            if symbol not in dict_of_letter or dict_of_letter[symbol] == 0:
                continue
            else:
                if A.find(symbol) >= 0:
                    result[num] = 'S'
                    dict_of_letter[symbol] -= 1
    return ''.join(result)


def tests():
    assert main('CLOUD', 'CUPID') == 'PSIIP', 'PSIIP !'
    assert main('ALICE', 'ELIBO') == 'SPPII', 'SPPII !'
    assert main('ABCBCYA', 'ZBBACAA') == 'IPSSPIP', 'IPSSPIP !'


if __name__ == "__main__":
    # tests()
    #start = perf_counter()   #  засекаем время начала работы функции
    main(input(), input())
    #finish = perf_counter()  #  засекаем окончание работы функции
    #print(finish - start)
