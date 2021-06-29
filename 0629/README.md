# Repository name : LikeLion_Web_0629
### Repository Content
  * 내용 : pandas 기본에 대해 실습을 통해 이해한다.
  * 참조 코드 : 캐글 노트북

### 소스 코드

-folium에 대하여 실습을 통해 알아본다.
-공공데이터자료의 전처리를 통해 folium으로 시각화해본다.

#1. matplotlib의 리뷰

#2. 캘리포니아 집값 데이터
 - longitude:주택이 서쪽으로 얼마나 가야 있는지 측정한 값(값이 높을수록 더 서쪽에 있음)
 - latitude: 주택이 북쪽으로 얼마나 가야 있는지 측정한 값(값이 높을수록 더 북쪽에 있음)
 - housingMedianAge: 블록 내 주택의 연령 중앙값(값이 낮을 수록 새 건물임)
 - totalRooms: 블록 내 주택의 총 방 개수
 - totalBedrooms: 블록 내 주택의 총 침실 수
 - population: 블록 내 거주 중인 총 주민 수
 - households: 블록 내 총가구(한 세대에 거주하는 그룹) 수
 - medianIncome: 블록 내 가구의 소득 중앙값(단위: 미화 10,000달러)
 - medianHouseValue: 블록 내 가구의 주택 매매가 중앙값(단위: 미국 달러)

 - sns.pairplot(temp_train)
 - sns.pairplot(데이터프레임명)
 - 같은 변수끼리는 히스토그램으로 나타나며 나머지는 모두 산점도형태로. 따라서 선형성을 띄는 변수들은 한눈에 확인하여 상관관계 파악가능

	train['room_level']=train.room_level.astype('category')
	train.info()
 - 수치형에서 범주형(category)으로 바꾸기 > 범주형 그래프 그리기위해서
 - dtype: int62,float62,object,bool(참과거짓),datetime64(날짜와시간),category
 - .set_categories([],ordered=True):레벨의 순서정해줌
 - 카테고리에 순서에 지정하면 sorting 및 min/max는 어휘 순서 대신 논리 순서를 사용
 - .sort_values(inplace=True): 레벨의 순서 확인가능

#3. folium
 # (실습) 우리나라 지역에 50군데 데이터를 만들고, markerCluster를 이용하여 지도 시각화를 해보자.
 
 - 최서단(백령도):37.96032176746126, 124.66512390794443
 - 최동단(독도):37.24302165970547, 131.8692453591853
 - 최남단(제주도):33.42821301567277, 126.6224680746694
 - 최북단(백령도):37.96032176746126, 124.66512390794443

 - GeoJSON (지오제이슨)은 위치정보를 갖는 점을 기반으로 체계적으로 지형을 표현하기 위해 설계된 개방형 공개 표준 형식이다

#4. 공공데이터를 사용하여 우리나라 지도에 시각화 수행하기
 - url: https://www.data.go.kr/data/15043191/fileData.do
 - 국가보훈처 보훈의료 위탁병원 코로나-19 병원 정보: 보훈대상자 의료 제공 위탁병원의 코로나-19 관련 병원 운영 현황 정보
(코로나 관련 국민안심병원, 감염병전담기관, 감염병전담기관 외래진료 정보)
 1. 주소 값을 구글스프레드시트(Geocode by Awesome Table)에서 위도,경도 값 변환하여 파일로 저장
 2. 결측치 확인 후 가공 
 3. 데이터 인덱싱: 필요정보 가져오기
 4. numpy자료로 만들기
 5. Marker를 군집화 시키기 - MarkerCluster