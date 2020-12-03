# heap.heapify(L) # 리스트 L로부터 min heap 구성
# m = heapq.heappop(L) # min heap L에서 최소값 삭제(반환)그리고 다시 힙의 구조를 유지한다.
# heapq.heappush(L, x) # min heap L에 원소 x 삽입 그리고 다시 힙의 구조를 유지한다.
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)# 힙을 만든다.
    
    while scoville[0] < K:# 배열의 모든 요소가 스코빌 기준치 이상일때까지 돌린다
        if len(scoville)==2:# 음식을 다 섞었는데도 스코빌 기준치를 못넘으면
            if heapq.heappop(scoville)+(heapq.heappop(scoville)*2) < K:
                return -1
            else:
                return answer-1
        elif len(scoville)==0:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
        answer += 1
    # print(scoville)

    return answer
print(solution([1, 2, 3, 9, 10, 12], 7))