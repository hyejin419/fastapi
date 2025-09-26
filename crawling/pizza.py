import os
import time
from pymongo import MongoClient
from bson import Binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import Request, urlopen

# MongoDB 연결 
url = 'mongodb+srv://apple:38k8UvvUCCQJqeLJ@cluster0.jsieax5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(url)
database = client['image_db']
collection = database['pizza_images']

# 저장 폴더
folder_name = "pizza_images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

driver = webdriver.Chrome()
count = 0  # 저장 이미지 개수 초기화
max_pages = 3  # 페이지 수 설정 

for page in range(1, max_pages + 1):
    print(f"\n[페이지 {page} 크롤링 중...]")

    # 페이지별 URL 구성
    url = f'https://pixabay.com/ko/images/search/피자/?pagi={page}'
    driver.get(url)
    time.sleep(2)  # 로딩 대기

    # 이미지 요소들 수집
    image_elements = driver.find_elements(By.CSS_SELECTOR, "img[srcset]")

    for img in image_elements:
        image_url = img.get_attribute("src")
        if image_url and "https://cdn.pixabay.com" in image_url:
            try:
                req = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
                image_data = urlopen(req).read()

                # 로컬에 저장
                filename = f"pizza_{count}.jpg"
                filepath = os.path.join(folder_name, filename)
                with open(filepath, 'wb') as f:
                    f.write(image_data)
                print(f"로컬 저장됨: {filename}")

                # open(filepath, 'wb'): 해당 경로에 파일을 쓰기(write) + 바이너리(binary) 모드로 연다
                # wb: 텍스트가 아닌 이미지, 영상, 음악 등 바이너리 데이터용 모드
                # with: 파일을 자동으로 열고 닫아주는 안전한 방식
                # f.write(image_data): image_data(바이트 형식의 이미지 데이터)를 실제로 파일에 쓴다.

                # MongoDB에 저장
                document = {
                    "filename": filename,
                    "image": Binary(image_data)  #이미지 파일을 MongoDB에 이진형식으로 저장
                }
                collection.insert_one(document)
                print(f"MongoDB 저장됨: {filename}")

                count += 1

            except Exception as e:
                print(f"실패: {image_url} - {e}")

driver.quit()
print(f"\n총 {count}개의 이미지를 저장했습니다.")



