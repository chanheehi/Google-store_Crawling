from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def Click_view_more_reviews(driver):
    driver.execute_script("window.scrollTo(0,1000)")     # 스크롤 내리기
    driver.implicitly_wait(5)   # 최대 5초까지 대기
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[4]/section/div/div/div[5]/div/div/button/span').click() # 리뷰 모두보기 클릭
    driver.implicitly_wait(5)
