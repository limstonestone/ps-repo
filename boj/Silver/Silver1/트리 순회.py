"""
https://www.acmicpc.net/problem/1991
"""


def try1():
    """
    - 약 40분 소요
    - 왼쪽, 오른쪽 정보를 그래프에 입력시 순서를 보존하여 주입
    - 주석 참고
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = dict()

    for _ in range(n):
        parent, left, right = input().split()
        graph[parent] = [left, right]

    forward_ans = ""
    middle_ans = ""
    backward_ans = ""

    def forward(node):
        nonlocal forward_ans
        if node == ".":  # 더 이상 탐색불가능할 때 종료
            return

        forward_ans += node  # 루트 노드부터 저장
        forward(
            graph[node][0]
        )  # 루트 노드의 왼쪽 노드 탐색 (새로운 루트가 됨 -> 루트가 되었으므로 계속해서 정답에 추가)
        forward(
            graph[node][1]
        )  # 루트 노드의 오른쪽 노드 탐색 (마찬가지로 새로운 루트가 됨, 왼쪽 자식은 이미 다 탐색된 상태)

    def middle(node):
        nonlocal middle_ans
        if node == ".":
            return

        middle(
            graph[node][0]
        )  # 위와 마찬가지로 왼쪽 자식부터 탐색, 더이상 탐색 불가능 하면 아래 행으로 이동
        middle_ans += (
            node  # 가장 마지막의 왼쪽 자식에 도달했을 경우 다시 루트로 거슬러올라옴
        )
        middle(graph[node][1])

    def backward(node):
        nonlocal backward_ans
        if node == ".":
            return

        backward(graph[node][0])
        backward(graph[node][1])
        backward_ans += node

    forward("A")
    print(forward_ans)

    middle("A")
    print(middle_ans)

    backward("A")
    print(backward_ans)


if __name__ == "__main__":
    try1()
