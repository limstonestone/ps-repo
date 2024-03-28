"""
https://www.acmicpc.net/problem/2217
"""


def try1():
    """
    - 약 24분 소요
    - N이 10만이므로 로프를 고르는 경우의 수를 직접 계산할 수는 없음
    - 그럼 로프를 어떻게 골라야하는가?
        - 로프의 최소, 최대에 핵심이 있을듯함
    - 가장 약한 로프를 들었을 때, 로프를 하나 더 든다면?
        - 두개의 합을 평균한 것은 무조건 가장 약한 로프보다 클 수 밖에 없음
        - 반대로, 두개의 합의 평균 * 2까지는 무조건 들 수 있다는 뜻
    - 그럼 i개를 든다면?
        - i개의 합의 평균 * i 까지는 무조건 들 수 있음
    - 이게 최댓값인가?
        - 만약 여기서 무게가 1이 추가된다고 생각하면, 가장 최소값의 조건을 만족하지 못할 것
        - 즉 이게 최대값임
    - 최소값이 꼭 전체 로프의 최소값일 필요는 없음
        - 로프는 주어지고 이 중에서 내가 고르는 것이기 때문에 모든 최소값을 순회하며 확인
    - 해당 로직을 점화식으로 구현
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    weights = [int(input()) for _ in range(n)]
    weights.sort(reverse=True)

    ans = 0

    for i in range(n):
        ans = max(ans, weights[i] * (i + 1))  # i 가 0부터 시작하므로 + 1

    print(ans)


if __name__ == "__main__":
    try1()
