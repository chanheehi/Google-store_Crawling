# 다른 .py 파일 import
from Setting import Crawling_setting
from Click_view_more_reviews import Click_view_more_reviews
from Scroll_down import Scroll_down
from Get_reviews import Get_reviews
from Save_data_mysql import Save_data_mysql
from Save_data_csv import Save_data_csv

# DB 연동, 크롬드라이버 실행, 크롤링할 url로 이동
driver = Crawling_setting()  

# 리뷰 더보기 클릭
Click_view_more_reviews(driver)

# 스크롤 내리기
scroll_down_count = 3   # 스크롤을 몇번 내리는지 설정
Scroll_down(driver, scroll_down_count)

# 각 리뷰의 정보를 크롤링
name_list, date_list, content_list, score_list = Get_reviews(driver)

# 데이터 데이터베이스로 저장
# Save_data_mysql(name_list, date_list, content_list, score_list)

# CSV로 저장
Save_data_csv(name_list, date_list, content_list, score_list)