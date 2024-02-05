"""
https://www.acmicpc.net/problem/9019
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 힌트 참조 후 30분 소요
    - 공식이 주어짐
        - n = ((d1 * 10 + d2) * 10 + d3) * 10 + d4
        - D : n *= 2
        - S : n -= 1 (이 때 n 이 0이면 9999 가 들어감을 주의)
        - L : popleft -> append
        - R : pop -> appendleft
    - 트리 형태로 뻗어나감 + 최소한의 나열 -> BFS

    - 자꾸 메모리초과 발생 -> 왜?
        - 중복되는 수를 계속 큐에 추가하므로
        - 그럼 중복되는 수를 빼자 -> 집합으로 계산 -> 시간초과...ㅠㅠ
        - 힌트) visited 배열을 만들면 됨!

    - 123 -> L 결과는 1230 임
        - 이에 주의해서 L, R 변환 공식을 설계해야함
    """

    import sys
    from collections import deque

    input = sys.stdin.readline

    t = int(input())

    def bfs(a, b):
        ans = deque([("", a)])
        visited = [False] * (10_001)
        visited[a] = True

        while ans:
            tmp_command, tmp_a = ans.popleft()

            if tmp_a == b:
                return tmp_command

            d = (tmp_a * 2) % 10_000
            if not visited[d]:
                ans.append((tmp_command + "D", d))
                visited[d] = True

            s = (tmp_a - 1) % 10_000
            if not visited[s]:
                ans.append((tmp_command + "S", s))
                visited[s] = True

            l = tmp_a // 1000 + (tmp_a % 1000) * 10
            if not visited[l]:
                ans.append((tmp_command + "L", l))
                visited[l] = True

            r = tmp_a // 10 + (tmp_a % 10) * 1000
            if not visited[r]:
                ans.append((tmp_command + "R", r))
                visited[r] = True

    for _ in range(t):
        a, b = map(int, input().split())

        print(bfs(a, b))


if __name__ == "__main__":
    try1()
