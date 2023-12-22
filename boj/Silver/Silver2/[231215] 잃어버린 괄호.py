"""
https://www.acmicpc.net/problem/1541
"""


def try1():
    """
    - 약 40분 소요
    - 입력 식의 길이는 최대 50 -> 여유로움
    - 최소로 만들기 위해서는 - 를 마주친 순간 다음 - 가 나올 때까지 + 들을 전부 괄호쳐주면 됨
        - 즉, 최초 - 를 마주친 순간부터는 뒤의 숫자들을 모두 빼버리는 것과 동치
    """
    import sys

    input = sys.stdin.readline

    sequence = input().rstrip().split("-")

    answer = 0
    for i, seq in enumerate(sequence):
        seq = seq.split("+")
        seq = sum(map(int, seq))

        answer = answer - seq if i != 0 else answer + seq  # 맨 처음 숫자는 더해줘야함

    print(answer)


if __name__ == "__main__":
    try1()
