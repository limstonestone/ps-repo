"""
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""


def solution(numbers, target):
    """
    - 약 46분 (힌트 참조)
    - 트리 형태로 생각해보면 DFS 로 풀이할 수 있음을 알 수 있음
        -      4
        -  -1,    1
        - -2,2, -2,2
        -     ...
        - -4인 경우도 마찬가지로 적용 (즉 dfs 2번 돌리기)
        - 일반적으로 주어지는 그래프의 DFS 문제와는 조금 달라서 고민하다가 힌트를 참조함
    - 주어진 입력 변수의 범위가 충분히 작으므로, 다른 방법으로도 풀 수 있음 (product 활용)
    """
    ans = 0

    def dfs(depth, result, graph):
        nonlocal ans

        if depth == len(numbers):
            if result == target:
                ans += 1
            return ans

        dfs(depth + 1, result + numbers[depth], graph)
        dfs(depth + 1, result - numbers[depth], graph)

        return ans

    ans = dfs(0, 0, numbers)
    return ans
