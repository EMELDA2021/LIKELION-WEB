# Repository name : LikeLion_Web_0623
### Repository Content
  * 내용 : 코로나 데이터를 통한 해석
  * 참조 코드 : 캐글노트북(타이타닉)

### 소스 코드

-matplitlib에 대하여 실습을 통해 알아본다.
-seaborn에 대해 실습을 통해 알아본다.

#1. seaborn의 기본 실습

*그래프별 특징확인
 - sns.boxplot
 - sns.barplot
 - sns.lmplot
 - sns.relplot
 - sns.jointplot
 - sns.scatterplot
 - sns.heatmap
 - sns.pairplot
 - sns.countplot

*데이터 확인 함수
 - data.shape
 - data.columns
 - data.info()
 - data.describe()
 - data.dtype
 - data.corr()

tip).describe()
 - 숫자형 자료의 경우 결과값의 index(좌측)은 개수, 평균, 표준편차, 최소, 최대,  lower, upper, 50% 가 리턴된다.
 - Object 자료, 예를 들어 문자열, 타임스탬프(시간)은 개수, unique (용어를 모르는데 중복을 제외한 값들의 개수?), 최빈값과, 그 값의 빈도를 보여준다.
 - 위의 둘이 섞여있는 경우는 숫자로만 되어있는 열(column)만 분석해서 알려준다고 되어있네요.

#2. 타이타닉(캐글)

자료를 보고 가설세우기

질문)왜 생존자가 Pclass에 따라 달라지는가?
가설)
1.혹시 1등급은 여성이 많아서 그런 것은 아닐까? (남성이 더 많다. 이 가설은 생각을 해보자.)
2.남성이 구조에 후 순위에 있었다. 3등급은 남성이 많기 때문에 ... ( 어느 정도 맞는 것 같다.)
3.Pclass별 나이를 확인해 봐야 하는데...
  -- 나이가 많은 분들이 많이 구조된 것 같다.
  -- 나이가 적은 사람들은 1등급에 별로 없다.
>생존에 영향을 끼치는 요소 - Age, Pclass

4.남성이 구조에 후 순위에 있었다. 3등급은 남성이 많기 때문에 ... ( 어느 정도 맞는 것 같다.)
5.Embarked가 어떤 영향을 끼쳤는지?
6.Fare가 히스토그램을 찍어보고 분포를 확인해 보기. Fare가 생존에 영향을 끼칠까요?

#3. 실습 프로젝트(팀)
자료변경:코로나 누적 데이터 확보
https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv

필요값만 추출(판다스)
covid_data_filtered = covid_data_after_2021[["continent", "location", "date", "total_cases", "new_cases", "total_deaths", "new_deaths_smoothed" ,"hosp_patients","positive_rate","new_vaccinations_smoothed","population","reproduction_rate"]]

추출한 콜롬으로 비교값 그래프화
활용값:new_cases_smoothed, new_deaths_smoothed, reproduction_rate
