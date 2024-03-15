"""
https://www.acmicpc.net/problem/10798
"""


def try1():
    """
    - 약 10분 소요
    - 총 들어오는 길이가 가로5, 세로 최대 15이므로 시간복잡도 충분
        - 따라서 "!" 로 패딩(여백을 채움)활용
    """
    import sys

    input = sys.stdin.readline
    words = []
    for i in range(5):
        word = input().rstrip()
        word += "!" * (15 - len(word))  # 길이가 15가 될때까지 !로 채움
        words.append(word)

    answer = ""
    for j in range(15):
        for i in range(5):
            if words[i][j] != "!":  # !는 무시
                answer += words[i][j]

    print(answer)


if __name__ == "__main__":
    try1()
