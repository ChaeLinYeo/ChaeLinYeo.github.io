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

### Honey Tip! Dataframe의 각 column은 "Series"다!
```python
type(covid['Confirmed'])
# pandas.core.series.Series
```
csv의 열 중 하나인 'Confirmed'를 키를 갖는 열의 타입을 한번 살펴보니 Series라고 나온다!  
각 열이 Series이다. 즉 데이터프레임은 사실 Series의 별렬적인 모음이다. 레코드 단위로 묶은 것이다.  
Series를 얻었다는 것은, 인덱싱, 슬라이싱 등의 액션을 취해줄 수 있다는 것이다.  
```python
covid['Confirmed'][0] # 인덱스로 값 접근 
# 36263

covid['Confirmed'][1:5] # 슬라이싱
# 1     4880
# 2    27973
# 3      907
# 4      950
# Name: Confirmed, dtype: int64
```
<br>
<br>

### Pandas 활용 3. "조건"을 이용해서 데이터 접근하기
```python
# 신규확진자가 100명이 넘는 나라를 찾아보자!
# csv에서 New cases가 신규확진자이다.
covid[covid['New cases'] > 100]
# covid['New cases'] > 100는 100이 넘는 값에 대해 True/False를 반환한다. 이 결과를 covid의 key로 넣으면 key에 대한 값들만 출력해준다.
covid[covid['New cases'] > 100].head(5)
```
```python
# WHO 지역(WHO Region)이 동남아시아인 나라 찾기

covid['WHO Region'].unique() # 해당 열에 존재하는 유니크 값 찾기
# array(['Eastern Mediterranean', 'Europe', 'Africa', 'Americas',
#        'Western Pacific', 'South-East Asia'], dtype=object)

covid[covid['WHO Region'] == 'South-East Asia']
```
<br>
<br>

### Pandas 활용 4. 행을 기준으로 데이터 접근하기
```python
# 예시 데이터 - 도서관 정보

books_dict = {"Available":[True, True, False], "Location":[102, 215, 323], "Genre":["Programming", "Physics", "Math"]}

books_dict
# {'Available': [True, True, False],
#  'Location': [102, 215, 323],
#  'Genre': ['Programming', 'Physics', 'Math']}

books_df = pd.DataFrame(books_dict, index=['버그란 무엇인가', '두근두근 물리학', '미분해줘 홈즈'])

books_df
# 	            Available	Location	Genre
# 버그란 무엇인가	True	    102	        Programming
# 두근두근 물리학	True	    215	        Physics
# 미분해줘 홈즈	   False	   323	       Math
```
<br>
<br>

### 인덱스를 이용해서 가저오기 : `.loc[row, col]`
행과 열의 값을 특정해서 가져올 수 있다.  
```python
books_df.loc["버그란 무엇인가"]
# Available           True
# Location             102
# Genre        Programming
# Name: 버그란 무엇인가, dtype: object

type(books_df.loc["버그란 무엇인가"])
# pandas.core.series.Series
```
```python
# "미분해줘 홈즈"책이 대출 가능한지?
books_df.loc["미분해줘 홈즈"]['Available'] # False
books_df.loc["미분해줘 홈즈", 'Available'] # False
```
<br>
<br>

### 숫자 인덱스를 이용해서 가져오기 : `.iloc[rowidx, colidx]
문자 인덱스가 아닌 숫자 인덱스를 이용해 값을 가져올 수 있다. 순수하게 위치의 값으로 값을 가져올 수 있다.  
```python
# 인덱스 0행의 인덱스 1열 가지고 오기
books_df.iloc[0, 1] # 102

# 인덱스 1행의 인덱스 0~1열 가지고오기
books_df.iloc[1, 0:2]
```
<br>
<br>
<br>

## Pandas 활용 5. groupby
- Split : 특정한 "기준"을 바탕으로 DataFrame을 분할
- Apply : 통계함수 - sum(), mean(), median(), - 을 적용해서 각 데이터를 압축
- Combine : Apply된 결과를 바탕으로 새로운 Series를 생성(group_key : applied_value)
`.groupby()`  
```python
covid.head(5)

# WHO Region 별 확진자수

# 1. covid에서 확진자 수 column만 추출한다
# 2. 이를 covid의 WHO Region을 기준으로 groupby한다.
covid_by_region = covid['Confirmed'].groupby(by=covid["WHO Region"])

covid_by_region
# <pandas.core.groupby.generic.SeriesGroupBy object at 0x118a125e0>
```
결과가 표가 아니라 저런 객체가 나오는 이유는, 지금 groupby의 세가지 프로세스 중에 Split만 수행했기 때문이다.  
Split만 사용하면 데이터가 분산되어있기만 하지 유의미한 정보를 출력할 수는 없다.  
Apply를 진행하면, 즉 통계함수를 Split된 객체에 적용하면 Combine도 같이 된다.  
```python
covid_by_region.sum()
# WHO Region
# Africa                    723207
# Americas                 8839286
# Eastern Mediterranean    1490744
# Europe                   3299523
# South-East Asia          1835297
# Western Pacific           292428
# Name: Confirmed, dtype: int64
```
여기서잠깐! 표본의 수가 많아서 확진자 수가 많게 집계되어 보이는 것일 수도 있지 않은가?  
```python
# 국가당 감염자 수
covid_by_region.mean() # sum() / 국가 수
# WHO Region
# Africa                    15066.812500
# Americas                 252551.028571
# Eastern Mediterranean     67761.090909
# Europe                    58920.053571
# South-East Asia          183529.700000
# Western Pacific           18276.750000
# Name: Confirmed, dtype: float64
```
우려했던 바와 같이, 유럽같은 경우 표본의 수가 많아서 확진자 수가 많이 집계된 경우였다.  
South-East Asia의 경우 국가당 확진자 수가 많은 것임을 알 수 있다.  
이런 식으로 새로운 인사이트들을 뽑아낼 수 있다.  
<br>
<br>
<br>

### 1. covid 데이터에서 100 case 대비 사망률(`Deaths / 100 Cases`)이 가장 높은 국가는?
```python
import pandas as pd
covid = pd.read_csv("./archive/country_wise_latest.csv")

covid[covid['Deaths / 100 Cases'] == covid['Deaths / 100 Cases'].max()]['Country/Region']
```

### 2. covid 데이터에서 신규 확진자가 없는 나라 중 WHO Region이 'Europe'를 모두 출력하면?  
Hint : 한 줄에 동시에 두가지 조건을 Apply하는 경우 Warning이 발생할 수 있습니다.  
```python
covid_no_cases = covid['New cases']==0
covid_europe = covid['WHO Region']=='Europe'
answer = covid[covid_no_cases & covid_europe]
answer
```

### 3. 다음 [데이터](https://www.kaggle.com/neuromusic/avocado-prices)를 이용해 각 Region별로 아보카도가 가장 비싼 평균가격(AveragePrice)을 출력하면?
```python
avocado = pd.read_csv("./archive/avocado.csv")
exp = avocado.groupby(avocado['region'])
exp.max()
```