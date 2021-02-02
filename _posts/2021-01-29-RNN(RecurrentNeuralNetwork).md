---
title : "[Deep Learning: 신경망의 기초]RNN(Recurrent Neural Network)"
data : 2021-01-29 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
use_math: true
---
# 심층학습 최적화
## 드롭아웃
- 드롭아웃(dropout) 규제 기법
    - 완전연결층의 노드 중 일정 비율(일반적으로 p=0.5 적용)을 임의 선택하여 제거 -> 남은 부분 신경망 학습
    - 완전연결의 단점: 오버피팅 -> 드롭아웃으로 dense한 것을 sparse하게 만듦으로써 오버피팅 방지. 가중치들이 서로 비슷하게 동기화되어 학습되지 않고 특징별로 의미가 두드러지게 학습될 수 있음.(의미들이 세분화되고 부각됨)
    - 많은 부분 신경망을 만들고, 앙상블 결합하는 기법
- 요즘엔 드롭아웃보다는 배치 노말라이제이션을 많이 쓴다.
<br>

- 신경망의 완전연결층(FC)에 드롭아웃 적용 알고리즘
- 입력: 드롭아웃 비율 $p_{input}, p_{hidden}$
- 출력: 최적해 $\Theta$
- 난수를 생성하여 초기해 $\Theta$를 설정한다.
- while(! 멈춤조건) // 수렴조건
    - 미니배치 B를 샘플링한다.
    - for(i=1 to |B|)   // B의 샘플 각각에 대해
        - 입력층은 $p_{input}$, 은닉층은 $p_{hidden}$ 비율로 드롭아웃을 수행한다.
        - 드롭아웃된 부분 신경망 $\Theta_i^{dropout}$로 전방 계산을 한다.
        - 오류 역전파를 이용하여 $\Theta_i^{dropout}$를 위한 그레디언트 $\bigtriangledown_i^{dropout}$를 구한다.
    - 그레디언트들의 평균 $\bigtriangledown_{ave}^{dropout}$를 계산한다.
    - $\Theta = \Theta - \rho \bigtriangledown_{ave}^{dropout}$ // 가중치 갱신
- $\widehat{\Theta} = \Theta$
<br>

- 일반적으로 입력층 제거 비율 0.2, 은닉층 제거 비율 0.5로 설정
<br>

- 예측 단계
    - 앙상블 효과 모방 
        - 학습 과정에서 가중치가(1-드롭아웃 비율)만큼만 참여했기 때문에 p만큼 보정
- 메모리와 계산 효율
    - 추가 메모리는 참거짓 배열 $\pi$, 추가 계산은 작음
    - 실제 부담은 신경망의 크기에서 옴: 보통 은닉 노드 수를 $1 \above 1pt P_{hidden}$만큼 늘림
<br>
<br>

## 앙상블 기법
- 앙상블(ensemble)
    - 서로 다른 여러 개의 모델을 결합하여 일반화 오류를 줄이는 기법
    - 현대 기계학습은 앙상블도 규제로 여김
- 두 가지 일
    1. 서로 다른 예측기를 학습하는 일
        - 서로 다른 구조의 신경망 여러 개를 학습 또는 같은 구조를 사용하지만 서로 다른 초기값과 하이퍼 매개변수를 설정하고 학습
            - **배깅**(bagging, bootstrap aggregating): 훈련집합을 여러 번 샘플링하여(복원추출) 서로 다른 훈련집합을 구성. 동시다발적으로 학습.
            - **부스팅**(boosting): i번째 예측기가 틀린 샘플을 i+1번째 예측기가 잘 인식하도록 연계성을 고려. 순차적으로 학습하여 서로 상호보완적인 관계가 되도록함.
    2. 학습된 예측기를 결합하는 일 -> 모델 평균(model average)
        - 여러 모델의 출력에서 평균을 구하거나 투표하여 최종 결과 결정
<br>
<br>

## 하이퍼 매개변수 최적화
- 학습 모델에는 두 종류의 매개변수가 있음
    - 내부 매개변수(parameter) 혹은 가중치(weight)
        - 신경망의 경우, 가중치 $\Theta$fh vyrl
        - 학습 알고리즘이 최적화함
            - 주어진 데이터로부터 결정됨
    - 하이퍼 매개변수(hyper-parameter)
        - 모델의 외부에서 모델의 동작을 조정함
            - 사람에 의해서 결정됨
        - 예: 은닉층의 개수, CNN의 필터 크기와 epoch, 학습률 등
<br>

- 하이퍼 매개변수 선택
    - 표준 참고 문헌이 제시하는 기본값을 사용하면 됨
        - 보토 여러 후보 값 또는 범위를 제시
    - 후보 값 중에서 주어진 데이터에 최적인 값 선택 <- 하이퍼 매개변수 최적화
- 하이퍼 매개변수 조합 생성을 구현하는 방법에 따라 수동탐색, 격자탐색, 임의 탐색
    - 최근 학습을 통한 자동 탐색 방법들이 연구됨(자동화된 기계학습)
<br>
<br>

- 격자 탐색(grid search)과 임의 탐색(random search)
    - 격자탐색은 격자모양으로 나눴을 때 교차점들에 위치한 것들을 탐색.
    - 임의 탐색은 난수로 하이퍼 매개변수 조합을 생성함. 격자 탐색보다 임의 탐색이 좋다.
- 로그 공간(log space) 간격으로 탐색
    - 어떤 하이퍼 매개변수는 로그 공간을 사용해야 함
    - 학습률 범위가 있을 때 로그 공간 간격은 등 간격보다 2배 증가된 간격으로 공간을 조사한다.
<br>

- 차원의 저주 문제 발생
    - 차원의 저주: 고차원이 될수록 그 안에서 의미있는 값을 찾기 위해서는 더 많은 데이터가 필요하다.
    - 매개변수가 $m$개이고 각각이 $q$개 구간이라면 $q^m$개의 점을 조사해야 함
- 임의 탐색이 우월함
    - 크게 하면서 경향성을 찾은 뒤 점차 세밀해지는 coarse-fine 탐색
<br>
<br>

# 2차 미분을 이용한 최적화 방법
- 뉴턴 방법
- 켤레 경사도 방법
- 유사 뉴턴 방법
<br>
<br>

- 1차 미분을 사용하는 경사 하강법
    - 현재 기계 학습의 주류 알고리즘
    - 두 가지 개선책
        - 경사도의 잡음을 줄임(미니배치, 모멘텀 사용 등)
        - 2차 미분 정보를 활용
- 2차미분 방법보다는 1차미분 방법이 더 많이 쓰임! 아직 가야할 길이 멀다~ 하지만 1차 민분보다 효과적일 수 있는 가능성은 열려있다!
<br>

- 경사 하강법을 더 빠르게 할 수 있나?
    - 1차 미분 정보로는 경사 하강법으로 해를 찾아가는 최단 직선 경로를 알 수 없음. 1차 미분은 현재 위치에서 지역적인 기울기 정보만 주기 때문. -> 뉴턴 방법(newton method)은 2차 미분 정보를 활용하여 사 하강법으로 해를 찾아가는 최단 직선 경로를 알아냄.
<br>

- 1차 미분 최적화와 2차 미분 최적화 비교
    - 1차 미분의 최적화
        - 경사도 사용하여 선형 근사 사용
        - 근사치 최소화
    - 2차 미분의 최적화
        - 경사도와 헤시안을 사용하여 2차 근사(2차 함수가 근사함수가 됨) 사용
        - 근사치의 최소값
<br>
<br>

## 뉴턴 방법
- 테일러 급수: 주어진 함수를 정의역에서 특정 점의 미분계수들을 계수로 가지는 다항식의 극한(멱급수)으로 표현함
- 테일러 급수를 적용하여 델타로 미분하면,
    - $w+\delta$를 최소점이라 가정하면, ${\partial J(w + \delta) \above 1pt \partial \delta} \approx J'(w) + \delta J''(w) = 0$
- 식을 조금 정리하면, 
    - $\delta = -{J'(w) \above 1pt J''(w)} = -(J''(w))^{-1}J'(w)$
- 변수가 여러 개인 경우로 확장하면,
    - $\delta = -H^{-1}\bigtriangledown J$
<br>
<br>

## 켤레 경사도 방법
- 직선 탐색(line search): 이동 크기를 결정하기 위해 직선으로 탐색하고, 미분
    - 원래의 경사하강법의 직선탐색: 현재 점에서부터 2차로 근사화할때 근사하는 범위를 직선의 형태를 통해서 탐색하고, 이동할 크기(근사할 크기)에 따라 이동
    - 켤레 경사도 방법(conjugate gradient method): 직전 정보를 사용하여 해에 빨리 접근. 이전에 썼던 방향과 현재의 방향 두가지를 이용해 새로운 방향을 찾고 근사한다. 뉴턴 방법에 비해 훨씬 빠르게 근사할 수 있다.
<br>
<br>

## 유사 뉴턴 방법
- 유사 뉴턴 방법(quasi-Newton methods)의 기본 개념
    - 문제점
        - 경사 하강법: 수렴 효율성 낮음
        - 뉴턴 방법: 헤시안 행렬 연산 부담 -> 헤시안 H의 역행렬을 근사하는 행렬 M을 사용
    - 대표적으로 점진적으로 헤시안을 근사화하는 LFGS가 많이 사용됨
    - 기계 학습에서는 M을 저장하는 메모리를 적게 쓰는 **L-BFGS를 주로 사용함**
        - 전체 배치를 통한 갱신을 할 수 있다면, L-BFGS 사용을 고려함
- 기계 학습에서 2차 미분 정보의 활용
    - 현재 널리 활용되지는 않지만 연구 계속되고 있음
<br>
<br>
