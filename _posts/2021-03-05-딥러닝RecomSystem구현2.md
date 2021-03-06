---
title : "[Recommendation system]Deep Learning 기반의 Recommendation System 구현 II"
data : 2021-03-05 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
use_math: true
---
# ML 기반 추천 엔진: 마무리
## 추천 엔진 평가 방법
- 먼저 모델 평가에 사용할 지표 결정
    - Classification이면 Confusion matrix, AUC-ROC, F1 score
    - Regression이면 RMSE, MAE, Log loss
- 다음으로 평가 방법 결정
    - 홀드 아웃 테스트(Train & Test 혹은 Train & Validation)
    - 교차 검증(Cross-Validation 혹은 K-Fold 테스트)
        - 일반적으로 홀드아웃 방식보다 오버피팅 이슈가 없음
- 특수한 교차 검증 방식: LOOCV(Leave One Out Cross Validation)
    - 데이터셋에 있는 레코드 수만큼 폴드를 만드는 것이다. K-fold에서 K가 레코드 수가 되는 것. 레코드 수만큼 반복하게 된다.
    - 교차 검증에서 폴드 수가 트레이닝 데이터 레코드 수와 동일한 경우
    - 즉 테스트를 한 예제를 대상으로 하는 것. 가장 좋은 방법이지만 시간이 오래 걸림
    - 훈련 데이터에 총 N개의 예제가 있다면 N-1개로 학습한 후 나머지 1개로 테스트하는 것을 N번 반복
<br>
<br>

## 추천 엔진 평가 방법
- 평점 기반
    - 평점을 예측하고 실제 평점과 비교
    - 추천 엔진에서는 보통 RMSE 혹은 MAE를 사용
- Top-N 추천 정확도 기반
    - 사용자별로 일부 높은 평점 레코드(사용자, 아이템, 평점)를 따로 빼놓고 나중에 추천되는 아이템들과의 일치율을 계산
- LOOCV 테스트 방법과 병행하여 사용
    - 사이킷런과 surprise 라이브러리에서 지원
    - LOOCV는 교차검증 방식으로 테스트셋에 사용자별로 오직 하나의 평점만을 남기기 때문에 Leave One Out이라고 불림.
<br>
<br>

## Top N 추천 정확도
- 모델 방식의 추천이고 N이 10이라고 가정하고(top 10개의 아이템을 추천함) 사용자별로 아래를 반복
    - 평점 데이터에서 이 사용자의 모든 데이터를 찾는다
    - 여기서 한 평점 레코드를 빼서 테스트 셋에 추가
    - 나머지 레코드들을 훈련 셋에 추가
    - 훈련셋과 테스트셋을 나누는 기준이 사용자별이다. 
    - 모든 사용자에 대해 반복하면 테스트셋에는 데이터셋에 있는 평점이 존재하는 사용자의 수만큼의 레코드가 들어간다. 나머지가 훈련셋에 들어간다.
    -> surprise의 LeaveOneOut 모듈을 사용하여 사용자별로 평점 정보를 하나씩 테스트셋으로 저장하고 이를 나중에 Top N 추천 정확도 계산에 사용  
- 만들어진 훈련 셋으로 모델 학습
- 훈련에 사용되지 않은 모든 레코드들을 가지고 평점 예측
    - sparse한 행렬들을 훈련할때 쓸 수는 없지만 예측할때 쓸 수 있다. 테스트셋에 들어간 데이터와 테스트셋에 들어가진 않았지만 비어있는 데이터들이 훈련에 사용되지 않은 모든 레코드들이다.
    - 즉 기본적으로 평점 정보가 없는 모든 사용자 ID와 아이템 ID 레코드들(여기에는 테스트셋의 레코드들도 들어감)
- 사용자별로 테스트셋의 아이템 중 평점이 높은 것들 중에 추천된 Top 10개에 포함된 것의 비율 계산 후 평균 계산 -> 이게 바로 Toop N 추천 정확도
- Top N 추천 정확도: 모든 사용자들의 추천 정확도 평균
    - 원래 Top N 추천 정확도: 
        - 분모: 사용자별로 하나씩 떼서 테스트셋에 보관한 것 중 평점이 높은 것(예를 들어 4.5 이상)의 수
        - 분자: 그것들 중 각 사용자에게 추천이 된 아이템의 수
        - 이것을 사용자별로 다 계산에서 평균을 낸 것이 Top N 정확도
    - 추천 위치에 따라 가중치를줬다면 이를 Top N 추천 NDCG(Discounted Cumulative Gain) 정확도라 부름. 위치에 따라 디스카운트를 한다는 뜻. top 10이라면 top10보다 top1에게 더 높은 가중치를 주는 것이다.
<br>
<br>

## 추천 성능 평가가 어려운 이유
- 추천은 다양성이 있어야 함. 계속 비슷한 것만 추천하는 것은 좋지 않음.
- 사람의 취향은 변하며 상황에 따라 다른 추천을 해야함.
- 추천은 순서를 고려해야 함. 시리즈로 구성된 책이라면 시리즈의 첫 번째를 추천하는 것이 좋음.
<br>
<br>

# A/B 테스트란?
## A/B 테스트: 온라인 실험이라고 부르기도 함
- A/B 테스트란 다수의 그룹으로 구성. 하나의 컨트롤 그룹과 하나 이상의 테스트 그룹
    - 컨트롤 그룹: 기존의 서비스에 그대로 노출되는 그룹
    - 테스트 그룹: 새로운 테스트에 노출되는 그룹
    - 두 그룹으로 나눌 때 bias가 고르게 분포되도록 해야한다.
- 실제 사용자를 대상으로 새로운 기능이나 변경을 객관적으로 검증하는 방법
- 테스트 시작 전에 어떤 지표를 가지고 테스트의 성패 여부를 정할지 결정함. -> 결과의 자의적인 판단 방지
- 두 그룹으로 나눌 때 bias가 고르게 분포되도록 해야한다.
- 한번에 하나의 새로운 기능이나 변화를 테스트해야함
    - 동시에 2가지 이상을 테스트할 경우 결과를 해석할 수 없음
- 작은 수의 사용자들에게 먼저 노출시켜 위험부담 줄임 -> 지표를 모니터링하면서 점차적으로 노출 비율 높임
- A/B 테스트 인프라 없이는 테스트를 할 수도 없고 분석도 불가능!
    - 프런트엔드, 백엔드, 데이터, 모든 엔지니어링 팀의 도움이 필요
<br>
<br>

## A/B 테스트 방식 설명
- A/B 테스트 가설 세우기: ~한 기능을 노출하면 ~의 지표가 개선될 것이다.
- 사용자를 같은 크기와 같은 속성의 두 그룹으로 나누기(bias가 없어야함)
    - 기존 기능에 노출될 사용자 그룹
    - 새로운 기능에 노출될 사용자 그룹 
    - 그룹 사이의 차이점을 간략하게 테스트해보면 좋다(평균 연령, 사는 지역, 성별 등)
- 이 사용자들의 다양한 행동을 기록
    - 어떤 아이템을 보고, 클릭하고, 소비하고, 리뷰하는지...
- 두 개의 그룹별로 다양한 지표 계산 후 기록
    - 두 그룹 간의 지표 차이가 통계적으로 유의미한지? -> 통계적 지식 필요
- 시간이 지나면서 어떤 흐름이 있는지 확인
<br>
<br>

## 태블로 기반 A/B 테스트 대시보드 예제
분석 기간을 선택하여 다양한 A와 B 그룹간에 필터의 결과들을 볼 수 있다.  
<br>
<br>

# 추천 엔진과 개인 정보 보호
## 개인 정보란?
- 개인을 식별할 수 있는 정보
    - PII(Personally Identifiable Information)
    - 특정 개인을 알아보기 어려운 정보는 개인정보가 아님
- 개인 식별 정보의 예
    - 이름, 이메일, 전화번호, 주소, 카드정보 등
- 개인 식별 정보의 다른 예
    - 몇가지 조합으로 식별 가능한 준식별자
        - 이름, 나이, 거주지, 직장
<br>
<br>

## 개인 정보 보호란?
- 개인의 정보가 적절한 동의없이 노출되거나 배포되지 않은 것
- 관련 법안들
    - 국내
        - 개인정보 보호법, 통신사업자 대상의 정보통신망법
        - 클라우드 컴퓨팅법
    - 미국
        - Cloud Act, Honest Ads Act, FOSTA, FCC Regulation
        - CCPA
        - HIPPA
    - 유럽연합
        - GDPR
<br>
<br>

## GDPR이란?
- 2018년 5월 25일부터 시행된 유럽연합의 개인정보보호 법령
- 유럽연합내 모든 회원국에 일괄 적용(강제)
- 적용 대상 기업
    - 유럽연합내의 회사가 아니어도 적용가능(네이버를 프랑스 사람이 쓴다면 GDPR의 대상자 이런식)
    - EU 사용자가 있는 웹서비스의 경우 모두 적용대상
- 위반시 벌금이 엄청남..
- GDPR 세부사항
    - 서비스 약관이 강화되었고 아동정보에 대해 더 강한 보호
    - 회원국에 따라 민감정보의 처리는 원칙금지
    - 정보주체의 권리 강화로 회사들은 30일내에 응답해야함
- GDPR에서 프로파일링 거부권이란?
    - 프로파일링:
        - 개인의 경제적 상황, 관심, 행동 등을 데이터 기반으로 자동 분석 및 예측하는 것
        - 특정인에 대한 낙인, 차별, 감시 등 프라이버시 위험 요소가 될 수 있음
    - 프로파일링의 예:
        - 검색 로그를 뒤져서 테러를 저지를만한 사람들의 테러 저지를 확률 계산
        - 개인의 과거 구매 이력으로 광고 캠페인의 타겟으로 선정
    - 프라이버시를 존중하는 검색엔진들의 등장(품질은 떨어짐)
        - 덕덕고우(DuckDuckGo)
<br>
<br>

## 구글/페이스북/마이크로소프트가 아는 내 정보 찾아보기
- 구글: <https://takeout.google.com/?pli=1>
- 페이스북: Accessing & Downloading Your Information
- 마이크로소프트: <http://account.microsoft.com/privacy>
<br>
<br>

# 추천 엔진 개발 교훈
- Cold Start: 특히 협업필터링 기반 추천의 경우
    - 사용자 데이터: 사용자가 서비스를 처음 사용하기 시작하는 경우
    - 아이템 데이터: 아이템이 처음 서비스에 노출되기 시작하는 경우
- 확장성(Scalability)
    - 몇 천만의 사용자를 처리할 수 있나?
        - 서비스가 성장하면 사용자 수가 대폭 증가
    - 몇 천만의 아이템을 처리할 수 있나?
        - 사용자의 수에 비해 아이템의 수는 상대적으로 성장 폭이 작음
    - 모델링에 걸리는 시간 뿐만 아니라 서빙시 시간도 중요
        - 앙상블 모델은 성능은 좋지만 오래걸린다.
<br>
<br>

## 추천 엔진 개발시 고려할 점
- 명시적/암시적 레이블 데이터의 부족
    - 리뷰, 평점, 클릭 데이터의 크기는 상대적으로 작음
    - 평점 데이터는 악의적인 해킹으로 조작 가능/평점알바 등
- 다양한 아이템의 추천
    - 관심, 선호도 편향화 심화. 신선한 아이템 추천이 필요. 개인의 취향을 강요당하지 않고 찾아나갈 수 있어야 한다.
    - 새로운 아이템을 어떻게 노출시킬지 고민이 필요.
- 인프라 필요
    - 필요한 데이터가 수집, 저장돼야하고 이를 처리할 수 있는 인프라 필요
    - 기술적인 관점에서는 Spark가 많이 사용됨(대용량 데이터 처리)
- 개인 정보 보호
    - GDPR(유럽연합), CCPA(미국 캘리포니아)등의 법률 존재
    - 이 과정에서 의도치 않은 개인정보 노출 가능
<br>
<br>

