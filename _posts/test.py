## 프로그래머스 코테
# def solution(n, words):
#     answer = [0, 0]
#     cnt = 0
#     for i in range(len(words)):
#         # print(i, words[i], words[i][-1])
#         if words[i] in words[:i]:#중복
#             cnt = cnt % n
#             answer = [cnt+1, (i)//n + 1]
#             break
#         elif (i != 0 and words[i-1][-1] != words[i][0] ):#잘못함
#             # print(words[i+1])
#             cnt %= n
#             answer = [cnt+1, (i)//n +1]
#             break
#         else:
#             answer = [0,0]
#         cnt+=1
#     return answer
# # print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# import itertools
# def solution(arr):
#     dp_max = [[0 for x in range(200)] for y in range(200)]
#     dp_min = [[0 for x in range(200)] for y in range(200)]
#     # memset(dp_max, -1000000, 40000);
#     # memset(dp_min, 1000000, 40000);
#     dp_max[:] = itertools.repeat(-1000000, 40000)
#     dp_min[:] = itertools.repeat(1000000, 40000)
#     answer = 1
#     num = len(arr)//2+1
#     # print(num)
#     for i in range(num):
#         # print(int(arr[i*2]))
#         dp_max[i][i] = int(arr[i*2])
#         dp_min[i][i] = int(arr[i*2])
#     for c in range(num):
#         for i in range(num-c):
#             j = c+i
#             for k in range(j):
#                 if (arr[k * 2 + 1] == "-"):
#                     dp_max[i][j] = max(dp_max[i][k] - dp_min[k + 1][j], dp_max[i][j])
#                     dp_min[i][j] = min(dp_min[i][k] - dp_max[k + 1][j], dp_min[i][j])
#                 elif (arr[k * 2 + 1] == "+"):
#                     dp_max[i][j] = max(dp_max[i][k] + dp_max[k + 1][j], dp_max[i][j])
#                     dp_min[i][j] = min(dp_min[i][k] + dp_min[k + 1][j], dp_min[i][j])
#     answer = dp_max[0][num-1]
#     return answer
# print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))



from itertools import permutations
def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i%2==0:
            arr[i] = int(arr[i])

    num = len(arr)//2
    idx = []
    for i in range(num):
        idx.append(2*i+1)

    calclist = list(permutations(idx)) #순열
    for calc in calclist:
        temp = arr[:]
        j = 0
        while j < len(calc):
            idx = calc[j]
            a = temp[idx-1]
            b = temp[idx+1]
            operation = temp[idx]
            if operation == "-":
                temp = temp[:idx-1]+[a-b]+temp[idx+2:]
            else :
                temp = temp[:idx-1]+[a+b]+temp[idx+2:]
            # calc = [e-2 if e > idx else e for e in calc]
            for e in calc:
                # print(e)
                if e > idx:
                    calc[calc.index(e)] = e-2
                else:
                    calc[calc.index(e)]  = e

            print(calc)
            # calc = list(calc)
            j+= 1
        answer.append(temp[0])

    # print(answer)
    return max(answer)


arr =["1", "-", "3", "+", "5", "-", "8"]
result=solution(arr)
print(result)