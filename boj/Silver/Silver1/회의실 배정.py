"""
https://www.acmicpc.net/problem/1931
"""


def try1():
    """
    - 약 1시간 풀이 후 반례를 보고 해결
    - 입력 최대 10만 -> O(NlogN), 입력 범위가 매우 큼
    - 규칙을 살펴보면, 종료시간을 기준으로 정렬했을 떄 다음 시작시간이 채택된 마지막의 종료시간보다 늦어질 떄 채택하면 됨
    - python 내장 sort 함수 사용 시, key=lambda 에 튜플 형태를 넣어주면 해당 순서대로 정렬을 수행함
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    times = list()
    for _ in range(n):
        s, e = map(int, input().split())
        times.append((s, e))

    times = sorted(times, key=lambda x: (x[1], x[0]))
    ans = [times[0]]

    for s, e in times[1:]:
        if s >= ans[-1][1]:  # 다음 시작시각이 최근 종료시각보다 늦어지는 시점 업데이트
            ans.append((s, e))

    print(len(ans))


if __name__ == "__main__":
    try1()
