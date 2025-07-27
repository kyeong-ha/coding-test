input = "abadabac"

def find_not_repeating_first_character(string):
    # # 1번째 풀이: string[0] 부터 순회하여 string 내에 같은 문자가 있는 경우에는 flag을 True로, 없는 경우에는 False로 설정하여 False인 경우에 해당 문자를 반환하도록 한다.
    # for target_index in range(len(string)):
    # flag = False
    # for index in range(len(string)):
    # if string[index] == string[target_index] and index != target_index:
    # flag = True
    # break
    # if flag == False:
    # return string[target_index]

    # 2번째 풀이: 알파벳의 빈도수를 담은 array을 구하여, 빈도수가 1인 알파벳 중 가장 먼저 나온 알파벳을 리턴한다. 단, 1인 빈도수가 없으면 "_"을 리턴한다.
    alphabet_occurrence_array = [0] * 26
    for char in string:
        alphabet_occurrence_array[ord(char) - ord("a")] += 1

    not_repeating_char_array = []
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] == 1:
            not_repeating_char_array.append(chr(index + 97))

    for char in string:
        if char in not_repeating_char_array:
            return char
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))