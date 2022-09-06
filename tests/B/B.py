# не оптимальный алгоритм, доработать
number_of_disciplines = int(input())
disciplines = dict()
for i in range(number_of_disciplines):
    name, number = input().split(',')
    disciplines.setdefault(name, int(number))
number_of_participants = int(input())
participants = dict()
for i in range(number_of_participants):
    name, disc, num_trick, penalty = input().split(',')
    participants.setdefault(name, (disc, int(num_trick), int(penalty)))
res = []
for name, number in disciplines.items():
    filtered_lst = list(filter(lambda x: x[1][0] == name, participants.items()))
    sortered_lst = sorted(filtered_lst, key=lambda x: (-x[1][1],x[1][2]))
    for i in range(number):
        if i <= len(sortered_lst) - 1:
            res.append(sortered_lst[i][0])

for name in sorted(res):
    print(name)
