---
title : "[Mindstorms EV3]Maze Runner 로봇 프로그래밍"
data : 2020-10-11 00:15:28 -0400
categories : MindstormsEV3
---
## Goal
Design both HW and SW to find the shortest route on a given map
<br>
<br>

## Requirements
1. Scan/read the map
2. Algorithm (find the route)
3. Move along the path
4. Competition: Shortest path
Machine must make a ‘beep’ sound both at the beginning and end
-> we measure the run time according to the beep sound 
<br>
<br>

## 맵과 로봇 사진
![Alt Text](/assets/images/MindstormsEV3/mazerunner_map.png)
![Alt Text](/assets/images/MindstormsEV3/robot_s.jpeg)
<br>
<br>

## 소프트웨어
```python

```
<br>
<br>

## 알고리즘
- 시작할때 부저를 한번 울린다.

- 컬러센서의 값이 1이면(검은색 감지)
    - 왼쪽 모터의 스피드를 올리고 오른쪽 모터의 스피드를 내려 로봇이 오른쪽으로 돌게 한다.
    - 방향 flag를 True로 바꾼다.

- greenflag가 0이고 컬러센서의 값이 3이면(초록색 감지)
    - 좀더 정교하게 초록색임을 감지할 필요가 있어 RGB값으로 한번 더 초록색의 범위를 판별한다.
    - 초록색이라면 greenflag를 1로 바꿔서 초록색이 한번만 인지되게 한다.
    - 3초동안 sleep하여 모터를 멈춘다. 
    - 3초 이후 sleep하기 전의 모터의 방향 flag가 True라면 우회전을 했던 것이므로 오른쪽 모터의 속도를 올리고 왼쪽 모터의 속도를 내려 좌회전을 해준다.
    - 3초 이후 sleep하기 전의 모터의 방향 flag가 False라면 좌회전을 햇던 것이므로 왼쪽 모터의 속도를 올리고 오른쪽 모터의 속도를 내려 우회전을 해준다.
        - 이때, flag를 인식 후 모터의 방향을 바꾸는 것은 컬러센서가 검은색을 다시 감지할 때까지이다.

- 컬러센서의 값이 5이면(빨간색 감지)
    - 부저를 울리고 두 모터를 정지시킨다.
    
- 컬러센서의 값이 검은색, 초록색, 빨간색이 아니라면(하얀색일 때):
    - 오른쪽 모터의 스피드를 올리고 왼쪽 모터의 스피드를 내려 로봇이 커브를 왼쪽으로 돌게 한다.
    - 방향 flag를 False로 바꾼다.
<br>
<br>

## 실험적인 결과로 얻은 적절한 모터값


|Situation|Left Motor|Right Motor|
|---|---|---|
|Initial value|190|190|
|White color detected(좌회전)|-10|400|
|Black color detected(우회전)|400|-10|
|Green color detected|0|0|
|Red color detected|0|0|

<br>
<br>

## 겪었던 문제점
1.  컬러 센서가 초록색을 잘 감지하지 못한다.
    - 특히 초록색을 감지하지 못하는 문제를 해결하기 위해 color mode가 아닌 RGB의 값으로 초록색을 좀더 정밀하게 감지하는 임계값을 실험적으로 얻어냈다.
2. 초록색 인식 후 3초 쉰 후에 모터가 엉뚱한 방향으로 돌아간다.
    - 방향 flag를 지정하여 우회전할때 True, 좌회전할때 False로 바꾸면서 초록색이 인식되었을때 이 값에 따라 3초 뒤의 모터 방향을 결정하게 했다.
    - 이마저도 잘 듣지 않을 경우가 생겨 센서가 다시 검정색을 인식할 때까지 결정된 모터 방향대로 움직이게 했다. 이 작없을 flag가 False일때 하도록 했는데, True일때도 문제가 생기면 동일한 while문을 만들어주면 된다.
3. 커브의 굴곡에 따라 로봇이 경로를 이탈한다.
    - 검은색일때 좌회전, 하얀색일때 우회전을 하던 것을 검은색일때 우회전, 하얀색일때 좌회전을 하도록 바꿨다.
    - 초기 속도를 100에서 190으로 높이고, 증감도 실험적으로 +210, -200으로 하여 즉각적으로 모터 방향을 움직일 수 있게 했다.