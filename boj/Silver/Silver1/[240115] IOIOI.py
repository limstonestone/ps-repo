"""
https://www.acmicpc.net/problem/5525
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - n 이 백만 이하 -> O(NlogN) ~ O(N)
    - 단순 문자열 슬라이싱을 활용하면 서브태스크2 에서 시간복잡도 이슈 발생

    - 답지 참조
        - P 와 직접 대조하지 않고 건너 띄면서 인덱싱 -> 시간 절약 + P가 길더라도(N이 크더라도) 문제 없음
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    s = input().rstrip()

    i, cnt, ans = 0, 0, 0

    while i < (m - 1):
        if s[i : i + 3] == "IOI":
            i += 2  # P 를 만족한다면 칸 이동
            cnt += 1  # cnt : n 까지 도달하는 지 확인
            if cnt == n:  # P_n 과 동일해진다면
                ans += 1  # 정답 증가
                cnt -= 1  # 이미 셈한 부분 건너띄기

        else:
            i += 1
            cnt = 0

    print(ans)


if __name__ == "__main__":
    try1()
