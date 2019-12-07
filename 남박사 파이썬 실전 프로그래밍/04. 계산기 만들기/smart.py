# 남박사10-1
# 2019-12-07 21:15

# 콘솔 스마트 계산기 만들기 스마트-파이썬 기초, 계산기 로직, 리스트, 반복문

opertor = ["+", "-", "*", "/", "="]
user_input = "5656 + 51212 * 10"

string_list = []
lop = 0

# 리스트에 몇번째에 있는지도 알아야 하니까 enumerate로 감싸서
for i, s in enumerate(user_input):
    if s in opertor:
        if user_input[lop:i].strip != "":
            string_list.append(user_input[lop:i])
            string_list.append(s)
            lop = i + 1
print(string_list)