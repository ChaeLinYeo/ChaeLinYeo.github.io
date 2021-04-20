---
title : "[프로그래머스 코딩테스트]Level03 - N-Queen"
data : 2021-04-17 00:15:28 -0400
categories : 프로그래머스코테
use_math: true
---
## Level 03 - N-Queen
### 문제 설명
가로, 세로 길이가 n인 정사각형으로된 체스판이 있습니다. 체스판 위의 n개의 퀸이 서로를 공격할 수 없도록 배치하고 싶습니다.

예를 들어서 n이 4인경우 다음과 같이 퀸을 배치하면 n개의 퀸은 서로를 한번에 공격 할 수 없습니다.
체스판의 가로 세로의 세로의 길이 n이 매개변수로 주어질 때, n개의 퀸이 조건에 만족 하도록 배치할 수 있는 방법의 수를 return하는 solution함수를 완성해주세요.

<br>

### 제한사항
- 퀸(Queen)은 가로, 세로, 대각선으로 이동할 수 있습니다.
- n은 12이하의 자연수 입니다.
<br>

### 입출력 예
|---|---|
|n|result|
|4|2|

<br>

### 풀이
한 행에는 한 개의 queen 밖에 위치할 수 없다는 것을 이용하여
모든 행에 퀸이 위치하는 것이 가능할 때 answer을 1증가 시켜준다.
같은 열에 퀸이 위치해있거나 대각선에 위치한 퀸이 이미 있다면 다음열에 위치시켜본다. 
가능한 경우 행을 증가시킨후 재귀함수를 호출하고 모두 불가능한경우 위치시킨 퀸을 제거하고 
다음 열에 위치시킨다 (백 트래킹)

- 같은 열 체크
    - queen[i]: i번째 행에서 퀸이 놓여있는 열의 위치
    - queen[j]: j번째 행에서 퀸이 놓여있는 열의 위치
    - queen[i] == queen[k]: 같은 열에 놓이므로 안됨

- 대각선 체크
    - 왼쪽에서 위협하는 퀸에 대해 열에서의 차이와 행에서의 차이가 같다.
        - queen[i]-queen[j] == i-j
    - 오른쪽에서 위협하는 퀸에 대해서 열에서의 차이와 행에서의 차이의 마이너스가 같다.
        - queen[i]-queen[j] == j-i
    - 즉 queen[i]와 queen[k]의 절댓값으로 대각선 위협 판단

```python
def is_promiss(queen, row):
    for i in range(row):
        if queen[i]==queen[row] or abs(queen[i]-queen[row])==abs(i-row):
            return False
    return True

def n_queens(queen, row):
    n = len(queen) # 하나의 퀸이 존재할 수 있는 한 행의 길이
    cnt = 0
    if n==row:return 1 # 끝에 도달하면 1을 리턴, n_queens함수가 cnt를 리턴할때 더해짐
    for col in range(n):
        queen[row] = col # 현재 퀸을 둔 위치 체크
        if is_promiss(queen, row): # 퀸을 둘 수 있는 자리인지
            cnt += n_queens(queen, row+1) # 백트레킹
    return cnt



def solution(n):
    queen = [0]*n # 하나의 퀸이 존재할 수 있는 한 행
    return n_queens(queen, 0)

print(solution(4)) #2
```