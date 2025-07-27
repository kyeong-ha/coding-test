input = 20
import math

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number):
        # 1번째 풀이: 2~number-1 까지 해당하는 n을 순서대로 조회하면서, 2~n-1로 단 1번도 나누어 떨어지지 않는 수를 소수 배열에 추가한다.
        # for i in range(2, n):

        # 2번째 풀이: 2~number-1 까지 해당하는 n을 순서대로 조회하면서, n보다 작은 소수로 단 1번도 나누어 떨어지지 않는 수를 소수 배열에 추가한다.
        # for i in prime_list:

        # 3번째 풀이: 2~number-1 까지 해당하는 n을 순서대로 조회하면서, 2~number의 제곱근으로 단 1번도 나누어 떨어지지 않는 수를 소수 배열에 추가한다.(에라토스테네스의 체)
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                break
        else:
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)