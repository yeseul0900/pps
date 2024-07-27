def determine_doremi(input_list):
    list_int = list(map(int, input_list))
    list_sort = sorted(list_int)
    list_reverse_sort = sorted(list_int, reverse=True)

    if list_int == list_sort:
        print("ascending")
    elif list_int == list_reverse_sort:
        print("descending")
    else:
        print("mixed")

input_list = input().split()
determine_doremi(input_list)
