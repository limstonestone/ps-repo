"""
https://www.acmicpc.net/problem/9012
"""


def try1():
    """
    - 약 15분 소요
    - 우선 "(" 와 ")" 의 개수가 다르다면 정답은 "NO"
        - 같더라도 열린 괄호보다 닫힌 괄호가 많아지는 순간에 정답은 "NO"
        - 열린 괄호는 닫힌괄호보다 많은 순간이 오더라도 나중에 닫힐 여지가 있으니 문제 없음
    """
    import sys

    input = sys.stdin.readline
    n = int(input())

    for _ in range(n):
        sequence = input().rstrip()
        left, right = 0, 0
        status = "YES"
        for seq in sequence:
            if seq == "(":
                left += 1
            else:
                right += 1
                if right > left:
                    status = "NO"
                    break

        print(status if left == right else "NO")


def try2():
    """
    - 약 4분 소요
    - 두 문자 "(", ")" 의 개수가 같은지 확인하면 끝
        - 마지막만 같으면 되는 것이 아니라, 중간에 어긋나는 부분이 있으면 중단해야 함
    """
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        ps = input().rstrip()
        left = 0

        for x in ps:
            if x == "(":
                left += 1
            else:
                left -= 1
                if left < 0:  # ")" 가 "("보다 많을 경우 중단
                    left = -1
                    break

        print("YES" if left == 0 else "NO")  # 왼쪽과 오른쪽의 개수가 같을때만 YES


if __name__ == "__main__":
    try2()
