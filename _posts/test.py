def solution(n, lost, reserve):
    answer = 0
    u = [1]*(n+2) # 학생의 유니폼 소지 여부 모두 1으로 초기화
    for r in reserve: # 여벌 갖고 있는사람 +1
        u[r]+=1
    for l in lost: # 도난당한 사람 -1
        u[l]-=1
    for i in range(len(u)): #  여분이 있는 사람은 자기보다 번호가 작은 사람에게 한벌을 빌려줌
        if u[i]==0 and u[i+1]==2:
            u[i]+=1
            u[i+1]-=1
    for i in range(len(u)):#  여분이 있는 사람은 자기보다 번호가 큰 사람에게 한벌을 빌려줌
        if u[i]==2 and u[i+1]==0:
            u[i]-=1
            u[i+1]+=1
    # print(u)
    for j in range(len(u)):
        if u[j]!=0:
            answer +=1
    return answer-2

print(solution(5, [2,4], [1,3,5]))#5