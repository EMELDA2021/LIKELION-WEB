# Repository name : LikeLion_Web_0630
### Repository Content
  * 내용 : plotly 기본에 대해 실습을 통해 이해한다.
  * 참조 코드 : 캐글 노트북

### 소스 코드

-plotly에 대하여 실습을 통해 알아본다.
-타이타닉, Bike 대회를 plotly를 이용하여 시각화를 해보자.

#1. plotly 기본
 - 반응형 브라우저 기반 시각화 라이브러리(과학,그래프 툴)
 - 자료.iplot(kind='그래프종류',title='제목',xTitle='x축제목',yTitle='y축제목')
 - 그래프종류: line, scatter,bar,barh,box,surface
 
 ### cufflinks
 - cufflinks: 판다스 데이터프레임+plotly > 사용자가 판다스로부터 직접시각화
 - 자료.datagen.lines: 데이터프레임 변환
 - 테마설정: themes=cf.getThemes() > 자료.iplot(kind='',theme='')

 ### plotly express
 - 다양한 유형의 수치를 위한 30개 이상의 함수 제공
 - px.data.자료():자료 변환 > px.그래프종류(자료,x=,y=)

 ### 다중그래프 그리기
 1. make_suplots(rows=1,cols=1): 틀(레이아웃)생성
 2. add-trace
 3. update_layout 

#2. plotly를 이용하여 타이타닉 데이터 분석
 