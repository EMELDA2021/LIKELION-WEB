# Repository name : LikeLion_Web_0628
### Repository Content
  * 내용 : pandas 기본에 대해 실습을 통해 이해한다.
  * 참조 코드 : 캐글 노트북

### 소스 코드

-pandas에 대하여 실습을 통해 알아본다.
-실제 데이터 셋의 전처리를 통해 pandas 데이터 전처리를 이해한다.

#1. pandas의 기본
 - 판다스 핵심자료구조:Series(1차원,리스트), DataFrame(2차원.딕셔너리)
 - 데이터 인덱싱: loc(컬럼명으로 추출), iloc(데이터 순서로 추출)
 - 값의 정렬: 데이터.sort_values(ascending=False) 내림차순 정렬
 - 결측치 확인: .dropna(subset=['컬럼명',...]) subset의 해당컬럼에 빈값 있다면 행삭제 .fillna({'컬럼명':값,...}) 빈값채우기
 - 열삭제: .drop(['컬럼명',...])
 - 데이터 자료형 변환: 데이터.astype(변환될 자료형명)
 - 문자>숫자,숫자>문자: 데이터.map({'문자':0,...}) 데이터.replace({'문자':0,....})
 - crosstap(): 특정 데이터 그룹에 대한 빈도수
 - groupby: 데이터를 그룹화. index를 dict로 표현
#2. 캘리포니아 집값 데이터

#3. 타이타닉 데이터 셋 실전 데이터 처리
 - 결정트리
 - from sklearn.tree import DecisionTreeClassifieer
 - 머신러닝:모델객체 만들기 > 모델 훈련시키기 > 훈련시킨 모델로 예측하기
 1. 모델객체 만들기
 tree=DecisionTreeClassifieer
 2. 모델 훈련시키기
 tree.fit(X-train,y-train)
 3. 훈련시킨 모델로 예측하기
 pred=tree.predict(X-test)

