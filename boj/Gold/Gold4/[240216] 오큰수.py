"""
https://www.acmicpc.net/problem/17298
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 입력의 크기가 100만 가량 -> O(N) 수준으로 풀이해야 함
    - 스택을 활용해서 시간여행 가능

    - 답지 풀이
        - 굳이 뒤부터 출발할 필요없이 순차적으로 진행하되, 인덱스를 스택에 저장해두면 선입후출이 되므로 반복문을 통한 지속적인 pop 연산을 통해 시간을 거슬러 채워넣을 수 있음
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    nums = list(map(int, input().split()))
    stack = [0]
    answer = [-1 for _ in range(n)]

    for i in range(1, n):
        while stack and (nums[stack[-1]] < nums[i]):
            answer[stack.pop()] = nums[i]
        stack.append(i)

    print(*answer)


if __name__ == "__main__":
    try1()
