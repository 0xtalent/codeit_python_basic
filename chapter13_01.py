# Chapter13-1
# 2019-12-05 19:18
# 코드잇 프로그래밍 기초 남은거 빠르게 끝내기

# 정렬

# 선택 정렬 코드 짜기

def selection_sort(my_list):
    # 바깥쪽 반복문
    for i in range(len(my_list)):
        min_index = i

        # 안쪽 반복문
        for j in range(i + 1, len(my_list)):
            value = my_list[j]
            if value < my_list[min_index]:
                min_index = j
        
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp
        
some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)

# 삽입 정렬 코드 짜기

def insertion_sort(my_list):
    for high_index in range(len(my_list)):
        low_index = high_index - 1
        for low_index in range(low_index, -1, -1):
            if my_list[low_index] > my_list[high_index]:
                temp = my_list[low_index]
                my_list[low_index] = my_list[high_index]
                my_list[high_index] = temp
                high_index = high_index - 1
            else:
                break
    return my_list

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)

# 완벽한 정답은?

# 삽입 정렬
def insertion_sort2(my_list):
    for i in range(len(my_list)):
        key = my_list[i]

        # i - 1부터 시작해서 왼쪽으로 하나씩 확인
        # 왼쪽 끝까지(0번 인덱스) 다 봤거나
        # key가 들어갈 자리를 찾으면 끝냄
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j = j - 1

        # key가 들어갈 자리에 삽입
        # 왼쪽 끝까지 가서 j가 -1이면 0번 인덱스에 key를 삽입
        my_list[j + 1] = key

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort2(some_list)
print(some_list)

# 너무 어려워요. 지금은 돌아가는 개념만 이해하고 넘어갈게요

# 합병 정렬 코드 짜기
"""
# 두 리스트 합치기
def merge(list1, list2):
    new_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    # list1에 남은 원소가 있다면, new_list에 추가하기
    if len(list1) > i:
        # new_list의 길이가 list1 + list2 의 길이와 같아질 때까지 반복
        while len(new_list) < len(list1 + list2):
            new_list.append(list1[i])
            i += 1

    # list2에 남은 원소가 있다면, new_list에 추가하기
    if len(list2) > j:
        # new_list의 길이가 list1 + list2 의 길이와 같아질 때까지 반복
        while len(new_list) < len(list1 + list2):
            new_list.append(list2[j])
            j += 1

    return new_list

# 합병 정렬
def merge_sort(my_list):
    # Base Case
    if len(my_list) <= 1:
        return my_list

    # Recursive Case: left와 right로 my_list를 나누어준다.
    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]

    # Recursive Case: merge_sort 함수를 재귀적으로 호출해 my_list를 잘게 쪼갠뒤 merge 함수로 합치는 과정을 반복한다.
    return merge(merge_sort(left), merge_sort(right))


some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)
"""
# 완벽한 정답은?
# 두 리스트 합치기
def merge(list1, list2):
    merged_list = []
    i = 0
    j = 0

    # 정렬되어 있는 list1과 list2의 원소들을 차례로 비교하여, 더 작은 원소를 merged_list에 추가하기
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # list1에 남은 원소가 있다면, merged_list에 추가하기
    if i < len(list1):
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 원소가 있다면, merged_list에 추가하기
    if j < len(list2):
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1

    return merged_list

# 합병 정렬
def merge_sort(my_list):
    # Base Case
    if len(my_list) <= 1:
        return my_list

    # Recursive Case: left와 right로 my_list를 나누어준다.
    left = my_list[:len(my_list) // 2]
    right = my_list[len(my_list) // 2:]

    # Recursive Case: my_list를 잘게 쪼개는 과정을 재귀적으로 반복하고, merge 함수를 사용하여 합쳐준다.
    return merge(merge_sort(left), merge_sort(right))

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)