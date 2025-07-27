def find_max_plus_or_multiply(array):
  max_number = array[0]
  for i in range(1, len(array)):
    plus = max_number + array[i]
    multiply = max_number * array[i]
    if plus > multiply:
      max_number = plus
    else:
      max_number = multiply
  return max_number


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))