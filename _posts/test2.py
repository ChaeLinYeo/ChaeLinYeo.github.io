def solution(s):
    stack = []
    for elem in s:
        while stack and stack[-1] < elem:
            stack.pop()
        stack.append(elem)
        # print(stack)
    return "".join(stack)

print(solution("xyb"))
