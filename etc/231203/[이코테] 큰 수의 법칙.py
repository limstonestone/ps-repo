"""
https://blex.me/@mildsalmon/chap-3-그리디-큰-수의-법칙
"""


### 1st trial (time : 10m)
def try1():
    """
    - 배열 내 최대값을 최대한 많이 더하는 것이 핵심 -> 그리디
    - n 은 정렬에 대한 시간복잡도를 확인하기 위해 주어진듯 함
    - 반복문 + 조건문 조합으로 풀이해낼수도 있지만, 연산 과정이 수열의 반복임
        - max1_1 + max1_2 + ... max1_k + max2 (배열의 최대 길이를 넘지 않으면 max2 추가)
    """
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))

    first_sum_n = (k) * (m // k)
    second_sum_n = m - first_sum_n

    arr = sorted(arr)
    print(first_sum_n * arr[-1] + second_sum_n * arr[-2])


if __name__ == "__main__":
    try1()
