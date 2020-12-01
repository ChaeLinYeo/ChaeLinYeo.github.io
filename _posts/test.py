def solution(numbers):
    answer = ''
    num1 = []
    diction = {}
    for i in range(len(numbers)):
        num1.append(str(numbers[i]))
    print(num1)
    for j in range(len(numbers)):
        diction[int(num1[j][0])] = int(num1[j][1])
    print(diction)

    return answer

print(solution([6, 10, 2]))