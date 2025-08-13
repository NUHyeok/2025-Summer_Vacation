def merge(list1, list2):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    i = 0
    j = 0
    list = []
    
    if len(list1) > 1:
        list1 = merge(list1[:(len(list1) // 2)], list1[len(list1)//2 :])
    if len(list2) > 1:
        list2 = merge(list2[:(len(list2) // 2)], list2[len(list2)//2 :])
    
    while True:
        if i == len(list1):
            for k in range(j, len(list2)):
                list.append(list2[k])
            break
        
        elif j == len(list2):
            for k in range(i, len(list1)):
                list.append(list1[k])
            break
        
        elif list1[i] > list2[j]:
            list.append(list2[j])
            j += 1
        
        elif list1[i] <= list2[j]:
            list.append(list1[i])
            i += 1
             
    return list

# 합병 정렬
def merge_sort(my_list):
    # 여기에 코드를 작성하세요
    mid = len(my_list) // 2
    return merge(my_list[:mid], my_list[mid:])

# 테스트 코드
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
