# Repository name : LikeLion_Web_0706
### Repository Content
  * 내용 : 타이타닉 데이터 셋의 전처리 및 시각화 실습
  * 참조 코드 : 

### 소스 코드


#1. 타이타닉 sklearn-ensemble
 
 ### 머신러닝
  from sklearn.ensemble import RandomForestClassifier
  model = RandomForestClassifier()
  model.fit(X_train, y_train)
  pred = model.predict(X_test)

  sub['Survived'] = pred
  sub.to_csv("first0706_rf01.csv", index=False)

 
#2. maplotlib 활용하여 그래프 그리기(bike sharing demand)
 

#3. 팀과제 수정

https://www.notion.so/1-2-4dfc0c48aa6046c2a5ef11d3e654782c

 ### vacc per msg
 - 필요 없는 단어 빼기
  vacc_encouragement = msg_total[msg_total["msg"].str.contains("백신")]
  vacc_encouragement = vacc_encouragement.loc[~((vacc_encouragement["msg"].str.contains("백신Song")) | (vacc_encouragement["msg"].str.contains("마스크")) | (vacc_encouragement["msg"].str.contains("확진자"))) ,:]
  vacc_encouragement
 
 ### msg after 4
 - y축 값 보정하기. twinx로 통일시켜 그래프가 펌핑됨
   ax3.set_ylim(0,700)