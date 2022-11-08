from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def Scroll_down(driver, scroll_down_count:int):
    modal = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fysCi']"))) #
    
    last_height = driver.execute_script("return arguments[0].scrollHeight", modal)  # 현재 스크롤 높이 가져오기
    i = 1

    while True:
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", modal)    # 스크롤 내리기
        time.sleep(1)
        driver.implicitly_wait(15)   # 최대 15초까지 대기 
        new_height = driver.execute_script("return arguments[0].scrollHeight", 'smooth', modal)   # 스크롤을 내렸을 때의 높이
        
        # 스크롤이 더 이상 내려가지 않을 때까지 내리기
        if new_height == last_height:
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight-100, 'smooth');", modal)    # 스크롤 조금 올리기
            time.sleep(3)
            driver.implicitly_wait(15)   # 최대 15초까지 대기 
        last_height = new_height    # 스크롤이 내려갔으므로 last_height 갱신
        driver.implicitly_wait(15)   # 최대 15초까지 대기 

        print('=========================='+str(i)+'번째 스크롤==========================')

        # 스크롤을 내린 횟수가 scroll_down_count와 같아지면 반복문 탈출
        if i == scroll_down_count:
            break   
        i += 1  # 스크롤을 내린 횟수 1 증가
