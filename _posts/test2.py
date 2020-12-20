from itertools import product

def solution(monster, S1, S2, S3):
    meet = 0
    total = 0
    S1_list = [i for i in range(1, S1+1)]
    S2_list = [i for i in range(1, S2+1)]
    S3_list = [i for i in range(1, S3+1)]
    for i in product(S1_list, S2_list, S3_list):
        # print(i, end=" ")
        total += 1
        if sum(i)+1 in monster:
            meet += 1
            # print(i)
    # print(meet, total)
    answer = int((1 - (meet/total))*1000)
    return answer

print(solution([4,9,5,8],2,3,4))#500