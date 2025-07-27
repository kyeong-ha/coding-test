input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 풀이: 모두 0으로 만드는 경우와 모두 1으로 만드는 경우 각각 계산하여 최소값을 리턴한다
    count_to_all_zero = 0
    count_to_all_one = 0

    # 1. 모두 0으로 만드는 경우
    # 1.1. 첫 숫자가 1인 경우: 뒤집기
    if string[0] == 1:
        count_to_all_zero += 1
    # 1.2. 숫자가 0 -> 1로 바뀌는 경우: 뒤집기
    for i in range(0, len(string)-1):
        if string[i] == '0' and string[i+1] == '1':
            count_to_all_zero += 1

    # 2. 모두 1으로 만드는 경우
    # 2.1. 첫 숫자가 0인 경우: 뒤집기
    if string[0] == 0:
        count_to_all_one += 1
    # 2.2. 숫자가 1 -> 0로 바뀌는 경우: 뒤집기
    for i in range(0, len(string)-1):
        if string[i] == '1' and string[i+1] == '0':
            count_to_all_one += 1

    return min(count_to_all_one, count_to_all_zero)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)