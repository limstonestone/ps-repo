"""
https://www.acmicpc.net/problem/2512
"""


def try1():
    """
    - 약 50분 풀이 후 실패로 답지 참조
    - n 이 1만 -> O(N^2) ~ O(NlogN) 알고리즘 필요
    - 탐색 범위가 10억으로 매우 넓음 -> 이진 탐색 O(logN)

    - 답지 풀이
        - 찾고자하는 "값" 을 중심점으로 두어야 함
        - 주어진 배열 내에서 탐색하는 것이 아니라 정해진 범위 내의 모든 값들에 대해서 탐색 가능
            - 이진탐색의 장점이 탐색 범위가 매우 넓을 때도 가능하기 때문임
            - 이 부분을 캐치하지 못했음
    """

    import sys

    input = sys.stdin.readline

    def binary_search(start, end):
        answer = 0

        while start <= end:
            mid = (start + end) // 2

            # 정수 상한액을 적용하여 sum 적용한 결과
            temp_sum = sum([x if x <= mid else mid for x in budget])

            # 합이 국가 총 예산보다 크다면 상한액 줄이기
            if temp_sum > target_sum:
                end = mid - 1

            # 국가 총 예산액보다 작거나 같다면 상한액 늘리기
            elif temp_sum <= target_sum:
                start = mid + 1
                answer = mid  # 정답 값 업데이트

        return answer

    N = int(input())
    budget = list(map(int, input().split()))
    max_budget = max(budget)

    target_sum = int(input())

    # 국가 총 예산이하라면 정수 상한액은 예산 중 최대 값
    if target_sum >= sum(budget):
        print(max_budget)

    # 아니라면 이진 탐색
    else:
        print(binary_search(0, max_budget))


if __name__ == "__main__":
    try1()
