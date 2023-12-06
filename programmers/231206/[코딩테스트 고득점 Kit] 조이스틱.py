"""
https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""


def solution(name):
    """
    - 약 1시간 풀이 후 실패
    - n 이 최대 20 -> O(N^3) 까지도 가능
    - 다음 알파벳과 이전 알파벳 중 변환 횟수가 가장 적은 것을 선택해야함 -> 그리디
    - 25번 가면 Z로감
    - 13번인 N 을 기준으로 왼쪽, 오른쪽이 동일해짐
    - 만약 A가 포함되어 있다면 A 를 건너띄는 것이 좋음 (예제에서 마지막으로 커서를 이동해서 A를 생략)
        - 하지만 이 로직이 굉장히 복잡함 (케이스가 굉장히 많음)

    - 풀이 실패로 답지 참조
        - 연속되는 A 중 길이가 긴 수열을 마주쳤을 떄, 다시 되돌아가 맨 오른쪽으로 가는게 나을지, 애초에 오른쪽부터 시작하는게 나을지 판단
        - 또한 상하, 좌우 이동을 따로 생각하는 것이 편함
        - 이런 경우는? (BAABAAAB)
            - 오른쪽이 더 길지만 오른쪽부터 시작하는게 더 좋음
            - 맨 마지막에 있는 값이 A 가 아닌 경우임
        - 2 * i + len(name) - next 의 의미
            - 오른쪽으로 갔다가 A 마주침 (i) -> 왼쪽으로 다시 이동 (i) -> 맨 오른쪽으로 이동후 남은 길이 더해줌 (len(name) - next)
        - i + 2 * (len(name) - next)] 의 의미
            - 오른쪽부터 시작 했다가 A 마주침 (len(name) - next)] -> 다시 되돌아가 맨 왼쪽으로 시작 (len(name) - next)] -> 남은 길이 더해줌 (i)
        - for 문에서 A 를 마주치는 순간마다 돌아갈지, 애초에 반대쪽부터 시작할지 판단을 하는 것

    """
    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer
