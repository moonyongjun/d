from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 멜론 장르별 차트 (예: R&B/Soul 장르)
url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0800"
driver.get(url)
time.sleep(3)

# 곡 제목과 아티스트 추출
titles = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank01 a")
artists = driver.find_elements(By.CSS_SELECTOR, "div.ellipsis.rank02 a")

print("[R&B 인기곡 Top 5]")
for i in range(5):
    print(f"{i+1}. {titles[i].text} - {artists[i].text}")

driver.quit()