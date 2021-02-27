---
title : "[Visual Recognition]GAN, Style Transfer"
data : 2021-02-26 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
use_math: true
---
# Visual Recognition: Generative Models
## Probability Density function
확률분포함수. PDF. 각 샘플에 대해 나오는 결과들의 분포.  
확률변수 X가 취하는 값이 실수 구간 또는 실수 구간의 합으로 주어질 때, 연속확률변수라고 한다. 예를 들어, 임의로 선택한 사람의 키나 어느 지역의 연간 강수량과 같은 측정치는 연속확률변수이다. 연속확률변수의 확률분포는 한 점에서의 확률이 아니라 어느 구간에 속할 확률로 정의하는데, 한 점에서의 상대적 가능성을 나타내는 확률밀도함수를 이용하여 정의한다.  
<br>

가정: 영상이 2차원 벡터이고, 다음과 같은 PDF를 가진다고 가정. 예를 들어 다음과 같이
- (3,2): 얼굴일 확률이 0.9
- (4,1): 얼굴일 확률이 0.01
실제 영상은 n차원 벡터 -> n개의 축을 가진 PDF로부터 생성된 샘플이라고 볼 수 있다.  
영상을 만들어내는 PDF를 알고 있으면 영상을 생성할 수 있음. PDF의 값이 큰 샘플을 생성하면 됨. -> 문제는, 이 PDF를 구하는 것이 불가능함.  
그래서 나온 것이 GAN!  
<br>
<br>

## GAN
Generative Adversarial Network(적대적으로 생성하는 네트워크)  
PDF를 구하려는 시도가 아닌 다른 시도를 해보자는 것에서 나온 GAN!  
초기의 GAN은 Generator(생성자)와 Discriminator(판별자)로 이루어졌다. 이 둘이 서로 경쟁하면서 성능을 올리는 방식이었다.  
- Generator: 정교하게 위조화폐를 생성한다.
- Discriminator: 위조화폐인지 아닌지 판별한다.
- 노이즈 -> Generator -> 가짜 생성 -> Discriminator에게 진짜를 줌 -> 가짜 or 진짜 판별 후 Generator에게 피드백
GAN에서는 Generator가 어떤 내용을 만들어내느냐가 진짜 데이터에 따라 달라진다. 고양이는 워낙 포즈가 다양해서 진짜같은 고양이를 만들어내기가 사람에 비해 어렵다.  
GAN은 노이즈로부터 어떠한 새로운 내용을 만들어내는 함수와 같다.  
<br>
<br>

## 분포 매핑함수로서의 GAN
GAN은 노이즈로부터 어떠한 새로운 내용을 만들어내는 함수와 같다. 가우시안 노이즈가 인풋으로 주어지면 (가우시안 분포로부터 생성한 노이즈) generative network를 통과해서 사람 얼굴을 만들어서 출력해준다.  
<br>
<br>

## Discriminator의 역할
진짜 얼굴 사진이 들어오면 큰값(1), 가짜 얼굴 사진이 들어오면 작은값(0)을 내보내는 함수 역할을 한다.  
Discriminator은 큰값이 나온것을 만들어내고, 작은값이 나온것은 만들지 말라고 Generator에게 피드백을 한다.  
Generator는 이 피드백으로 업데이트를 한다.  
<br>
<br>

## Discriminator Network
초기의 Discriminator의 네트워크는 입력으로 이미지가 들어가면 4개의 컨볼루션을 지난다. 각 컨볼루션마다 파라미터들이 나온다. 컨볼루션을 지날 때마다 작아져서 나중에 1 or 0(진짜/가짜) 판별 값으로 나온다.  
파라미터들: 컨볼루션에 쓰이는 필터의 weight 값들.  
<br>
<br>

## Generator Network
Generator도 컨볼루션 뉴럴 네트워크이다. 입력으로 노이즈가 들어가면 4개의 컨볼루션을 지난다. 컨볼루션을 지날 때마다 커져서 output으로 컬러영상이 된다.  
<br>
<br>

## Strided Convolution
컨볼루션할때 사이즈가 커지는 것은 Fractionally-strided convolution을 이용하는 것이다.  
<br>
<br>

## Cost Function
필터의 파라미터를 찾으려면 cost function을 최소화해야 한다.  
초기의 논문의 비용함수는 다음과 같다.  
$V(D) = log D(x) + log(1 - D(\hat x))$  
- $X$: Real image
- $\hat X$: False image
V(D)라는 함수는 이 값을 크게하는 D를 찾고자 한다. (로스가 커지기를 원한다.) 여기에 -를 붙이면 로스를 최소화하는 함수가 된다.  
가짜 영상을 $\hat x = G(z)$라고 하자.  
$V(D, G) = log D(x) + log(1 - D(G(z)))$  
