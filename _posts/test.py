# def solution(v):
#     answer = [-1,-1]

#     if v[0][0] == v[1][0]: answer[0] = v[2][0]
#     if v[0][0] == v[2][0]: answer[0] = v[1][0]
#     if v[1][0] == v[2][0]: answer[0] = v[0][0]
    
#     if v[0][1] == v[1][1]: answer[1] = v[2][1]
#     if v[0][1] == v[2][1]: answer[1] = v[1][1]
#     if v[1][1] == v[2][1]: answer[1] = v[0][1]
#     return answer

# print(solution([[1, 4], [3, 4], [3, 10]]))

# import operator
# def solution(max_weight, specs, names):
#     d = dict(specs)
#     answer = 1
#     weight = 0
#     # for i in range(len(specs)):
#     #     specs[i][1] = int(specs[i][1])
#     # sd = dict(specs)
#     # # print(sd)
#     # # d = sorted(sd.items(), key=operator.itemgetter(0))
#     # d = sorted(sd.items(), key = lambda item: item[1])
#     # # print(d)
#     # d = dict(d)
#     # # print(d)
#     for name in names:
#         weight += int(d.get(name))
#         if weight > max_weight:
#             answer += 1
#             weight += int(d.get(name))
#     return answer

# print(solution(200, [["toy", "50"], ["snack", "180"]], ["toy", "snack", "toy"]))


