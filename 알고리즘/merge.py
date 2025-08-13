def merge(list1, list2):
    # 여기에 코드를 작성하세요
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
    
    
        
    
# 테스트 코드
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))