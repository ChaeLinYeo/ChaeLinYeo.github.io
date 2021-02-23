---
title : "[Visual Recognition]Visual Recognition: Object Detection, Faster RCNN"
data : 2021-02-23 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
use_math: true
---
# Visual Recognition: Object Detection(1) - Fast RCNN
## Object Detection 문제정의
영상안에 있는 모든 물체(object)들과 그것들의 위치(영역)을 함께 찾는다.  
- Classification + Localization = Object Detection
- 입력: 영상, 출력: 벡터(9개)
    - 입력 영상이 뉴럴 네트워크의 여러 필터를 거치게 된다. 마지막 단에는 우리가 관심있는 클래그의 개수만큼의 Output이 나온다. (예: 보행자 / 차 / 오토바이 / 배경 일 확률에 대한 4가지의 Output)
    - 여기에 localization이 추가되어 클래스의 정보와 더불어 위치 정보가 추가되어 도출된다 (예: 물체가 있느냐 / 물체의 중심점의 x좌표 / 물체의 중심점의 y좌표 / 물체의 넓이 / 물체의 높이)
    - 결론적으로, 입력 영상 -> 9개의 원소를 갖는 벡터 출력하는 네트워크를 만드는 것이다.
        - weight의 업데이트는, 현재의 예측치와 Ground Truth의 차이가 줄어들도록 CNN을 업데이트한다. 
    - 로스함수: 현재의 예측치 - Ground Truth값의 제곱. 로스함수를 최소화하는 것이 목표.
        - 현재의 예측치는 인공신경망의 파라미터에 의존하는 함수임
- Object Detection에서는 box가 반드시 한 개인 것은 아님. 영상 1개에 대하여 벡터 1개만으로는 모든 object가 표현이 안됨. 따라서 여러 오브젝트에 대해 박스체킹이 됨.
    - 어느 위치에 오브젝트가 있는지 찾아줘야함. 오브젝트 영역의 크기도 결정해야 함. + 어떤 오브젝트인지도 알려줘야 함(분류) -> 이런 여러 문제를 동시에 풀기가 쉽지 않다. 
<br>

## Object Detection 요소기술
- Region Proposal: Object가 있을만한 영역을 다수 추천
- Non-max Suppression: 겹치는 영역을 제거
- Classification: 영역속의 Object를 분류
- Bounding Box Regression: Object 영역을 미세조정
<br>

## Faster RCNN 기본 flow
![png](/assets/images/2021-02-23/1.png)  
- 출처: https://medium.com/datadriveninvestor/review-on-fast-rcnn-202c9eadd23b
- Pre-trained 모델을 base network라고도 부른다. 처음 나왔을땐 VGGNet을 썼고, Mobilenet, ResNet등을 사용할 수 있다.
- Rol Pooling은 Region Proposal을 통해 나온 서로 다른 크기의 영역들을 같은 사이즈들로 맞춘다. (fully connected layer는 고정된 크기를 input으로 받기 때문에)
- Region proposal에서는 대충의 바운더리가 나왔다면 FC레이어 이후에는 그 오브젝트의 종류별로 클래시피케이션을 수행한다.
<br>

## Base Network
- 초기의 논문에서는 VGG Net을 썼음.
- 224*224*3 사이즈의 이미지가 들어오면 컨볼루션+pooling을 수행하여 5번의 pooling layer를 거쳐 7*7*512가 된다. 즉 feature map의 사이즈가 224/2^5 = 224/32 = 7, 7*7크기의 이미지가 된 것. 풀링 레이어의 개수는 쓰기 나름이다.
- 이 결과를 Region proposal의 네트워크에 집어넣게 된다.
<br>

## Region Proposal Architecture
- Region proposal의 네트워크는 다음과 같이 구성된다.
    - 3*3 convolution(아래와 같이 양쪽으로 나눠진다. 따라서 2개의 output이 나온다.): 512개의 output channels
        - 1*1 convolution: 2k(=36)개의 output channels
        - 1*1 convolution: 4k(=36)개의 output channels 
            - 각각의 컨볼루션은 각각의 로스를 최소화한다.
<br>

## 3*3 Convolution 후의 Output
- 224 * 224 사이즈의 이미지 -> 3 * 3 컨볼루션을 통과하여 7 * 7 사이즈의 이미지
- 7 * 7 feature map에서의 한 픽셀은 원래영상(224*224)에서 32 * 32에 해당하는 영역임. 
<br>

## 1*1 convolution
- 1 * 1 컨볼루션은 3차원 필터인데 각 픽셀의 width, height가 1이다.
- 3 * 3 컨볼루션을 통해 나오는 feature에 1 * 1 컨볼루션을 씌우면 겹치는 각 픽셀 영역에서의 필터값과 1 * 1 컨볼루션의 피쳐맵의 값이 곱해진다. 겹치는 각 픽셀마다 하나의 값이 나온다.
- 결과적으로 하나의 맵이 나온다.
<br>

## 1*1 Convolution 후의 Output
- 1*1 Convolution을 통과하면 하나의 맵이 나온다. 
- 2개의 1*1 Convolution은 각각 2k의 output channel(1k의 맵 2개)
    - 여기에서 각 맵의 위치 2개를 통해 Objectness 벡터가 나온다
    - 이 값은 해당 픽셀 위치에 오브젝트가 있을 확률을 알려준다.
- 그리고 4k의 output channel(1k의 맵 4개)이 도출된다. 
    - 여기에서 각 맵의 위치 4개를 통해 Bounding Box 벡터가 나온다
    - 이 값의 2개는 오브젝트를 감싸는 바운딩 박스의 중심점을 알려준다.
    - 이 값의 나머지 2개는 중심점을 기준으로 하여 박스의 width, height를 알려준다.
- Objectness 벡터와 Bounding Box 벡터를 합쳐 같은 위치에 해당하는 feature vector가 된다.(오브젝트가 있을 확률 + 오브젝트 박스의 중심점 + 너비와 높이의 정보를 갖고있다.)
<br>

## IoU(Intersection over Union) measure(측정도구)
IoU = 예측값과 참값의 교집합 / 예측값과 참값의 합집합  
IoU = 0.1 # Poor  
IoU = 0.6 # Good  
IoU = 0.8 # Excellent  
IoU가 1이면 가장 최댓값, 예측값과 참값이 모두 일치할 때.  
IoU가 0이면 가장 최솟값, 예측값과 참값이 아예 일치하지 않을 때.  
0과 1사이의 값을 갖고, 1에 가까울수록 좋은 성능을 가진 것이다.  
<br>

## Objectness 벡터
- 2개의 벡터: 이 영역이 오브젝트에 해당하는 영역인지 아닌지(오브젝트일 확률/오브젝트 아닐 확률)
- 4개의 벡터: 이 영역이 오브젝트에 해당하는 영역이라면 오브젝트의 바운딩 박스의 위치와 크기는 어떻게 되는지(오브젝트의 중심점의 x, y좌표, 오브젝트의 바운더리의 너비, 높이) 
<br>

