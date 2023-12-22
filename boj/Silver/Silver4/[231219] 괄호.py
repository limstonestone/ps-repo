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


if __name__ == "__main__":
    try1()
