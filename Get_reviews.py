from bs4 import BeautifulSoup
from datetime import datetime

def Get_reviews(driver):
    html_source = driver.page_source    # 현재 페이지의 html 소스 가져오기
    soup_source = BeautifulSoup(html_source, 'html.parser') # html 파싱
    review_source = soup_source.find_all(class_ = 'RHo1pe') # 각 리뷰

    i = 0   # 리뷰의 개수
    name_list, date_list, content_list, score_list = [], [], [], [] # 크롤링한 데이터를 저장할 리스트

    for review in review_source:    # 각 리뷰의 정보를 크롤링
        i = i+1 # 리뷰의 개수   # 리뷰의 개수
        name = review.find_all(class_ = 'X5PpBb')[0].text.replace("'", " ").replace('"', " ")   # 리뷰 작성자
        date = review.find_all(class_ = 'bp9Aid')[0].text   # 리뷰 작성일
        date = datetime.strptime(date, '%Y년 %m월 %d일')    # 날짜 형식을 datetime으로 변환
        date = date.strftime('%Y%m%d')  # 날짜 형식을 YYYYMMDD로 변경
        content = review.find_all(class_ = 'h3YV2d')[0].text.replace("'", " ").replace('"', ' ')    # 리뷰 내용
        score1 = rating = review.find_all(class_ = "iXRFPc")[0]['aria-label'][10]   # 별점
        score = score1.replace('별표 5개 만점에 ', '').replace('개를 받았습니다.', '')  # 별점
        
        # 리스트에 각자 데이터 추가
        name_list.append(name) 
        date_list.append(date)  
        content_list.append(content)
        score_list.append(score)
        print('==================='+str(i)+'번째, 데이터 파싱================')

    return name_list, date_list, content_list, score_list   # 크롤링한 데이터를 반환