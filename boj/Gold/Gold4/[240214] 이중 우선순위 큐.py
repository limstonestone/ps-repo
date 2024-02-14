"""
https://www.acmicpc.net/problem/7662
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 우선 순위 큐 -> 힙(파이썬 heapq 라이브러리)을 이용해서 풀이할 수 있음
        - 파이썬의 최소힙은 최소값이 앞으로 정렬됨
    - 큐에 부호를 함께 삽입하여 풀이하여 예제는 맞췄지만 답은 실패

    - 답지 참조
        - 한번에 다 삽입하는 것이 아닌 최소힙, 최대힙을 따로 구현하여 동기화 작업이 필요
        - 이 때 제거를 했을 경우를 고려하기 위해 방문 배열을 생성(id 를 함께 삽입)
            - 최소힙/최대힙 둘 다 같은 숫자가 들어가는 것이므로 하나의 힙에서 제거된 경우를 고려하기 위함임
    """
    import sys
    import heapq

    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        k = int(input())
        visited = [False] * k
        max_h, min_h = [], []

        for i in range(k):
            string, num = input().split()
            num = int(num)

            if string == "I":
                heapq.heappush(max_h, (-num, i))
                heapq.heappush(min_h, (num, i))
            else:
                if num == -1:  # 최소값을 삭제해야한다면 -> 최소힙
                    if min_h:
                        # 최소값 삭제 + 최소값이 가진 인덱스 방문 처리
                        min_idx = heapq.heappop(min_h)[1]
                        visited[min_idx] = True
                elif num == 1:
                    if max_h:
                        max_idx = heapq.heappop(max_h)[1]
                        visited[max_idx] = True

            # 힙에 들어있고 방문한 원소라면 -> 반대편 힙에서 지워진 원소이므로 동기화(삭제해주기)
            while min_h and visited[min_h[0][1]]:
                heapq.heappop(min_h)
            while max_h and visited[max_h[0][1]]:
                heapq.heappop(max_h)

        if min_h:
            print(-max_h[0][0], min_h[0][0])
        else:
            print("EMPTY")


if __name__ == "__main__":
    try1()
