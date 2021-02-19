---
title : "[NLP]Transforme와 BERT"
data : 2021-02-19 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
use_math: true
---
# 자연어 처리: 딥모델 - Transforemr와 BERT
## NLP와 딥모델
- NLP를 위한 딥모델들
    - RNN(LSTM 등)
    - TextCNN
    - Transformer
    - BERT(Transformer encoder를 사용)
    - GPT(Transformer decoder를 사용)
많은 모델들이 Transformer 모델에 기반을 둔다!  
<br>

## RNN
- 문제점
    - 멀리 떨어진 단어들 간의 의존성을 모델링하기 어려움
    - 순차적인 속성으로 인한 느린 속도
        - 한 단어의 프로세싱을 위해서 그 전의 단계로부터 넘어온 히든 state를 입력으로 사용하는게 순차적으로 일어난다.
        - 순차적이기 때문에 인풋이 길어지면 처리하기 힘들다.
        - 병렬화시키기 힘들다.
<br>

## textCNN
이미지처리의 CNN과정과 매우 유사.  
feature map 적용 -> max pooling -> 뽑혀진 특징들을 하나의 벡터로 병합 (dense 레이어를 두기도 함) -> 최종적인 softmax분류기  
- RNN에 비해 컨볼루션 연산이 병렬이 되기 때문에 계산이 빠르다.
- 하지만 멀리 떨어진 단어들 간의 의존성을 모델링하기 어려움
- 텍스트 분류 문제에 대해 나쁘지 않은 성능을 보인다.
<br>

## Transformer 모델
- Attention Is All You Need(이 모델이 소개된 논문 제목)
    - No RNN, No convolution
        - RNN구조도 필요없고, CNN처럼 컨볼루션도 필요없다.
    - 오직 attention으로만 단어의 의미를 문맥에 맞게 잘 표현할 수 있다.
    - 병렬화 기능
    - BERT, GPT등의 모델의 기반
<br>

## ML 모델 이해를 위한 팁
- 복잡한 ML 모델을 이해하기 위해서 다음과 같은 순서를 따라 갈 것
    - 이 모델이 풀려고 하는 문제는 무엇인가? (분류/번역/등등...)
    - 추론(inference) 단계를 먼저 이해. "학습"된 모델이 어떤 "입력"을 받아서 어떤 "출력"을 계산하는지 파악할 것
    - 무엇이 학습되는가(모델 파라미터는 무엇인가)? 모델 파라미터와 입력, 그리고 그 둘의 함수를 구분할 것.
    - 어떻게 학습되는가(모델 파라미터를 어떻게 학습하는가)? 어떤 에러함수를 사용하는가?
<br>

## Transformer
- 이 모델이 풀려고 하는 문제는 무엇인가?
    - Seq2seq: 시퀀스의 입력이 주어졌을때 시퀀스의 출력을 내보냄.
    - 순차적입력에 대해 순차적출력을 반환
    - 대표적인 예: 기계번역, 질의응답
- 다음 url 참고: <https://jalammar.github.io/illustrated-transformer>
<br>

### 추론단계 이해
- 모델이 학습되었다고 가정하고, 새로운 input이 들어왔을 때 output이 어떻게 계산되는지.
- 전체적인 구조: input(예: 프랑스어) -> transformer(블랙박스) -> output(예: 영어)
- transformer(블랙박스)의 구성
    - ENCODERS
        - 여러개의 동일한 인코더가 층을 이루며 쌓여있음
        - 각 인코더 안에 들어있는 모델 파라미터는 서로 공유되지 않는다. 다 다르다.
        - 각 단어들이 하나의 인코더를 지나갈때 인코더 안에서 다음과 같은 작업이 이루어진다.
            - Self-Attention: 각 단어의 임베딩이 Self-Attention의 인풋으로 들어가면서 다른 단어들과의 관계를 사용해서 단어의 의미가 좀더 정확해진다. 즉 각각의 단어의 의미를 이해하는데 있어 주변의 문맥을 사용한다. 서로 다른 단어들의 관계를 봐야해서 의존성이 있으므로 병렬화가 힘듦.
            - Feed Forward: Self-Attention의 출력이 인풋으로 사용된다. 서로 다른 단어에 대한 의존성이 없어 병렬화 가능. Feed Forward Neural Network로 구성되며, 모델이 표현할 수 있는 표현력을 더 높여준다.
            - 결과적으로 한 단어마다 임베딩이 있고, 그 임베딩이 계속해서 변해가면서 제일 위까지 올라가는 구조이다.
    - DECODERS
        - 여러개의 동일한 디코더가 층을 이루며 쌓여있음
        - 각 디코더 안에 들어있는 모델 파라미터는 서로 공유되지 않는다. 다 다르다.
<br>

### 추론단계 이해: Self-Attention
- "The animal didn't cross the street because it was too tired"
- 여기서 "it"이 가리키는 단어는?
- 단어의 의미는 문맥에 의해 결정된다. 같은 단어라도 문맥에 의해 뜻이 달라진다. 문맥화된다.
- 현재 단어의 의미(임베딩을 통해 표현되는)를 주변 단어들의 의미조합(weighted sum)으로 표현
    - 각 단어의 임베딩 마다 weight을 가진다.
<br>

### 추론단계 이해: Self-Attention(단어 임베딩 벡터 중심으로)
- 첫번째 단계
    - Input: 단어
    - Embedding: 인풋으로 주어진 단어가 임베딩되어 n차원이 된다. 이 단어임베딩으로 Queries, Keys, Values라는 벡터를 생성한다. $X_1, X_2,...$ 와 같이 쓴다.
    - Queries: 쿼리벡터 $q^T = X^T W^Q$, 입력과 모델 파라미터의 함수값은 $q^T$, 입력은 $X^T $, 모델 파라미터는 $W^Q$
    - Keys: 키벡터 $k^T = X^T W^K$, 입력과 모델 파라미터의 함수값은 $k^T$, 입력은 $X^T $, 모델 파라미터는 $W^K$
    - Values: 밸류벡터 $v^T = X^T W^V$, 입력과 모델 파라미터의 함수값은 $v^T$, 입력은 $X^T $, 모델 파라미터는 $W^V$
- 두번째 단계: 쿼리, 키, 밸류 벡터를 구했으면 attention행렬을 만든다. 
    - attention행렬의 j번째 원소($a_{ij}$일때 ): i번째 단어에 미치는 j번째 단어의 영향의 크기
    - $a_{ij}$를 구하는 방법: 
        - $q_i * k_i$ 쿼리벡터와 키벡터의 dot product을 하여 Score를 구한다. 자신을 포함한 모든 나머지 단어들의 키 벡터들과의 dot product를 구한다!
        - 그리고 위의 값을 임베딩의 사이즈(보통 64를 많이 쓴다)의 루트값인 8로 나눠준다.
        - 위의 값에 소프트맥스를 적용해 벡터값을 확률로 만들어준다.(다 더하면 1이 되는)
        - 위 과정들을 식으로 정리하면 다음과 같다.
            - ${exp(q_i^T k_j) \above 1pt \sum_j exp(q_i^T k_j)}$
- 세번째 단계: value벡터를 사용해 계산된 weight을 가지고 weighted sum을 구한다.
    - 두번째 단계의 소프트맥스 값인 weight값과 밸류벡터를 곱하여 더한다.(각 단어 임베딩마다 곱을 구한 뒤 모두 더한다.)
    - 결과는 다음의 식으로 표현할 수 있다.
        - $z_i = \sum_j a_{ij} v_j^T$
<br>

### 추론단계 이해: Self-Attention(행렬연산으로 표현)
- 실제로 위의 단계들을 구현할때는 벡터가 아닌 텐서로 구현한다. 
- X: 입력
- $W^Q, W^K, W^V$: 모델 파라미터
- Q, K, V: 입력과 모델 파라미터에 관한 함수의 출력값
    - $X * W^Q = Q$
    - $X * W^K = K$
    - $X * W^V = V$
- $softmax({Q*K^T \above 1pt \sqrt{d_k}} * V) = Z$
    - s: sequence length
    - h: size_per_head: 64 많이 씀
    - d: input embedding size, 512 많이 씀
    - X: 인풋, 행벡터 형태, s*d사이즈
    - $QK^T_{ij} = q_i^T k_j$
    - $ATT_{ij} = {exp(q_i^T k_j) \above 1pt \sum_j exp(q_i^T k_j)}$
        - $q_i^T k_j = {q_i^T k_j \above 1pt \sqrt {64}}$
    - ATT(attention 행렬)을 소프트맥스에 넣고 밸류벡터 V를 곱하면 끝! 이 최종적인 행렬을 Z라고 한다.
<br>

### 추론단계 이해: Multi-headed attention
- 다양한 attention matrix들을 반영하기 위한 방법. 
- CNN 모델에서 필터를 여러개 사용하는 것과 비슷한 맥락!
- 각각의 헤드마다 독립된 파라미터 행렬들이 생기고, 독립적으로 학습해야 한다.
- s*h의 Z가 N개 생긴다.
- 헤더의 개수를 무조건 늘린다고 좋은 것은 아니다! 
1. input이 단어들의 시퀀스 X로 주어진다.
2. 각 단어를 임베딩한다.
3. 모델 파라미터 $W^Q, W^K, W^V$가 하나의 헤드마다 있고, 이것을 사용해 입력행렬에 곱해준다.
4. 결과로 나온 Q, K, V행렬을 가지고 attention matrix를 계산한다.
5. 최종적으로 출력이 되는 Z 행렬을 사용해 모든 헤드들의 Z행렬을 합쳐준다. 합친 행렬에 W^O라는 또다른 행렬을 곱해 원래 input으로 들어왔던 X의 형태와 동일한 Z행렬을 출력한다. 
<br>

## Transformer: Self-Attention 구현
<https://github.com/google-research/bert/blob/master/modeling.py>  
- attention_layer함수에 Self-Attention이 구현되어 있다.
<br>

## 추론단계 이해: Positional encoding
- 단어의 순서를 어떻게 표현할 것인가?
    - 단어 뿐만 아니라 단어의 포지션도 임베딩으로 만들자는 아이디어엑서 착안
    - 이렇게 만들어진 포지션에 대한 임베딩이 인코더에 인풋으로 들어간다.
    - 임베딩은 따로 학습하지 않고 함수를 통해 표현한다. 첫번째 포지션에 대한 임베딩은 어떤 함수에 대해 의해 계산되고... n번째 포지션에 대한 임베딩도 마찬가지.
<br>

### 추론단계 이해: Residuals
- input(X) -> ENCOODER #1
- ENCODER #1 안에서 일어나는 작업들(구조)
    1. Self-Attention
    2. Add & Normalize - residual 커넥션
    3. Feed Forward: 각각의 단어가 별개로 처리된다. 병렬로 처리될 수 있다. 나머지는 병렬화할 수 없다.
    4. Add & Normalize - residual 커넥션
- Residual 커넥션은 input으로 들어온 임베딩이 attention을 거치지 않고 바로 attention의 아웃풋에 다시 더해주는 것이다.
- input 단어 임베딩으로 X1, X2가 들어오면 X2가 Add & Normalize마다 residual 커넥션을 통해 input으로 들어간다.
- deep한 모델에서 나타날 수 있는 banishing gradient문제를 방지한다.
<br>

### 추론단계 이해: Encoder 종합
- 동일한 구조를 가진 인코더들이 여러개가 쌓여 transformer를 만든다.
- 각각의 인코더들의 구조는 동일하지만 인코더들 간에 파라미터를 공유하진 않는다.
- 하나의 인코더에서 나온 아웃풋의 다른 인코더의 인풋이 된다.
- 제일 상단에 있는 인코더가 (마지막으로 출력하는 텐서가) 디코더 부분의 인자로 전달된다.
- 디코더가 하는 일은, 입력 단어들의 시퀀스에 대해 번역 등의 출력을 해준다.
<br>

### 추론단계 이해: Decoder
- 번역을 예시로 들었을 때
- 인코더 부분의 최종적인 출력 텐서는 K, V행렬이다. 이것을 디코더에 전달한다. 디코더는 주어진 정보를 바탕으로 해서 번역된 첫번째 단어를 출력한다. 
- 추론단계의 마지막에서 하는 일은 디코더에서 출력된 임베딩 벡터를 가지고 하나의 출력값을 계산하는 것이다. 예제의 경우 번역을 하는 것이기 때문에 vocabulary안에 속해 있는 하나의 단어를 출력하는 것이 된다. 임베딩 벡터는 단어 하나에 해당하고, 문장의 시작같은 경우 start of sentence같은 특수 기호가 되고, 어느정도 진행이 된 후의 임베딩은 직전 단어까지 번역된 정보가 함축되어있는 임베딩이다. 이것을 기초로 다음 단어가 무엇인지 예측하는 작업이다.
- 디코더에서 일어나는 작업은 다음과 같다.
1. 디코더는 주어진 임베딩 벡터를 가지고 Linear에서 logits값을 계산한다. logits값에 나타나는 스코어들이 단어가 가질 수 있는 확률이 된다.
2. Softmax를 통해 확률로 나타낸 것을 log_probs로 생성한다. log_probs에서 가장 큰 값을 가지는 것이 vocabulary에 해당되는 단어를 output으로 내보낸다.
<br>

## Transformer
- 모델학습의 에러함수는? Cross entropy
<br>

## BERT
- 이 모델이 풀려고 하는 문제는 무엇인가?
    - Transfer learning을 통해 적은 양의 데이터로도 양질의 모델(분류기 등)을 학습하는 것
    - Transformer모델로부터 파생되어 나왔다. 많은 모델들이 그렇다.
    - Transformer모델의 인코더 부분을 사용한다. 디코더 부분은 사용하지 않는다.
<br>

## 추론단계 이해: Fine-tuned 모델
Input(Features. 문자열, 문서와같은 시퀀스 데이터) -> BERT(블랙박스) -> Classifier(Feed-forward neural network + softmax) -> Output(Prediction)  
- input 문장 맨 처음에 CLS라는 특수한 토큰이 붙는다.
- output은 input 단어와 동일한 개수로 출력된다.
<br>

## 추론단계 이해: Pre-trained모델 - 입력/출력
- 여러개의 인코더가 모여있는 transformer의 인코더와 동일한 구조이다.
- 512개의 단어가 입력되면 동일한 개수의 벡터들이 출력된다.
<br>

## 추론단계 이해: Fine-tuned 모델 - 출력
- 입력된 단어들 전체에 대해서 임베딩 벡터를 모두 출력한다.
- Fine Tuning 단계에서는 Classification이 출력하는 단어 임베딩에 포커스를 맞춘다. 
- Classification에 우리가 원하는 classification을 쌓아올릴 수 있다. binary, multiclass classification 등등! 이부분은 소량의 데이터로 추가적인 학습이 이루어져야 한다.
<br>

## 모델 학습: Pre-trained 모델
- 인코더만으로 모델을 학습해야 한다.
- Masked language model
    - input의 여러 단어 중 랜덤하게 하나를 mask로 숨긴다. 그리고 버트 모델의 출력을 통해서 그 숨겨진 단어를 예측하게 만든다. 이로써 모델 파라미터를 학습시킨다. 이로써 trnasformer안에 있는 모델들의 파라미터 뿐만 아니라 인풋으로 주어지는 토큰들의 임베딩 까지도 학습할 수 있다.
    - 버트에서는 인풋을 프로세싱할 때 단어 단위가 아니라 subword단위로 한다. word piece라는 토크나이제이션을 사용해 서브워드 단위로 토큰을 나눠 vocabulary의 사이즈를 크게 줄인다. 
<br>

## BERT
- 모델 학습: Fine-tuned 모델
    - Pre-trained 모델의 파라미터를 기초로 새로운 작업(예를 들어 분류)을 위한 데이터(적은 양)를 사용해 파라미터를 업데이트한다.
<br>

## BERT: 응용
- 문맥화된 임베딩 생성: 버트를 통해서 나오는 아웃풋을 또다른 모델의 인풋으로 사용할 수 있다. 그렇게 생성된 벡터는 한 단어의 벡터가 아닌 문서/문장 전체의 임베딩이므로 "문맥화된 임베딩"이라고 한다.
    - Output중에 어떤 부분을 사용하면 좋은가? 
        - 최종적인 레이어만을 쓰는 경우: F1 score(클수록 좋음)이 94.9
        - 여러개의 레이어가 합쳐진 것(가장 상단의 4개의 레이어를 합쳤을 때): F1 score이 96.1로 가장 높았음
- Data Augmentation
    - 클래스를 바꾸지 않는 범위 안에서 입력을 변환. 학습데이터를 확장시킴. 더 나은 일반화성능 기대.
    - 이미지의 경우: shift, flip, resize, rotate
    - 텍스트의 경우: BERT모델의 아이디어를 그대로 사용할 수 있다. 
        - 문서 D와 클래스 c가 주어졌을 때, D의 단어들을 랜덤하게 mask한 다음 BERT를 사용해서 예측하고 그 결과를 D'으로 학습데이터에 추가한다(클래스 c와 함께).
        - GPT 모델을 사용해서 비슷한 방식으로 학습데이터를 확장할 수 있다.
    - 분류기 모델을 학습할때 binary가 아닌 multi class일 때, 특정 클래스에 대해 학습데이터가 부족할때 유용하다.
