"""
https://www.acmicpc.net/problem/11053
"""


def try1():
    """
    - 약 20분 풀이 후 실패로 답지 참조
    - 이전의 연산 결과를 참고해 다음 연산에 활용 -> DP

    - 답지 풀이
        - 이중 반복문을 활용하여 이전 값들에 대해서 모두 탐색을 진행
        - O(N^2) 풀이를 배제하고싶어 반복문 하나로 풀이하려했지만 아이디어가 떠오르지않았음
            - 어차피 주어진 문제의 입력 범위는 충분하니 우선 풀이해내는 것에 집중하기
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    seq = list(map(int, input().split()))

    dp = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:  # 현재 값이 특정 이전 값보다 더 크다면
                dp[i] = max(dp[i], dp[j] + 1)  # 기존 설정 부분 수열 그대로 vs 부분 수열을 새로 정의하기

    print(max(dp))


if __name__ == "__main__":
    try1()
