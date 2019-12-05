# Chapter14-1
# 2019-12-05 20:43
# 코드잇 프로그래밍 기초 남은거 빠르게 끝내기

# 알고리즘

# 선형 탐색

def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

# 이진 탐색 - 반복문

def binary_search(element, some_list):
    #인덱스 초기값 설정
    start_index = 0
    end_index = len(some_list) - 1
    
    #시작 인덱스가 끝인덱스 보다 적을때 루프(두 값이 같다면 빠져나온다)
    while start_index < end_index:
        
        #중간 인덱스값 설정
        mid_index = round((start_index + end_index) / 2)
        
        #element 와 중간인덱스의 값이 같다면
        if element == some_list[mid_index]:
            return mid_index
        
        #element가 작다면
        elif element < some_list[mid_index]:
            end_index = mid_index
        
        #element가 크다면
        elif element > some_list[mid_index]:
            start_index = mid_index
            
    #반복문에서 빠져나왔을때        
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))