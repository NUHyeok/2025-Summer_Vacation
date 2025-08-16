# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


    
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    
    if start == end:
        return my_list
    
    b = start
    pivot = my_list[end]
    
    
    for i in range(start, end):
        if my_list[i] <= pivot:
            swap_elements(my_list, i, b)
            b += 1
    
    swap_elements(my_list, b, end)
    
    #if start < b-1:
    #   partition(my_list, start, b-1)
        
    #if b+1 < end:
    #    partition(my_list, b+1, end)
        
    return b

    
# 퀵 정렬
def quicksort(my_list, start, end):
    # 여기에 코드를 작성하세요
        
    if start == end:
        return my_list
    
    b = start
    pivot = my_list[end]
    
    
    for i in range(start, end):
        if my_list[i] <= pivot:
            swap_elements(my_list, i, b)
            b += 1
    
    swap_elements(my_list, b, end)
    
    if start < b-1:
       quicksort(my_list, start, b-1)
        
    if b+1 < end:
        quicksort(my_list, b+1, end)
    
    return my_list


# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)