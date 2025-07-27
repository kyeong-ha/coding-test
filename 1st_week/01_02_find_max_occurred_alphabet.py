# find_alphabet_occurrence_array 을 통해 집계된 등장횟수를 탐색하여 가장 큰 숫자를 추출한다.
def find_max_occurred_alphabet(string):
    max_occurred_alphabet = "a"
    
    alphabet_occurrence_array = find_alphabet_occurrence_array(string)

    max_occurrence_index = alphabet_occurrence_array.index(max(alphabet_occurrence_array))
    # max_occurrence = 0
    # max_occurrence_index = 0
    # for index, occurrence in enumerate(alphabet_occurrence_array):
        # if max_occurrence < occurrence:
            # max_occurrence = occurrence
            # max_occurrence_index = index
            
           
    max_occurred_alphabet = chr(max_occurrence_index+97)
    
    return max_occurred_alphabet

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            alphabet_occurrence_array[ord(char)-ord('a')] += 1
    return alphabet_occurrence_array

print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))
