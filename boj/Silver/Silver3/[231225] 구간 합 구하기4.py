"""
https://www.acmicpc.net/problem/11659
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 단순히 슬라이싱으로 구현하면 시간 초과
        - N 이 10만 -> O(NlogN) 알고리즘이 필요, M(최대 10만)도 고려해야함
    - numbers 가 정해져있으므로, 반복되는 연산이 있어 배열에 저장해놓으면 좋음
        - j 가 i 보다 무조건 크거나 같으므로 상/하삼각행렬
        - 구현했더니 메모리 초과..!

    - 답지 풀이
        - 구간합은 S[j] - S[i-1] 로 표현할 수 있는 것이 핵심
            - 여기서 S 는 누적합
        - 공식처럼 외워두자..!

    """

    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    cumsum = [0]  # j 에서 인덱싱 오류 방지
    tmp_sum = 0

    for i in range(n):  # 누적합 저장
        tmp_sum += numbers[i]
        cumsum.append(tmp_sum)

    for _ in range(m):
        i, j = map(int, input().split())
        print(cumsum[j] - cumsum[i - 1])


if __name__ == "__main__":
    try1()
