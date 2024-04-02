def solution(keymap, targets):
    """
    - 약 12분 소요
    - 입력 길이 굉장히 작음 -> 시간복잡도 신경 X
    """
    answer = []

    for target in targets:  # 각 타겟 입력받음
        tmp_cnt = 0  # 한 타겟에 대한 정답
        for x in target:  # 한 타겟에서 문자 각각 확인
            idx = 1e9
            for key in keymap:  # 가능한 키맵을 모두 탐색
                if x in key:  # 키맵에 문자가 존재한다면 해당 위치(idx+1) 반환
                    idx = min(idx, key.index(x) + 1)  # 이때, 최소값으로 이루어져야함

            if idx == 1e9:  # 만약 모든 키맵에 문자가 존재하지 않으면 idx 는 초기상태
                tmp_cnt = (
                    -1
                )  # 따라서 -1을 출력하고, 뒤의 알파벳은 더 탐색할 필요가 없음
                break  # for x in target 을 종료, 즉 뒤의 문자를 안봐도 정답은 -1

            tmp_cnt += idx  # 임시 정답(한 알파벳에 대한)에 가장 작게 누르는 자판값 반환

        answer.append(tmp_cnt)  # 아까 저장해놓은 타겟에 대한 최소값 정답 배열에 추가

    return answer
