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

<br>
<br>

## 겪었던 문제점
1. 컬러 센서가 불규칙하게 흔들리면서 이동한다.
    - 컬러 센서에 긴 다리를 부착하여 해결
2. 컬러 센서가 1.7cm씩 간격을 따라 이동하지 않는다.
    - 속도에 따른 컬러 센서 이동 거리를 측정하여 count를 매긴다.
    - 1.7cm의 범위 내의 일정 count가 되면 한번씩 인식된 컬러를 배열에 기록한다.
3. 부속품이 많아 모터의 움직임이 둔화된다.
    - 모터 체인을 추가해 헐렁하게 하고, 대신 컬러 센서의 바닥 지지대를 설치함. 움직임이 훨씬 부드러워지고 덜 끊김.