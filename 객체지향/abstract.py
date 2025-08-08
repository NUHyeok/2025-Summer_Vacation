def sort(my_list):
    for i in range(1, len(my_list)):
        value = my_list[i]
        j = i-1
        while j >= 0 and value < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = value
    return my_list