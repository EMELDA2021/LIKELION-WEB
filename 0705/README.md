# Repository name : LikeLion_Web_0705
### Repository Content
  * 내용 : 타이타닉 데이터 셋의 전처리 및 시각화 실습
  * 참조 코드 : 

### 소스 코드


#1. 타이타닉 캐글 노트북 데이터 셋의 전처리 및 시각화 실습
 
 ### 결측치 처리하기
 - .isnull().sum()
 - .value_counts()
 - .fillna()

 ### 카테고리화 하기
 - .map({'값':1,'값':2}).astype(int)
 - .replace(a,b)
 
 ### 결측치를 있는 값과 없는 값으로 넣기
 - .isna()
 
 ### 구간 기준으로 카테고리화
 - pd.concat([자료,자료],join='inner')
 - pd.qcut(자료[컬럼], 구간갯수, labels=False)
 - .iloc[행,열]
 - pd.concat([자료,자료[열],axis=1): join로 누락되었던 열 다시 넣기
 
 ### 머신러닝 돌리기
 - sklearn.tree

#2. 팀과제 중간 발표

https://www.notion.so/1-2-4dfc0c48aa6046c2a5ef11d3e654782c