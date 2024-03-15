"""
https://www.acmicpc.net/problem/20529
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 전체 학생을 다 받을 필요가 없음, MBTI 가 발생할 전체 경우의 수는 16
        - 따라서 Counter 의 키를 활용 -> 삼중 반복문을 사용해도 문제될 것 없음
        - Counter 의 값에서 정렬 후 횟수가 3이 나오면 0을 출력하도록
    - 왜인지 모르겠지만 계속해서 틀림...

    - 답지 참조
        - 최대 경우의수가 16 이므로 n 이 33 이상이라면 무조건 3개는 겹침
        - 따라서 답이 무조건 0이됨
        - 즉 전체 경우의수를 32로 확 줄일 수 있음 -> 브루트포스 가능
            - 이를 "비둘기집 원리" 라고 함
    """
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        mbti = input().split()
        ans = 1e9

        if n > 32:
            print(0)
        else:
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        tmp = 0
                        if i == j or j == k or i == k:
                            continue
                        for x in range(4):
                            tmp += mbti[i][x] != mbti[j][x]
                            tmp += mbti[i][x] != mbti[k][x]
                            tmp += mbti[j][x] != mbti[k][x]
                        ans = min(tmp, ans)
            print(ans)


if __name__ == "__main__":
    try1()
