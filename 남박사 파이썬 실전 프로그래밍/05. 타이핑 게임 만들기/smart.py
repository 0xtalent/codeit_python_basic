'''
한글 = ((초성 * 21) + 중성) * 28 + 종성 + 44032

초성 = ((x - 44032) / 28) / 21
중성 = ((x - 44032) / 28) % 21
종성 = (x - 44032) % 28
'''

CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅛ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "뵤", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

# print(len(CHO))
# print(len(JUNG))
# print(len(JONG))

# a = chr(((0 * 21) + 0) * 28 + 0 + 44032)
# print(a)

user_input = input("입력> ")
word_list = list(user_input)

break_word = []

for k in word_list:
    if ord(k) >= ord("가") and ord(k) <= ord("힣"):
        # 유니코드 상 몇번째 글자인지 인덱스를 구한다.
        char_index = ord(k) - ord('가')

        # 초성 = ((문자코드 - 44032) / 28) / 21
        char1 = int((char_index / 28) / 21)
        break_word.append(CHO[char1])

        # 중성 = ((x - 44032) / 28) % 21
        char2 = int((char_index / 28) % 21)
        break_word.append(JUNG[char2])

        # 종성 = (x - 44032) % 28
        char3 = int(char_index % 28)

        if char3 > 0:
            break_word.append(JONG[char3])
    
    else:
        break_word.append(k)

print("입력: {}".format(user_input))
print("분해: {}".format(break_word))