from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 자동 실행
driver = webdriver.Chrome()  # chromedriver.exe가 같은 폴더에 있어야 함

# 멜론 차트 페이지 열기
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(3)  # 로딩 대기

# 제목과 가수 가져오기
titles = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank01 a")
artists = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank02 a")

# 출력
for i in range(100):
    print(f"{i+1}위: {titles[i].text} - {artists[i].text}")

driver.quit()