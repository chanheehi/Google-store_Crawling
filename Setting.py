from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pymysql

def Crawling_setting():
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='review_data', charset='utf8mb4') #SQL 연동
    cursor = db.cursor()   #SQL 연동
    cursor.execute("USE review_data")   #review_data DB 사용
    target_url = 'https://play.google.com/store/apps/details?id=com.sampleapp&hl=ko'    # 크롤링할 url

    heandlessoptions = webdriver.ChromeOptions()    # 크롬 옵션 설정
    heandlessoptions.add_argument('headless')   # 크롬 옵션 설정
    driverPath = "./chromedriver.exe" # 크롬드라이버 설치된 경로. 파이썬(.py) 저장 경로와 동일하면 그냥 파일명만
    driver = webdriver.Chrome(ChromeDriverManager().install()) # 크롬드라이버 실행  , options=heandlessoptions
    driver.get(target_url)      # 크롤링할 url로 이동

    return driver