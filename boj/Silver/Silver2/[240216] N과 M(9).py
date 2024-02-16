"""
https://www.acmicpc.net/problem/15663
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 중복 확인하는 경우 시간복잡도를 잘 계산하지않으면 시간초과 발생하기 매우 쉬움
    - Counter 와 Set 자료형을 활용해 중복 처리 시도
        - 46%에서 실패 .. ㅠㅠ
        - 원인을 찾아보니 같은 수열이지만 순서가 다른 경우에도 다른 문자열로 취급됨 (문자로 변환하는 과정)

    - 답지 풀이
        - 재귀문에 들어가기 전 방문 처리를 한 후, 재귀문을 탈출(길이를 만족)하면 방문을 해제하는 테크닉 사용
        - if i > 0 and nums[i] == nums[i - 1] and (not visited[i - 1]):
            - i > 0
                첫 번째 수는 무조건 사용됨
            - nums[i] == nums[i - 1] and (not visited[i - 1])
                현재 수가 이전 수와 같고(앞 조건), 이전 수가 사용되지 않았다면 현재 수 사용 X
    """
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    seq = []
    visited = [False] * (n)

    def dfs():
        if len(seq) == m:
            print(*seq)
            return

        for i in range(n):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and (not visited[i - 1]):
                continue

            seq.append(nums[i])
            visited[i] = True
            dfs()
            seq.pop()
            visited[i] = False

    dfs()


if __name__ == "__main__":
    try1()
