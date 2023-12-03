"""
https://blex.me/@mildsalmon/chap-3-그리디-숫자-카드-게임
"""


### 1st trial (time : 4m)
def try1():
    """
    - 배열 내 최소값을 찾은 후, 이전 최소값과 비교하여 더 큰값을 저장-> 구현 or 그리디
    - 18~19번째 줄 코드를 min_val = max(min_val, tmp_min_val) 로 바꿔도 좋을 듯함
    """
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_val = 0

    for i in range(n):
        tmp_min_val = min(arr[i])
        if min_val < tmp_min_val:
            min_val = tmp_min_val

    print(min_val)


if __name__ == "__main__":
    try1()
