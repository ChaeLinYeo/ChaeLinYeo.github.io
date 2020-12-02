def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : (x*4)[:4], reverse = True)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer

# def solution(numbers):
#     numbers = [str(x) for x in numbers] # 문자열로 변환. O(n)복잡도를 가진다.
#     numbers.sort(key=lambda x : (x*4)[:4], reverse = True) # x라는 원소가 주어지면 4번 반복하고 앞에서 4개까지를 슬라이스해서 딱 4개에 맞게 떨어지도록 만든다. 그리고 내림차순으로 정렬한다. O(nlogn)복잡도를 가진다.
#     print(numbers)
#     if numbers[0] == '0':
#         answer = '0'
#         # 만약 0만 두개 이상 들어있는 배열이 주어진다면, 00, 0000 이런게 나오게 될텐데, 그럴때는 0 한글자로 이루어진 문자열을 리턴하게 해야한다.
#     else:
#         answer = ''.join(numbers)
#     # if에 의한 수행은 O(n)
#     return answer

print(solution([6, 00, 2]))
# print(solution([3, 30, 34, 5, 9])) # 9534330