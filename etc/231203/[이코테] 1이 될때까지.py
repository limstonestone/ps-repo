"""
https://blex.me/@mildsalmon/chap-3-그리디-1이-될-때까지
"""


### 1st trial (time : 3m)
def try1():
    """
    - 최대한 많이 나누어야 소요되는 횟수가 적음 -> 그리디
    - 한 loop 당 1씩 빼는 것이 아니라 나누어 떨어지는 수가 될때까지 한번에 연산 가능, 시간효율증가
        - target = (n // k) * k
        - ans += (n - target)
        - result += 1
        - n //= k
    """
    n, k = map(int, input().split())
    ans = 0

    while n != 1:
        ans += 1
        if n % k == 0:
            n /= k
        else:
            n -= 1

    print(ans)


if __name__ == "__main__":
    try1()
