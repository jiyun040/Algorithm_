def solution(video_len, pos, op_start, op_end, commands):
    # 시간을 mm:ss 형식에서 초로 변환하는 함수
    def time_to_seconds(time_str):
        mm, ss = map(int, time_str.split(":"))
        return mm * 60 + ss
    
    # 초를 mm:ss 형식으로 변환하는 함수
    def seconds_to_time(seconds):
        mm = seconds // 60
        ss = seconds % 60
        return f"{mm:02}:{ss:02}"

    # 입력을 초 단위로 변환
    video_len_sec = time_to_seconds(video_len)
    pos_sec = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)

    # 오프닝 구간 처리 함수
    def skip_op(pos_sec):
        if op_start_sec <= pos_sec <= op_end_sec:
            return op_end_sec
        return pos_sec

    # 초기 위치에서 오프닝 구간을 건너뛰기
    pos_sec = skip_op(pos_sec)

    # 명령어 처리
    for command in commands:
        if command == "prev":
            pos_sec = max(0, pos_sec - 10)
        elif command == "next":
            pos_sec = min(video_len_sec, pos_sec + 10)
        
        # 명령어 처리 후 오프닝 구간을 건너뛰는 로직
        pos_sec = skip_op(pos_sec)

    # 결과 반환
    return seconds_to_time(pos_sec)