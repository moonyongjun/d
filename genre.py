from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 열기
driver = webdriver.Chrome()

# 멜론 R&B/Soul 장르 페이지 열기
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0800"
driver.get(url)
time.sleep(3)  # 페이지 로딩 대기

# 곡 제목과 아티스트 추출
titles = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank01 a")
artists = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank02 a")

# 상위 5곡 출력
print("🎵 멜론 R&B/Soul 장르 TOP 5 🎵")
for i in range(5):
    print(f"{i+1}. {titles[i].text} - {artists[i].text}")

# 브라우저 닫기
driver.quit()
