"""
https://www.acmicpc.net/problem/1620
"""


def try1():
    """
    - 약 8분 소요
    - key 와 value 를 활용하여 해결
        - isdigit() 메소드를 활용하여 문자열이 들어오더라도 숫자인지 판단가능
    """

    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    pok_dict = dict()

    for i in range(1, n + 1):
        pok = input().rstrip()
        pok_dict[pok] = i

    key = [0] + list(pok_dict.keys())

    for _ in range(m):
        question = input().rstrip()

        if question.isdigit():  # 문자열이 숫자인지 아닌지 확인하는 메소드
            print(key[int(question)])

        else:
            print(pok_dict[question])


if __name__ == "__main__":
    try1()
