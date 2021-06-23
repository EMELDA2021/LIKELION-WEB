# Repository name : LikeLion_Web_0622
### Repository Content
  * 내용 : 코로나 데이터를 통한 해석
  * 참조 코드 : 

### 소스 코드

-코로나에 대한 데이터에 대해 알아보고 파악해본다.
-데이터를 통한 현실을 바라보는 시각을 키운다.

1.코로나 실시간 보드 참조(팀)

코로나보드(https://coronaboard.kr/)

[해석:]
1.가설: 인구대비 사망자수가 낮은 나라는 어떤 대책을 가지고 있을까?(사회적거리두기, 독자적 치료방법 등)
>인구수가 적거나 사망자수가 적어 유효한 값이 나오지 않음

2.가설: 인구대비 사망자수가 높은 나라는 어떤 문제를 가지고 있을까?
>유효한 값을 가지기 위해 인구수가 우리나라보다 높은 나라 선정(28개국)
>국가별 물리적 위치에 주목(7대륙으로 분류)
>상위 랭크 국가는 유럽권, 아프리카권. 중상위 중동. 하위 아시아권. 오세아니아는 인구가 적어 포함되지 않음
>유럽권과 아프리카권은 델타변이 바이러스 이슈 발생

*참조뉴스
코로나 사투 1년반 400만명 사망…80개국 들불처럼 번지는 델타 변이 '변수'(매일경제, 2021-06-18)
https://www.mk.co.kr/news/world/view/2021/06/592393/

사망자 수가 가장 많은 나라는 미국, 브라질, 인도, 러시아, 멕시코 등으로 전세계 코로나19 사망자의 약 50%가 해당 국가에서 나왔다. 인구 대비 사망률이 가장 높은 국가는 페루, 헝가리, 보스니아, 체코 등이다.

로이터 통신은 전세계 코로나19 감염자 100명당 43명은 중남미 지역에서 발생했다고 봤다. 
지난주 코로나19 사망자 비율이 가장 높은 상위 9개 국가는 모두 라틴 아메리카였다. 볼리비아, 칠레, 우루과이에서는 25~40세 코로나19 환자가 많으며 브라질 상파울루에서는 중환자실에 있는 환자의 80%가 코로나19 감염자이다.

>델타변이 바이러스(2020년12월)발생. 발생기준으로 확진자수를 확보하고 싶었으나 데이터 확보 불가.

[결론:]
1.인구대비 사망자수가 높은 지역은 유럽과 아프리카권이다. 이유는 델타변이 바이러스의 경로때문.
2.데이터의 허수(누적값)발견. 미국과 프랑스는 초기 사망자수가 많아 누적값으로 상위권 랭크
>델타변이의 연관성을 보기 위해서는 기준에 맞은 자료확보 중요


2.뉴욕 타임즈 실시간 사이트
구글로그인필요

3.아워인데이터 사이트 참조

tip)
셀레니움에서는 페이지에 안보이는 걸 불러오기
>ActionChains 사용
>scrollY사용
for i in range(0,10):
    time.sleep(1)
    # 현재 상태에서 150만큼 쭉쭉 10번 내리기
    driver.execute_script("window.scrollTo(0, window.scrollY + 150);")

4.전제 데이터 및 기타 데이터 수집 조사 및 정리