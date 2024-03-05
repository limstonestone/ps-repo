"""
https://school.programmers.co.kr/learn/courses/30/lessons/12914
"""


def solution(n):
    """
    - 약 3분 소요
    - 입력 2000 -> O(NlogN) ~ O(N^2)
    - 과거의 값을 저장해뒀다가 활용 -> DP
        - 3을 뛰는 방법은 1에서 2칸을 뛰거나, 2에서 1칸을 뛰는 것과 같음
    """
    dp = [0] * (n + 2)  # 인덱싱 오류 방지
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567

    return dp[n]
