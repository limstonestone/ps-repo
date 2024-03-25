"""
https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""


def solution(number, k):
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 입력길이가 백 만자리이므로 O(N) 수준의 풀이를 구현해야 함
    - 고정된 길이에서 고정된 개수만큼 제거하므로 가능한 경우의 수는 모두 자리수가 같음
        - 따라서 앞자리수가 클 수록 큰 수일 것 (순서대로 순회함)
        - 주의해야할 점은 앞자리수가 가장크더라도 뒤에 남은 글자 수가 정해진 길이보다 짧으면 안됨

    - 답지 풀이
        - 숫자를 보존해나가는것에 집중하는 것이 아니라, 숫자를 제거하는 것에 집중
        - 앞 자리수가 클 수록 큰 수이므로 스택을 활용하여 과거값을 탐색
        - 최근에 스택에 들어온 값이 현재 값보다 작다면 제거하는 방식
    """
    n = len(number)
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 남은 k개의 숫자 제거 (이미 가장 큰 순서대로 들어와있으니 넘치는 만큼 제거)
    stack = stack[:-k] if k > 0 else stack

    return "".join(stack)
