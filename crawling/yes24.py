import time
import os
import re
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# 이미지 저장 함수
def save_image(img_url, title, save_dir):
    try:
        response = requests.get(img_url, timeout=10)
        if response.status_code == 200:
            # 파일명에 사용할 수 없는 문자 제거
            safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
            file_path = os.path.join(save_dir, f"{safe_title}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)
    except Exception as e:
        print(f"이미지 저장 실패 ({title}): {e}")

# 예스24 크롤링 함수 
def fetch_yes24(keyword, max_pages=1):
    all_data = []

    # 이미지 저장 디렉토리 생성
    save_dir = os.path.join("images", "yes24")
    os.makedirs(save_dir, exist_ok=True)

    driver = webdriver.Chrome()

    for page in range(1, max_pages + 1):
        print(f"예스24 {page}페이지 크롤링 중...")
        url = f'https://www.yes24.com/Product/Search?domain=ALL&query={keyword}&page={page}'
        driver.get(url)
        time.sleep(2)

        items = driver.find_elements(By.CSS_SELECTOR, "#yesSchList > li")

        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, ".info_row.info_name").text.strip()
                author = item.find_element(By.CSS_SELECTOR, ".info_pubGrp .info_auth").text.strip()
                price = item.find_element(By.CSS_SELECTOR, ".info_row.info_price").text.strip()
                publisher = item.find_element(By.CSS_SELECTOR, ".info_pubGrp .info_pub").text.strip()
                pub_date = item.find_element(By.CSS_SELECTOR, ".info_pubGrp .info_date").text.strip()

                # 이미지 URL 추출 및 저장
                try:
                    img_url = item.find_element(By.CSS_SELECTOR, ".item_img img").get_attribute("src")
                    save_image(img_url, title, save_dir)
                except:
                    img_url = "이미지 없음"

                all_data.append({
                    '검색어': keyword,
                    '제목': title,
                    '저자': author,
                    '가격': price,
                    '출판사': publisher,
                    '출판일': pub_date,
                    '이미지': img_url
                })

            except:
                continue

    driver.quit()
    return pd.DataFrame(all_data)

# 실행 함수
def crawl_yes24(keyword, max_pages=1):
    df_yes24 = fetch_yes24(keyword, max_pages)
    file_name = "yes24_books.csv"
    df_yes24.to_csv(file_name, index=False, encoding='utf-8-sig')
    print("예스24 데이터가 저장되었습니다.")
    print(df_yes24.head())

# 실행
if __name__ == "__main__":
    crawl_yes24('파이썬', 3)
