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