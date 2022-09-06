# валится на 13 тесте, найти ошибку в алгоритме
with open('input.txt', 'r') as file_in:
    data = file_in.read()

def verification(var):
    stack_in = ['']
    stack_n = []
    lst = ['{','}']
    for i, v in enumerate(var):
        if stack_in[-1] == '{' and v == '}':
            stack_in.pop(-1)
            stack_n.pop(-1)
        else:
            if v in lst:
                stack_in.append(v)
                stack_n.append(i+1)
    if len(stack_in) == 2 and len(stack_n) == 1:
        return stack_n[-1]
    else:
        return -1

print(verification(data))
