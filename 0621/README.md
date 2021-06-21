# Repository name : LikeLion_Web_0621
### Repository Content
  * 내용 : amazon 크롤링
  * 참조 코드 : 

### 소스 코드

-쇼핑몰을 검색하고 정보를 가져오는 것을 실습을 통해 알아본다.
-페이지를 이동하여 리뷰를 가져와보기

1.쇼핑몰 데이터 가져오기-리뷰

아마존: kimchi powder
https://www.amazon.com/SEC-KIMCHI-Korean-Kimchi-Seasoning/dp/B07RH7FN4Z/ref=sr_1_1?crid=18WA1TL8YLC45&dchild=1&keywords=kimchi+powder&qid=1624255100&sprefix=kimchi%2Caps%2C331&sr=8-1

하나의 제품 여러 페이지 리뷰 정보 가져오기 실습해 보기
추가 정보 가져오기(사용자 이름) 
추가 정보 가져오기(평점)
추가 정보 가져오기(날짜)
지역 정보 추가, 몇 명에게 더 도움이 되었다.

아마존 상품을 하나 선정한 이후에 리뷰 및 기타를 가져와서 정리해 보자.(csv, xlsx파일 등). github 올리고 github 코드 공유하기

bs4로 빠르게 찾아오기
셀레니움으로 동적움직임 활용


all_user=[]
all_ratings=[]
all_date=[]
all_location=[]
all_help=[]
all_review=[]

for page in range(2,7,1):
    time.sleep(3)
    
    page=driver.page_source
    soup=BeautifulSoup(page,'html.parser')
    all_r1=soup.find_all('div',class_='a-section celwidget')
    
    for one in all_r1:
        user_one=one.find('span',class_='a-profile-name').text
        all_user.append(user_one)

        rate_one=one.find('span',class_='a-icon-alt').text[0:3]
        all_ratings.append(rate_one)

        info_one=one.find('span',class_='a-size-base a-color-secondary review-date').text.lstrip("Reviewd in ").split(" on ")
        all_date.append(info_one[-1])
        all_location.append(info_one[0])    

        try:
            help_one=one.find('span',class_='a-size-base a-color-tertiary cr-vote-text').text
        except:
            help_one='0'
        all_help.append(help_one)
    
        tmp = one.text
        review = tmp.replace("\n", "")
        all_review.append(review)
    
    print('user:',all_user[-1],'rating:',all_ratings[-1])
    print('review:',all_review[-1],end='\n\n\n')

    sel_next = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
    sel_next.click()

print(len(all_user))
print(len(all_ratings))
print(len(all_date))
print(len(all_location))
print(len(all_help))
print(len(all_review))


dat_review1={'user':all_user,'ratings':all_ratings,'date':all_date,
            'location':all_location,'help':all_help,
            'review':all_review}