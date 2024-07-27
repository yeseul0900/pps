num = int(input())
over_average_rate_list = []
for i in range(num):
    count_student = 0
    input_list = input().split()
    list_int = list(map(int, input_list))
    num_student = list_int[0]

    sum_score = sum(list_int[1:])
    average = sum_score/num_student
    for i in list_int[1:]:
        if i>average:
            count_student = count_student + 1
    rate = round(count_student/num_student * 100, 3)
    over_average_rate_list.append(rate)
    
for i in over_average_rate_list:
    print(f'{i:.3f}%')
