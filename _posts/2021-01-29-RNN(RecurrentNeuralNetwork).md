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
    - 완전연결의 단점: 오버피팅 -> 드롭아웃으로 dense한 것을 sparse하게 만듦으로써 오버피팅 방지
    - 많은 부분 신경망을 만들고, 앙상블 결합하는 기법
