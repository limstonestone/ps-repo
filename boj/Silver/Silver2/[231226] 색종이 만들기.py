"""
https://www.acmicpc.net/problem/2630
"""


def solution():
    """
    - 약 40분 풀이 후 실패로 답지 참조
    - 그래프 탐색 문제라 생각하여 dfs(재귀)로 접근했지만 문제가 굉장히 복잡해졌음

    - 답지 풀이
        - 분할 정복 : 재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄여가는 방식
        - 첫 색상이 나머지 색상과 같은지 확인 후 틀린 것이 존재 -> 틀린 구역을 다시 네 구역으로 나눔 -> 계속 반복(재귀)
    - 분할 정복
        - Divide -> Conquer -> Combine 순서
        - Divide 가 잘되어 있으면 Conquer 은 쉬움, 즉 Divide 를 잘 하는 것이 중요
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    graph = [list(map(int, input().split())) for _ in range(n)]

    ans_w, ans_b = 0, 0

    def solution(x, y, n):
        nonlocal ans_w, ans_b
        color = graph[x][y]

        # 시작 위치는 항상 속한 정사각형의 (0, 0) 위치라고 생각해도 무방함
        for i in range(x, x + n):
            for j in range(y, y + n):
                if color != graph[i][j]:
                    solution(x, y, n // 2)  # 1사분면
                    solution(x, y + n // 2, n // 2)  # 2사분면
                    solution(x + n // 2, y, n // 2)  # 3사분면
                    solution(x + n // 2, y + n // 2, n // 2)  # 4사분면
                    return

        if color == 0:
            ans_w += 1
        else:
            ans_b += 1

    solution(0, 0, n)
    print(ans_w)
    print(ans_b)


if __name__ == "__main__":
    solution()
