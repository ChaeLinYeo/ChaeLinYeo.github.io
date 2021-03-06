---
title : "EDA 프로젝트"
data : 2020-12-18 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
use_math: true
---
## Mission : It's Your Turn!

### 1. 본문에서 언급된 Feature를 제외하고 유의미한 Feature를 1개 이상 찾아봅시다.

- Hint : Fare? Sibsp? Parch?

### 2. [Kaggle](https://www.kaggle.com/datasets)에서 Dataset을 찾고, 이 Dataset에서 유의미한 Feature를 3개 이상 찾고 이를 시각화해봅시다.

함께 보면 좋은 라이브러리 document
- [numpy]()
- [pandas]()
- [seaborn]()
- [matplotlib]()

무대뽀로 하기 힘들다면? 다음 Hint와 함께 시도해봅시다:
1. 데이터를 톺아봅시다.
- 각 데이터는 어떤 자료형을 가지고 있나요?
- 데이터에 결측치는 없나요? -> 있다면 이를 어떻게 메꿔줄까요?
- 데이터의 자료형을 바꿔줄 필요가 있나요? -> 범주형의 One-hot encoding
2. 데이터에 대한 가설을 세워봅시다.
- 가설은 개인의 경험에 의해서 도출되어도 상관이 없습니다.
- 가설은 명확할 수록 좋습니다. ex) Titanic Data에서 Survival 여부와 성별에는 상관관계가 있다!
3. 가설을 검증하기 위한 증거를 찾아봅시다.
- 이 증거는 한 눈에 보이지 않을 수 있습니다. 우리가 다룬 여러 Technique를 써줘야 합니다.
- `groupby()`를 통해서 그룹화된 정보에 통계량을 도입하면 어떨까요?
- 시각화를 통해 일목요연하게 보여주면 더욱 좋겠죠?


```python
# 라이브러리 선언
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline
```


```python
# 데이터 불러오기
data = pd.read_csv('./bestsellers with categories.csv')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Author</th>
      <th>User Rating</th>
      <th>Reviews</th>
      <th>Price</th>
      <th>Year</th>
      <th>Genre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10-Day Green Smoothie Cleanse</td>
      <td>JJ Smith</td>
      <td>4.7</td>
      <td>17350</td>
      <td>8</td>
      <td>2016</td>
      <td>Non Fiction</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11/22/63: A Novel</td>
      <td>Stephen King</td>
      <td>4.6</td>
      <td>2052</td>
      <td>22</td>
      <td>2011</td>
      <td>Fiction</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12 Rules for Life: An Antidote to Chaos</td>
      <td>Jordan B. Peterson</td>
      <td>4.7</td>
      <td>18979</td>
      <td>15</td>
      <td>2018</td>
      <td>Non Fiction</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1984 (Signet Classics)</td>
      <td>George Orwell</td>
      <td>4.7</td>
      <td>21424</td>
      <td>6</td>
      <td>2017</td>
      <td>Fiction</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5,000 Awesome Facts (About Everything!) (Natio...</td>
      <td>National Geographic Kids</td>
      <td>4.8</td>
      <td>7665</td>
      <td>12</td>
      <td>2019</td>
      <td>Non Fiction</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Non Fiction과 Fiction장르의 가격차이

plt.hist(data[data['Genre']=='Non Fiction']['Price'])
plt.hist(data[data['Genre']=='Fiction']['Price'])
plt.legend(['Non Ficton', 'Fiction'])

plt.show()
# 전반적으로 Non Fiction인 책이 Fiction인 책보다 가격대가 높음을 알 수 있다.
# Non Fiction인 책의 경우 전문서적 등이 많이 포함되어 Fiction인 책보다 가격대가 높은 게 않을까?
```


    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_38_0.png)
    



```python
# Non Fiction과 Fiction장르의 리뷰차이
sns.heatmap(data[['Genre','Reviews']].groupby(['Genre']).mean(), annot=True)
plt.show()
# Fiction이 Non Fiction보다 리뷰가 많은 것을 알 수 있다.
```


    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_39_0.png)
    



```python
sns.heatmap(data.corr(), annot=True)
plt.show()
```


    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_40_0.png)
    


# 음.. 딱히 건져낼만한 유의미한 Feature을 더 찾기 힘들어서 다른 데이터셋으로 해보았다. 강한 상관관계가 보이지 않는다.
### 상관계수에 대하여
- -1에 가까운 값이 얻어지면 : 누가 봐도 매우 강력한 음(-)의 상관. 오히려 너무 확고하기 때문에 사회과학 데이터일 경우 데이터를 조작한 게 아닌가 의심할 정도이다. 물론 이건 사회과학 얘기고 순수학문에 가까운 분야일수록 요구되는 상관관계는 높은 편.
- -0.5 정도의 값이 얻어지면 : 강력한 음(-)의 상관. 연구자는 변인 x 가 증가하면 변인 y 가 감소한다고 자신 있게 말할 수 있다.
- -0.2 정도의 값이 얻어지면 : 음(-)의 상관이긴 한데 너무 약해서 모호하다. 상관관계가 없다고는 할 수 없지만 좀 더 의심해 봐야 한다.
- 0 정도의 값이 얻어지면 : 대부분의 경우, 상관관계가 있을거라고 간주되지 않는다. 다른 후속 연구들을 통해 뒤집어질지는 모르지만 일단은 회의적이다. 하지만 무조건적으로 그런건 아니라 2차 방정식 그래프와 비슷한 모양이 될 경우 상관관계는 있으나 상관계수는 0에 가깝게 나온다.
- 0.2 정도의 값이 얻어지면 : 너무 약해서 의심스러운 양(+)의 상관. 이것만으로는 상관관계에 대해 아주 장담할 수는 없다. 하지만 사회과학에선 매우 큰 상관관계가 있는 것으로 간주한다.
- 0.5 정도의 값이 얻어지면 : 강력한 양(+)의 상관. 변인 x 가 증가하면 변인 y 가 증가한다는 주장은 이제 통계적으로 지지받고 있다.
- 1에 가까운 값이 얻어지면 : 이상할 정도로 강력한 양(+)의 상관. 위와 마찬가지로, 이렇게까지 확고한 상관관계는 오히려 쉽게 찾아보기 어렵다.

# Word Happiness Report 데이터셋
### https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html
- pandas API레퍼런스
### http://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot
- seaborn API레퍼런스


```python
data15 = pd.read_csv('./word_happiness_report/2015.csv')
data16 = pd.read_csv('./word_happiness_report/2016.csv')
data17 = pd.read_csv('./word_happiness_report/2017.csv')
data18 = pd.read_csv('./word_happiness_report/2018.csv')
data19 = pd.read_csv('./word_happiness_report/2019.csv')
# data = pd.concat([data15,data16,data17,data18,data19])
# data
# sns.heatmap(data.corr(), annot=True)
# 위와 같이 5개의 데이터를 한번에 합쳤더니 column도 다 다르고, 결측치도 많아서 엄청나게 더러워졌다 ㅠ
# 일단 각 column을 살펴보면서 정리해줘야겠다! 버릴 건 drop하고, 의미가 같지만 이름이 다른 column끼리는 통합해주고.
```


```python
data15.head(5)
# Standard Error는 2015년에만 존재한다.
# Dystopia Residual도 2015년과 2016년에만 존재한다. 2017년의 Dystopia.Residual와 같다.
# Region은 2015, 2016년에만 있다.
# Country는 다른 연도의 Country or region과 같은 내용을 담고 있다.
# Overall rank == Happiness Rank

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Region</th>
      <th>Happiness Rank</th>
      <th>Happiness Score</th>
      <th>Standard Error</th>
      <th>Economy (GDP per Capita)</th>
      <th>Family</th>
      <th>Health (Life Expectancy)</th>
      <th>Freedom</th>
      <th>Trust (Government Corruption)</th>
      <th>Generosity</th>
      <th>Dystopia Residual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Switzerland</td>
      <td>Western Europe</td>
      <td>1</td>
      <td>7.587</td>
      <td>0.03411</td>
      <td>1.39651</td>
      <td>1.34951</td>
      <td>0.94143</td>
      <td>0.66557</td>
      <td>0.41978</td>
      <td>0.29678</td>
      <td>2.51738</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Iceland</td>
      <td>Western Europe</td>
      <td>2</td>
      <td>7.561</td>
      <td>0.04884</td>
      <td>1.30232</td>
      <td>1.40223</td>
      <td>0.94784</td>
      <td>0.62877</td>
      <td>0.14145</td>
      <td>0.43630</td>
      <td>2.70201</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Denmark</td>
      <td>Western Europe</td>
      <td>3</td>
      <td>7.527</td>
      <td>0.03328</td>
      <td>1.32548</td>
      <td>1.36058</td>
      <td>0.87464</td>
      <td>0.64938</td>
      <td>0.48357</td>
      <td>0.34139</td>
      <td>2.49204</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Norway</td>
      <td>Western Europe</td>
      <td>4</td>
      <td>7.522</td>
      <td>0.03880</td>
      <td>1.45900</td>
      <td>1.33095</td>
      <td>0.88521</td>
      <td>0.66973</td>
      <td>0.36503</td>
      <td>0.34699</td>
      <td>2.46531</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Canada</td>
      <td>North America</td>
      <td>5</td>
      <td>7.427</td>
      <td>0.03553</td>
      <td>1.32629</td>
      <td>1.32261</td>
      <td>0.90563</td>
      <td>0.63297</td>
      <td>0.32957</td>
      <td>0.45811</td>
      <td>2.45176</td>
    </tr>
  </tbody>
</table>
</div>




```python
data16.head(5)
# Dystopia Residual도 2015년과 2016년에만 존재한다. 2017년의 Dystopia.Residual와 같다.
# Region은 2015, 2016년에만 있다.
# Country는 다른 연도의 Country or region과 같은 내용을 담고 있다.
# Lower Confidence Interval은 2016년에만 있다.
# Upper Confidence Interval도 2016년에만 있다.
# Overall rank == Happiness Rank
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Region</th>
      <th>Happiness Rank</th>
      <th>Happiness Score</th>
      <th>Lower Confidence Interval</th>
      <th>Upper Confidence Interval</th>
      <th>Economy (GDP per Capita)</th>
      <th>Family</th>
      <th>Health (Life Expectancy)</th>
      <th>Freedom</th>
      <th>Trust (Government Corruption)</th>
      <th>Generosity</th>
      <th>Dystopia Residual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Denmark</td>
      <td>Western Europe</td>
      <td>1</td>
      <td>7.526</td>
      <td>7.460</td>
      <td>7.592</td>
      <td>1.44178</td>
      <td>1.16374</td>
      <td>0.79504</td>
      <td>0.57941</td>
      <td>0.44453</td>
      <td>0.36171</td>
      <td>2.73939</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Switzerland</td>
      <td>Western Europe</td>
      <td>2</td>
      <td>7.509</td>
      <td>7.428</td>
      <td>7.590</td>
      <td>1.52733</td>
      <td>1.14524</td>
      <td>0.86303</td>
      <td>0.58557</td>
      <td>0.41203</td>
      <td>0.28083</td>
      <td>2.69463</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Iceland</td>
      <td>Western Europe</td>
      <td>3</td>
      <td>7.501</td>
      <td>7.333</td>
      <td>7.669</td>
      <td>1.42666</td>
      <td>1.18326</td>
      <td>0.86733</td>
      <td>0.56624</td>
      <td>0.14975</td>
      <td>0.47678</td>
      <td>2.83137</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Norway</td>
      <td>Western Europe</td>
      <td>4</td>
      <td>7.498</td>
      <td>7.421</td>
      <td>7.575</td>
      <td>1.57744</td>
      <td>1.12690</td>
      <td>0.79579</td>
      <td>0.59609</td>
      <td>0.35776</td>
      <td>0.37895</td>
      <td>2.66465</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Finland</td>
      <td>Western Europe</td>
      <td>5</td>
      <td>7.413</td>
      <td>7.351</td>
      <td>7.475</td>
      <td>1.40598</td>
      <td>1.13464</td>
      <td>0.81091</td>
      <td>0.57104</td>
      <td>0.41004</td>
      <td>0.25492</td>
      <td>2.82596</td>
    </tr>
  </tbody>
</table>
</div>




```python
data17.head(5)
# Country는 다른 연도의 Country or region과 같은 내용을 담고 있다.
# Whisker.high는 2017년에만 있다.
# Whisker.low도 2017년에만 있다.
# Dystopia.Residual는 2017년에만 있다. 2015,1016년의 Dystopia Residual와 같다.
# Overall rank == Happiness Rank
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Happiness.Rank</th>
      <th>Happiness.Score</th>
      <th>Whisker.high</th>
      <th>Whisker.low</th>
      <th>Economy..GDP.per.Capita.</th>
      <th>Family</th>
      <th>Health..Life.Expectancy.</th>
      <th>Freedom</th>
      <th>Generosity</th>
      <th>Trust..Government.Corruption.</th>
      <th>Dystopia.Residual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Norway</td>
      <td>1</td>
      <td>7.537</td>
      <td>7.594445</td>
      <td>7.479556</td>
      <td>1.616463</td>
      <td>1.533524</td>
      <td>0.796667</td>
      <td>0.635423</td>
      <td>0.362012</td>
      <td>0.315964</td>
      <td>2.277027</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Denmark</td>
      <td>2</td>
      <td>7.522</td>
      <td>7.581728</td>
      <td>7.462272</td>
      <td>1.482383</td>
      <td>1.551122</td>
      <td>0.792566</td>
      <td>0.626007</td>
      <td>0.355280</td>
      <td>0.400770</td>
      <td>2.313707</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Iceland</td>
      <td>3</td>
      <td>7.504</td>
      <td>7.622030</td>
      <td>7.385970</td>
      <td>1.480633</td>
      <td>1.610574</td>
      <td>0.833552</td>
      <td>0.627163</td>
      <td>0.475540</td>
      <td>0.153527</td>
      <td>2.322715</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Switzerland</td>
      <td>4</td>
      <td>7.494</td>
      <td>7.561772</td>
      <td>7.426227</td>
      <td>1.564980</td>
      <td>1.516912</td>
      <td>0.858131</td>
      <td>0.620071</td>
      <td>0.290549</td>
      <td>0.367007</td>
      <td>2.276716</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Finland</td>
      <td>5</td>
      <td>7.469</td>
      <td>7.527542</td>
      <td>7.410458</td>
      <td>1.443572</td>
      <td>1.540247</td>
      <td>0.809158</td>
      <td>0.617951</td>
      <td>0.245483</td>
      <td>0.382612</td>
      <td>2.430182</td>
    </tr>
  </tbody>
</table>
</div>




```python
data18.head(5)
# Country or region은 다른 연도의 Country와 같은 내용을 담고 있다.
# Overall rank == Happiness Rank
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Overall rank</th>
      <th>Country or region</th>
      <th>Score</th>
      <th>GDP per capita</th>
      <th>Social support</th>
      <th>Healthy life expectancy</th>
      <th>Freedom to make life choices</th>
      <th>Generosity</th>
      <th>Perceptions of corruption</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Finland</td>
      <td>7.632</td>
      <td>1.305</td>
      <td>1.592</td>
      <td>0.874</td>
      <td>0.681</td>
      <td>0.202</td>
      <td>0.393</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Norway</td>
      <td>7.594</td>
      <td>1.456</td>
      <td>1.582</td>
      <td>0.861</td>
      <td>0.686</td>
      <td>0.286</td>
      <td>0.340</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Denmark</td>
      <td>7.555</td>
      <td>1.351</td>
      <td>1.590</td>
      <td>0.868</td>
      <td>0.683</td>
      <td>0.284</td>
      <td>0.408</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Iceland</td>
      <td>7.495</td>
      <td>1.343</td>
      <td>1.644</td>
      <td>0.914</td>
      <td>0.677</td>
      <td>0.353</td>
      <td>0.138</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Switzerland</td>
      <td>7.487</td>
      <td>1.420</td>
      <td>1.549</td>
      <td>0.927</td>
      <td>0.660</td>
      <td>0.256</td>
      <td>0.357</td>
    </tr>
  </tbody>
</table>
</div>




```python
data19.head(5)
# Country or region은 다른 연도의 Country와 같은 내용을 담고 있다.
# Overall rank == Happiness Rank
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Overall rank</th>
      <th>Country or region</th>
      <th>Score</th>
      <th>GDP per capita</th>
      <th>Social support</th>
      <th>Healthy life expectancy</th>
      <th>Freedom to make life choices</th>
      <th>Generosity</th>
      <th>Perceptions of corruption</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Finland</td>
      <td>7.769</td>
      <td>1.340</td>
      <td>1.587</td>
      <td>0.986</td>
      <td>0.596</td>
      <td>0.153</td>
      <td>0.393</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Denmark</td>
      <td>7.600</td>
      <td>1.383</td>
      <td>1.573</td>
      <td>0.996</td>
      <td>0.592</td>
      <td>0.252</td>
      <td>0.410</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Norway</td>
      <td>7.554</td>
      <td>1.488</td>
      <td>1.582</td>
      <td>1.028</td>
      <td>0.603</td>
      <td>0.271</td>
      <td>0.341</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Iceland</td>
      <td>7.494</td>
      <td>1.380</td>
      <td>1.624</td>
      <td>1.026</td>
      <td>0.591</td>
      <td>0.354</td>
      <td>0.118</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Netherlands</td>
      <td>7.488</td>
      <td>1.396</td>
      <td>1.522</td>
      <td>0.999</td>
      <td>0.557</td>
      <td>0.322</td>
      <td>0.298</td>
    </tr>
  </tbody>
</table>
</div>



### 이제 모든 연도에 있지 않은 column들은 삭제해줄건데, del과 drop중 뭐를 쓰는게 좋을지 몰라서 찾아봤다.
del은 "remove an item from a list"라며 list를 기준으로 remove가 일어납니다. drop은 pandas.DataFrame.drop method로서 pandas에 특화되어 있기 때문에 drop을 사용하는걸 추천드립니다.  
라고 나오길래 drop을 쓰기로 했다..!  
사용된 파라미터는 다음과 같다(판다스 API레퍼런스에 의하면..)  
- columnssingle label or list-like
    - Alternative to specifying axis (labels, axis=1 is equivalent to columns=labels).
- nplacebool, default False
    - If False, return a copy. Otherwise, do operation inplace and return None.
- errors{‘ignore’, ‘raise’}, default ‘raise’
    - If ‘ignore’, suppress error and only existing labels are dropped.
- axis{0 or ‘index’, 1 or ‘columns’}, default 0
    - Whether to drop labels from the index (0 or ‘index’) or columns (1 or ‘columns’).


```python
data15.drop(columns="Standard Error",inplace=True,errors="ignore", axis=1)
data15.drop(columns="Dystopia Residual",inplace=True,errors="ignore", axis=1)
data15.drop(columns="Region",inplace=True,errors="ignore", axis=1)

data16.drop(columns="Lower Confidence Interval",inplace=True,errors="ignore", axis=1)
data16.drop(columns="Upper Confidence Interval",inplace=True,errors="ignore", axis=1)
data16.drop(columns="Dystopia Residual",inplace=True,errors="ignore", axis=1)
data16.drop(columns="Region",inplace=True,errors="ignore", axis=1)

data17.drop(columns="Whisker.high",inplace=True,errors="ignore", axis=1)
data17.drop(columns="Whisker.low",inplace=True,errors="ignore", axis=1)
data17.drop(columns="Dystopia.Residual",inplace=True,errors="ignore", axis=1)
```

### 이제 모든 연도에 공통적으로 있는 column들만 남았다.  근데 같은 내용을 담고 있는 column들이라도 이름이 다른 경우가 있어 통일해줘야한다(노가다)


```python
data15=data15.rename(columns={"Country" : "Country or region",
                            "Economy (GDP per Capita)":"GDP per capita",
                            "Health (Life Expectancy)":"Healthy life expectancy",
                            "Trust (Government Corruption)":"Perceptions of corruption"})
```


```python
data16=data16.rename(columns={"Country" : "Country or region",
                            "Economy (GDP per Capita)":"GDP per capita",
                            "Health (Life Expectancy)":"Healthy life expectancy",
                            "Trust (Government Corruption)":"Perceptions of corruption"})
```


```python
data17=data17.rename(columns={"Country" : "Country or region",
                            "Happiness.Score":"Happiness Score",
                            "Economy..GDP.per.Capita.":"GDP per capita",
                            "Health..Life.Expectancy.":"Healthy life expectancy",
                            "Trust..Government.Corruption.":"Perceptions of corruption",
                             "Happiness.Rank" : "Happiness Rank"})
```


```python
data18=data18.rename(columns={"Freedom to make life choices" : "Freedom",
                             "Score" : "Happiness Score",
                             "Social support" : "Family",
                             "Overall rank" : "Happiness Rank"})
```


```python
data19=data19.rename(columns={"Freedom to make life choices" : "Freedom",
                             "Score" : "Happiness Score",
                             "Social support" : "Family",
                             "Overall rank" : "Happiness Rank"})
```


```python
alldata = pd.concat([data15,data16,data17,data18,data19])
alldata
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country or region</th>
      <th>Happiness Rank</th>
      <th>Happiness Score</th>
      <th>GDP per capita</th>
      <th>Family</th>
      <th>Healthy life expectancy</th>
      <th>Freedom</th>
      <th>Perceptions of corruption</th>
      <th>Generosity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Switzerland</td>
      <td>1</td>
      <td>7.587</td>
      <td>1.39651</td>
      <td>1.34951</td>
      <td>0.94143</td>
      <td>0.66557</td>
      <td>0.41978</td>
      <td>0.29678</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Iceland</td>
      <td>2</td>
      <td>7.561</td>
      <td>1.30232</td>
      <td>1.40223</td>
      <td>0.94784</td>
      <td>0.62877</td>
      <td>0.14145</td>
      <td>0.43630</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Denmark</td>
      <td>3</td>
      <td>7.527</td>
      <td>1.32548</td>
      <td>1.36058</td>
      <td>0.87464</td>
      <td>0.64938</td>
      <td>0.48357</td>
      <td>0.34139</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Norway</td>
      <td>4</td>
      <td>7.522</td>
      <td>1.45900</td>
      <td>1.33095</td>
      <td>0.88521</td>
      <td>0.66973</td>
      <td>0.36503</td>
      <td>0.34699</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Canada</td>
      <td>5</td>
      <td>7.427</td>
      <td>1.32629</td>
      <td>1.32261</td>
      <td>0.90563</td>
      <td>0.63297</td>
      <td>0.32957</td>
      <td>0.45811</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>151</th>
      <td>Rwanda</td>
      <td>152</td>
      <td>3.334</td>
      <td>0.35900</td>
      <td>0.71100</td>
      <td>0.61400</td>
      <td>0.55500</td>
      <td>0.41100</td>
      <td>0.21700</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Tanzania</td>
      <td>153</td>
      <td>3.231</td>
      <td>0.47600</td>
      <td>0.88500</td>
      <td>0.49900</td>
      <td>0.41700</td>
      <td>0.14700</td>
      <td>0.27600</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Afghanistan</td>
      <td>154</td>
      <td>3.203</td>
      <td>0.35000</td>
      <td>0.51700</td>
      <td>0.36100</td>
      <td>0.00000</td>
      <td>0.02500</td>
      <td>0.15800</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Central African Republic</td>
      <td>155</td>
      <td>3.083</td>
      <td>0.02600</td>
      <td>0.00000</td>
      <td>0.10500</td>
      <td>0.22500</td>
      <td>0.03500</td>
      <td>0.23500</td>
    </tr>
    <tr>
      <th>155</th>
      <td>South Sudan</td>
      <td>156</td>
      <td>2.853</td>
      <td>0.30600</td>
      <td>0.57500</td>
      <td>0.29500</td>
      <td>0.01000</td>
      <td>0.09100</td>
      <td>0.20200</td>
    </tr>
  </tbody>
</table>
<p>782 rows × 9 columns</p>
</div>




```python
sns.heatmap(alldata.corr(), annot=True)
```




    <AxesSubplot:>




    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_57_1.png)
    


### 이제 깔끔하게 2015~20019년도를 합쳐서 column간의 상관관계를 파악할 수 있다!!
### 강한 상관관계를 갖는 column들 중, -0.5 또는 0.5에 가까운 값을 갖는 것들
- Happiness Score & Freedom : 0.55
- GDP per capita & Family : 0.59
- Family & Freedom : 0.42
- Healthy life expectanacy & Family : 0.57
- Freedom & Perception of corruption : 0.46
- Freedom & Happiness Rank : -0.54

### 1. Happiness Score & Freedom : 0.55


```python
sns.scatterplot(x='Happiness Score', y='Freedom', hue='Freedom', data=alldata)
plt.xlabel('Happiness Score')
plt.ylabel('Freedom')
plt.show()

# 행복지수가 높을수록 자유롭다고 느끼는 사람이 많음을 알 수 있다.
```


    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_60_0.png)
    


### 2. GDP per capita & Family : 0.59


```python
plt.scatter(x=alldata['GDP per capita'], y=alldata['Family'])
plt.xlabel('GDP per capita')
plt.ylabel('Family')
plt.show()

# 1인당 GDP 지수가 높을수록 가족이 많은 경우가 많음을 알 수 있다.
```


    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_62_0.png)
    


### 3. Family & Freedom : 0.42


```python
plt.xlabel('Family')
plt.ylabel('Freedom')
plt.hist(x=alldata['Family'], weights=alldata['Freedom'], bins=np.arange(0, 2, 0.1))
plt.xticks(np.arange(0, 2, 0.1)) # Extra : xticks를 올바르게 처리해봅시다.
plt.show()

# 가족이 많을수록 자유를 느끼는 사람들이 많음을 알 수 있다.
```


    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_64_0.png)
    


### 4. Healthy life expectancy & Family : 0.57


```python
sns.displot(data=alldata, x='Family', y='Healthy life expectancy')
plt.show()

# 가족이 많을수록, 건강한 삶에 대한 기대치가 높음을 알 수 있다.
```


    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_66_0.png)
    


### 5. Freedom & Perceptions of corruption : 0.46


```python
sns.jointplot(alldata['Freedom'],alldata['Perceptions of corruption'],kind="hex",size=7,ratio=3)
plt.show()

# 자유도가 높다고 해서 반드시 국가가 부패했다는 인식이 높은 것은 아니다.
# 하지만 비교적 자유도가 높을 때, 자유도가 낮을 때보다 국가가 부패했다는 비판적인 인식을 갖고 있는 사람들이 많음을 알 수 있다.
# 그리고 자유도가 높을수록 국가의 부패인식 정도가 0부터 0.5까지 넓게 분포하는 것을 통해, 
# 자유도가 높을수록 국가의 부패인식에 대해 다양한 생각을 갖고 있는 사람이 많음을 알 수 있다.
```

    /usr/local/lib/python3.9/site-packages/seaborn/_decorators.py:36: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(
    /usr/local/lib/python3.9/site-packages/seaborn/axisgrid.py:2015: UserWarning: The `size` parameter has been renamed to `height`; please update your code.
      warnings.warn(msg, UserWarning)



    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_68_1.png)
    


### 6. Freedom & Happiness Rank : -0.54


```python
sns.regplot(alldata['Freedom'],alldata['Happiness Rank'], color="g")
plt.show()
# 자유도가 높을수록 비교적 행복 순위가 떨어지는 경향을 보임을 알 수 있다.
```

    /usr/local/lib/python3.9/site-packages/seaborn/_decorators.py:36: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      warnings.warn(



    
![png](/assets/images/2020-12-18-EDA_files/2020-12-18-EDA_70_1.png)
    

