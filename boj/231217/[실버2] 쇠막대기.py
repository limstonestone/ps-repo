"""
https://www.acmicpc.net/problem/10799
"""


def try1():
    """
    - 약 40분 풀이 후 실패
    - n 이 10만 -> O(NlogN)
    - 직접 풀어쓰는 답을 구하는 원리
        - ( X X ) 가 주어졌을 때 ( ) 를 없애고, 점은 그대로 둠
        - 이 때 ( ) 안의 X 개수 + 1 을 더 해줌 -> ( X ) 의 경우 2개로 쪼개짐, ( X X ) 의 경우 3개로 쪼개짐
        - 이 과정을 막대기가 없어질 때 까지 반복
        - 하지만 구현 실패 ㅠㅠ

    - 답지 참조
        - ( 를 마주친 순간 스택에 push, ) 를 만나는 순간 pop
        - 그 과정에서 괄호가 레이저면 안에 있는 쪼개진 개수를 더해 줌(스택의 개수)
    """
    batch = input()
    stack = []
    ans = 0
    for i in range(len(batch)):
        if batch[i] == "(":
            stack.append("(")
        else:
            if batch[i - 1] == "(":  # "()" 인 경우 -> result += 0
                stack.pop()  # 직전의 ( 제거
                ans += len(stack)  # 첫 번째 경우인 현재의 쇠막대기들을 카운팅합니다.

            else:  # "))" 인 경우 -> 파이프 꼬다리가 남으므로 +1
                stack.pop()  # "(" 제거
                ans += 1  # 이 부분은 두 번째 경우인 나머지 부분을 세는 것입니다.
    print(ans)


if __name__ == "__main__":
    try1()
