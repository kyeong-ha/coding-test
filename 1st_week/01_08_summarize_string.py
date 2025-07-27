def summarize_string(input_str):
    # 알파벳의 빈도수 배열을 생성한 뒤, input_str을 순회하면서 각 문자의 유니코드에 해당되는 index에 빈도수를 체크한다.
    result = ""

    alphabet_occurrence_array = [0] * 26
    for s in input_str:
        alphabet_occurrence_array[ord(s)-ord("a")] += 1

    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] > 0: # 빈도수가 0보다 큰 경우에만 서식에 맞게 출력
            result += chr(index+97) + str(alphabet_occurrence_array[index]) + "/"

    return result[:-1]

input_str = "acccdeee"
print(summarize_string(input_str))