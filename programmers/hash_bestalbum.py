# 베스트 앨범 - 해시
def solution(genres, plays):
    answer = []
    # 제일 잘 팔린 장르 2개를 구한다
    albums = dict()
    for g, p in zip(genres, plays):
        if g not in albums:
            albums[g] = p
        else:
            albums[g] += p
    genre_rank = sorted(albums.items(), key=lambda x: x[1], reverse=True)

    # 이름순, 판매순, 고유번호 순으로 정렬한다
    arr = sorted(list(zip(genres, plays, range(len(genres)))), key=lambda x: (x[0], -x[1], x[2]))

    for i in range(len(genre_rank)):
        cnt = 0
        for genre, play, idx in arr:
            if cnt == 2:
                break
            if genre == genre_rank[i][0]:
                cnt += 1
                answer.append(idx)

    return answer