# 남박사10-1
# 2019-12-07 21:15

# 콘솔 스마트 계산기 만들기 스마트-파이썬 기초, 계산기 로직, 리스트, 반복문

user_input = input("계산식을 입력하세요> ")
opertor = ["+", "-", "*", "/", "="]

string_list = []
lop = 0

# 마지막에 operator로 안끝나면 임의로 =을 추가해주자
if user_input[-1] not in opertor:
    user_input += "="

# 리스트에 몇번째에 있는지도 알아야 하니까 enumerate로 감싸서
for i, s in enumerate(user_input):
    if s in opertor:
        if user_input[lop:i].strip != "":
            string_list.append(user_input[lop:i])
            string_list.append(s)
            lop = i + 1

# =은 임의로 넣은 거니까 마지막꺼 빼고 할당
string_list = string_list[:-1]

pos = 0
while True:
    if pos + 1 > len(string_list):
        break
    if len(string_list) > pos + 1 and string_list[pos] in opertor:
        temp = string_list[pos-1] + string_list[pos] + string_list[pos+1]
        del string_list[0:3]
        string_list.insert(0, str(eval(temp)))
        pos = 0
    pos += 1
    print(string_list)