---
title : "[Leetcode]85 - Maximul Rectangle"
data : 2021-04-26 00:15:28 -0400
categories : 코테
use_math: true
---
## 85 - Maximul Rectangle
### 문제 설명
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.  
<br>

### 제한사항
- rows == matrix.length
- cols == matrix[i].length
- 0 <= row, cols <= 200
- matrix[i][j] is '0' or '1'.
<br>

### 입출력 예
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  
Output: 6  

<br>

### 풀이
1. 첫 시도: 문제를 대충 훑어봤을 땐 프로그래머스 level03의 floodfill 영역구하기와비슷하다고 생각, bfs -> rectangle모양을 지켜야 하므로 실패
2. 두번째 시도: 매트릭스의 한 줄씩을 리스트에 담아0이 나와 끊기지 않으면 계속 더한 후여러 조건의 if문을 생성해 높이는 비교하는 앞 뒤 열 중 큰 값, 너비는 1씩 증가한 뒤 마지막에 곱하는 방식으로 그중 가장 최댓값 구하기 -> 테스트케이스 부분 통과 
3. 세번째 시도: 매트릭스의 한줄씩을 리스트에 담아0이 나와 끊기지 않으면 계속 더한 후 스택을 사용해 인덱스 값을 넣고 높이와 너비 구하기 -> 성공


![png](/assets/images/codingtest/maximalrectangle.png)  

```python
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        size = 0
        w=1
        h=1
        if not matrix or not matrix[0] : # []인 경우와 [[]]인 경우
            return 0
        line = [0]*(len(matrix[0])+1) # 매트릭스의 한줄씩 담는다
        for row in matrix:
            for i in range(len(row)): # 열이 1이면 +1하고, 0이면 이전 덧셈을 날리고 0으로 초기화
                if row[i]=='1':
                    line[i]+=1
                else:
                    line[i]=0
            print(line)
            stack=[0] # 첫번째 인덱스부터 시작
            for i in range(len(row)+1): # 맨 끝자리까지의 비교를 위해 +1
                while stack and line[i] < line[stack[-1]]:# 스택이 비워져있지 않으면서, 앞의 열보다 뒤의 열의 값이 작을때
                    h=line[stack.pop()] # 높이는 스택의 마지막(즉 stack[-1])이 최대 길이
                    if stack:
                        w=i-stack[-1]-1 # 너비
                    else:
                        w=i
                    size=max(size,h*w) # 넓이 자동으로 최댓값 저장
                    print(stack)
                stack.append(i) # 다음 인덱스 추가하여 계속 비교...
        return size
 

matri x = [["0","0","0"],["0","0","0"],["1","1","1"]]
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] # 6
# matrix = [] # 0
# matrix = [["0"]] # 0
# matrix = [["1"]] # 1
# matrix = [["0","0"]] # 0
# matrix = [["1","1"]] # 2
ob = Solution()
print(ob.maximalRectangle(matrix))

```