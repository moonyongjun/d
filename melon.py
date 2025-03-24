from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 경로 설정
driver_path = "chromedriver.exe"  # Windows: chromedriver.exe / Mac: ./chromedriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# 멜론 차트 페이지 열기
url = "https://www.melon.com/chart/index.htm"
driver.get(url)

# 페이지 로딩 시간 대기
time.sleep(3)

# 프레임 전환 (멜론은 iframe 안에 차트가 있음)
# 만약 프레임 전환이 필요 없으면 아래 줄은 생략
# driver.switch_to.frame("iframe_id")  # (현재는 필요 없음)

# 곡 제목과 아티스트 가져오기
titles = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank01 a")
artists = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank02 span a")

# 출력
for i in range(100):
    print(f"{i+1}위: {titles[i].text} - {artists[i].text}")

# 드라이버 종료
driver.quit()
