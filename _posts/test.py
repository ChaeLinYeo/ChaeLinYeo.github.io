def solution(numbers):
    answer = ''
    d = {} # 원래의 숫자가 키, 변형된 숫자가 값으로 들어갈 사전
    origin = list(map(str, numbers)) # 원래의 수를 담아둘 오리진 배열
    numbers = list(map(str, numbers)) # numbers의 숫자를 문자열로 바꿈
    for i in range(len(numbers)):
        numbers[i]=numbers[i]*3
        numbers[i]=numbers[i][:4]
        d[origin[i]] = numbers[i]
    print(numbers)

    d = sorted(d.items(), reverse=True, key=lambda item:item[1]) # 딕셔너리의 값을 기준으로 내림차순 정렬
    print(d)
    for i in range(len(d)):
        answer += d[i][0]

    return answer

# print(solution([6, 00, 2]))
print(solution([3, 30, 34, 5, 9])) # 9534330