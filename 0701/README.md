# Repository name : LikeLion_Web_0701
### Repository Content
  * 내용 : konlpy 기본에 대해 실습을 통해 이해한다.
  * 참조 코드 : 

### 소스 코드

-konly에 대하여 실습을 통해 알아본다.
-타이타닉, Bike 대회를 plotly를 이용하여 시각화를 해보자.

#1. konlpy 기본
 - 자연어처리, 토큰화, 명사추출, 불용어처리, 시각화
 
 ### 자연어처리(NLP)
 - 자연어 처리는 컴퓨터과학과 정보공학및 인공 지능의 하위분야이다.
 - 사람이 작성한 언어, 즉 텍스트를 처리하는 기술
 - 컴퓨터와 인간(자연)언어 간의 상호 작용, 특히 대량의 자연 언어 데이터를 처리하고 분석한다.
 - 컴퓨터 프로그래밍하는 방법과 관련있다. (위키 참조-Eng)

 ### 토큰화
 - 텍스트 문서를 띄어쓰기 공백과 모든 구두점을 제거하여 연속하는 단어의 열(stream of words)로 분할하는 것이다
 - nltk.Text: nltk.Text()는 문서 하나를 편리하게 탐색할 수 있는 다양한 기능을 제공
 ### 불용어처리
 - stopwords=set(STOPWORDS): 중복값 없애기
 - stop_word와 new_word로 분리하여 사용
 
 ### 워드클라우드
 - wordcloud: numpy사용

 