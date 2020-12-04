# def solution(s):
#     answer = True
#     stack = []
#     for c in s:
#         if c == '(': # 여는 괄호이면
#             stack.append(c) # 스택에 푸시
#         elif c == ')': # 닫는 괄호이면
#             if not stack: # 스택이 비어있다면
#                 return False
#             else : # 스택이 비어 있지 않으면, 즉 스택 내부에 여는 괄호가 있으면
#                 stack.pop()
#     return not stack

def solution(s):
    answer = 0
    s = s[::-1]
    s = list(s)
    stack = [s.pop()]
    # print(s, stack)
    for word in s:
        # print(stack, word)
        if len(stack)==0:
            stack.append(word)
        elif stack[-1] != word:#스택의 탑에 있는것과 다르면 넣고
            stack.append(word)
        else:#같으면 뺀다
            stack.pop()
    # print(stack)
    if not stack:
        answer = 1
    else:
        answer = 0
    return answer
# print(solution("baabaa"))
print(solution("cdcd"))