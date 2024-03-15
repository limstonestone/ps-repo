"""
https://www.acmicpc.net/problem/15657
"""


def try1():
    """
    - 30분 풀이
    - 백트래킹으로 풀이
    - 처음 시작으로는 아무 숫자가 들어와도 관계 X
    - 재귀 루프가 한번 끝났을 때 전체 시퀀스의 가장 왼편(정렬되었으므로)을 제거해주는 방식
    """
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())
    sequence = sorted(map(int, input().split()))

    seq = []

    def dfs(start, tmp_sequence):
        if len(seq) == m:
            print(*seq)
            return

        for i in range(len(tmp_sequence)):
            seq.append(tmp_sequence[i])
            dfs(tmp_sequence[i], tmp_sequence[i:])
            seq.pop()

    dfs(0, sequence)


def try2():
    """
    - 백트래킹 / 답지 참조 풀이
    - 본인 풀이에서 배열을 새로 동기화하는 대신 인덱싱을 활용하여 배열에 새롭게 접근 (훨씬 효율적)
    """
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    temp = []

    def dfs(start):
        if len(temp) == m:
            print(*temp)
            return
        for i in range(start, n):
            temp.append(nums[i])
            dfs(i)
            temp.pop()

    dfs(0)


if __name__ == "__main__":
    try1()
