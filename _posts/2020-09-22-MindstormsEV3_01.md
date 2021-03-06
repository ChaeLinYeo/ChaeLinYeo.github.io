---
title : "[Mindstorms EV3]LineTrace 로봇 프로그래밍:U자형 커브"
data : 2020-09-22 00:15:28 -0400
categories : MindstormsEV3
---
## Goal
1. Follow the straight line
2. Follow the S-shaped (curved) line
3. Stop at the GREEN block for 3 seconds
4. Stop/Finish at the RED block
5. Vehicle must make ‘beep’ sound both at the beginning and the end
<br>
<br>

## 맵과 로봇 사진
![Alt Text](/assets/images/MindstormsEV3/map.png)
![Alt Text](/assets/images/MindstormsEV3/robot.png)
<br>
<br>

## 하드웨어
- Mindstorms EV3 메뉴얼의 기본 로봇 구조
- 컬러 감지 센서 한개
- 모터 두개
- 바퀴 두개
<br>
<br>

## 소프트웨어
```python
import ev3dev.ev3 as ev3
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

#sensor
cs = ev3.ColorSensor()
#so = Sound()
#so.beep()
speed = 100
rm = ev3.LargeMotor('outC')
lm = ev3.LargeMotor('outB')
greenflag=0

while(True):
    try:
        cs = ev3.ColorSensor()
        if(cs.color == 1):    #if color is black
            rm.run_to_rel_pos(position_sp=1080, speed_sp=speed)
            lm.run_to_rel_pos(position_sp=1080, speed_sp=speed)
        elif(cs.color == 3 and greenflag==0):    #if color is green
            #sleep(3)
            print("it is green")
            greenflag = 1
            rm.stop()
            lm.stop()
            sleep(3)
            rm.run_to_rel_pos(position_sp=1080, speed_sp=speed)
            lm.run_to_rel_pos(position_sp=1080, speed_sp=speed)
        elif(cs.color == 5):    #if color is red
            rm.stop()
            lm.stop()
            so = Sound()
            so.beep()
            break
        elif(cs.color == 6):   #if color is white
            rm.run_to_rel_pos(position_sp=1080, speed_sp=speed)
            lm.run_to_rel_pos(position_sp=1080, speed_sp=speed+375)
    except:
        #print(e)
        rm.stop()
        lm.stop()
        break
```
<br>
<br>

## 알고리즘
- 센서가 검은색을 감지하면
    - 두 모터의 속도를 동일하게 하여 직진한다.

- 센서가 초록색을 감지하고 greenflag가 0이면
    - greenflag를 1로 바꿔서 초록색이 한번만 인지되게 한다.
    - 3초동안 sleep하여 모터를 멈춘다. 
    - 3초 이후 다시 두 모터의 속도를 동일하게 하여 직진한다.

- 센서가 하얀색을 감지하면
    - 왼쪽 모터의 스피드를 올려 로봇이 커브를 크게 오른쪽으로 돌게 한다.

- 센서가 빨간색을 감지하면
    - 부저가 울리고 두 모터를 정지시킨다.
<br>
<br>

## 실험적인 결과로 얻은 적절한 모터값


|Situation|Left Motor|Right Motor|
|---|---|---|
|Initial value|100|100|
|White color detected|475|100|
|Black color detected|100|100|
|Green color detected|0|0|
|Red color detected|0|0|

<br>
<br>

## 겪었던 문제점
1.  컬러 센서가 색을 잘 감지하지 못한다.
    - 이를 해결하기 위해 컬러 센서가 지면과 가까워지도록 레고를 조립했다.
2. 첫번째 문제를 해결하자 발생한 문제이다. 센서가 초록색을 계속 인식해서 계속 sleep(3)을 유발한다.
    - 이 문제는 플래그를 사용하여 초록색을 한번만 인지하도록 했다. 플래그가 0일 때만 sleep(3)을 하며, 이후 플래그를 1로 바꿔 다시 초록색이 인지 되어도 모터를 움직일 수 있도록 한다.
3. 커브가 심한 곳에서 모터가 잘 움직이지 않는다.
    - 실험적으로 두 모터의 속도 차이를 크게 벌리는 적절한 값을 찾아 해결했다. 기본 속도 100에 커브에서 375를 더해주면 깔끔하게 움직인다.
