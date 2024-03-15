"""
https://www.acmicpc.net/problem/1316
"""


def try1():
    """
    - 약 8분 소요
    - 단어의 길이가 최대 100 -> 복잡하게 생각X, 구현
    - 이전 단어 / 현재 단어를 비교 + 단어 사전 활용
        - 집합 자료형을 활용하여 in 연산시 시간복잡도 O(1)
            - 사실 알파벳이라 길이가 적어 큰 의미 없긴함
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = n

    for _ in range(n):
        word = list(input().rstrip())
        used_words = set()
        prev_word = ""
        while word:
            cur_word = word.pop()
            if prev_word != cur_word:  # 현재단어와 이전단어가 일치하지 않을 때,
                if cur_word in used_words:  # 이미 사용된 단어라면 정답 -1
                    ans -= 1
                    break
                else:  # 아직 사용된 단어가 아니라면
                    used_words.add(cur_word)  # 사용 리스트에 추가
                    prev_word = cur_word  # 이전 단어 갱신

    print(ans)


if __name__ == "__main__":
    try1()
