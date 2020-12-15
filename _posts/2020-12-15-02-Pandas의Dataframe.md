---
title : "[Python으로 데이터 다루기 II - Pandas]4강:Pandas의 Dataframe"
data : 2020-12-15 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
use_math: true
---
## Pandas로 2차원 데이터 다루기 - dataframe
### dataframe?
- 2-D labeled table
- key와 value가 있는 labeled된 자료구조
- 인덱스를 지정할 수도 있음. 데이터를 참조하는 데 쓰임
딕셔너리를 사용하여 데이터프레임을 만들 수 있다.  
Series에서는 리스트로 먼저 시작했지만, 데이터프레임의 경우 리스트만 가지고는 2차원 구조를 만들기 버겁다는 특징이 있다.  
표(테이블)이라는 데이터 자체가 가로와 세로를 가져야 하는데, 리스트보다는 딕셔너리가 2차원 구조를 표현하기에 적합하다.  
```python
d = {"height":[1, 2, 3, 4], "weight":[30, 40, 50, 60]}

df = pd.DataFrame(d)

df
# 	height	weight
# 0	    1	    30
# 1	    2	    40
# 2	    3	    50
# 3	    4	    60
```
행이 어떤 특정 데이터 하나를 의미하고, 각 데이터는 여러 column을 가지는 형태를 볼 수 있다.  
예를 들어 인덱스 0의 데이터는 height가 1이고 weight가 30인 데이터이다.  
데이터프레임의 경우 numpy의 array와 다르게 숫자만 받는 게 아니라 문자, 날짜, 객체 등 여러 타입을 다뤄줄 수 있다. 따라서 height, weight 열에 대해 어떤 자료형이 담겼는지 확인해줄 필요가 있다.  
numpy에서는 동일한 데이터를 담았기 때문에 `numpy.array.dtype`와 같이 적어줬었다.  
pandas의 경우 여러 열이 존재하기 때문에, 각 열에 따라 데이터타입이 다를 수 있다.  
`df.dtypes`
```python
# dtype 확인
df.dtypes
# height    int64
# weight    int64
# dtype: object
```
<br>
<br>

### From CSV to dataframe
pandas는 csv(데이터) -> dataframe으로 바꿀 수 있는 함수를 지원한다.  
- Comma Separated Value를 Data Frame으로 생성해줄 수 있다. 
- `.read_csv()`를 이용
https://www.kaggle.com/imdevskp/corona-virus-report#  
위 링크에서 COVID-19데이터셋 다운로드!  
```python
# 동일 경로에 country_wise_latest.csv가 존재하면:
covid = pd.read_csv("./archive/country_wise_latest.csv") # csv 파일이 있는 경로

covid
```
<br>
<br>

### Pandas 활용 1. 일부분만 관찰하기
`head(n)` : 처음 n개의 데이터 참조
```python
# 위에서부터 5개를 관찰하는 방법(함수)
covid.head(5)
```
`tail(n)` : 마지막 n개의 데이터 참조
```python
# 아래에서부터 5개를 관찰하는 방법(함수)
covid.tail(5)
```
<br>
<br>

### Pandas 활용 2. 데이터 접근하기
- `df['column name']` or `df.column_name`
```python
covid['Active'] # 띄어쓰기 포함된 Key를 찾을 수 있음
covid.Active # 띄어쓰기 포함된 Key를 찾을 수 없음
```
주의! : csv에서 column의 name은 띄어쓰기가 들어있다. 따라서 띄어쓰기가 들어있는 열을 접근하기 위해서는 `df.column_name`이 아닌 `df['column name']`을 써야 한다.  