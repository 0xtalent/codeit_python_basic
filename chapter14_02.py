# Chapter14-2
# 2019-12-06 21:28
# 코드잇 프로그래밍 기초 남은거 빠르게 끝내기

# 이진 탐색 - 반복문 완벽한 정답은?

"""
초기에 start_index는 0으로, end_index는 len(some_list) - 1로 지정해줍시다. 그리고 리스트가 이미 정렬되어 있다는 사실을 활용하여 start_index가 end_index보다 작을 때까지, 아래의 내용을 반복합니다.

element가 some_list[midpoint]와 일치한다면, 그 인덱스를 리턴하고 종료합니다.
element가 some_list[midpoint]보다 작다면, 탐색 범위의 후반부는 제외시켜도 됩니다. 따라서 end_index를 midpoint - 1로 업데이트해줍니다.
element가 some_list[midpoint]보다 크다면, 탐색 범위의 전반부는 제외시켜도 됩니다. 따라서 start_index를 midpoint + 1로 업데이트해줍니다.
반복문이 종료될 때까지 원소를 찾지 못하면, None의 값을 리턴해줍니다.
"""

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif element < some_list[midpoint]:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1

    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
