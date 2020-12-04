def solution(s):
    match = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for c in s:
        if c in '({[': # 여는 괄호이면 push
            stack.append(c)
            # pop을 쓰면 AttributeError: 'list' object has no attribute 'push' 발생
        elif c in ')}]': # 닫는 괄호일 때
            if not stack: # 스택이 비어있으면
                return False
            else: # 스택이 비어 있지 않으면, 즉 스택 내부에 여는 괄호가 있으면
                t = stack.pop()
                if t != match[c]:
                    return False
                # stack.pop()
    return not stack
print(solution("[)"))