# 충분히 작은 수 or array[0]을 fix한 뒤, 남은 원소와 비교하여 큰 숫자를 찾아낸다 => O(n)
def find_max_num(array):
    max_num = -999999 # max_num = array{0]
    for num in array:
        if max_num < num:
            max_num = num
    return max_num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))