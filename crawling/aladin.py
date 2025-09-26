import time
import re
import os
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# 이미지 저장 함수
def save_image(img_url, title, save_dir):
    try:
        response = requests.get(img_url, timeout=10)
        if response.status_code == 200:
            # 파일명에서 특수문자 제거
            safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
            file_path = os.path.join(save_dir, f"{safe_title}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)
    except Exception as e:
        print(f" 이미지 저장 실패 ({title}): {e}")

# 알라딘 크롤링 함수
def fetch_aladin(keyword, max_pages=1):
    all_data = []

    # 이미지 저장 디렉토리 생성
    save_dir = os.path.join("images", "aladin")
    os.makedirs(save_dir, exist_ok=True)

    driver = webdriver.Chrome()

    for page in range(1, max_pages + 1):
        print(f"알라딘 {page}페이지 크롤링 중...")
        url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&KeyWord={keyword}&page={page}"
        driver.get(url)
        time.sleep(2)

        book_boxes = driver.find_elements(By.CSS_SELECTOR, "div.ss_book_box")

        for box in book_boxes:
            try:
                title_element = box.find_element(By.CSS_SELECTOR, "a.bo3")
                title = title_element.text.strip()

                author = box.find_element(By.CSS_SELECTOR, "li > a[href*='AuthorSearch']").text.strip()
                publisher = box.find_element(By.CSS_SELECTOR, "li > a[href*='PublisherSearch']").text.strip()

                try:
                    li_text = box.find_element(By.CSS_SELECTOR, "li").get_attribute("innerText")
                    li_text = li_text.replace('\n', ' ').replace('\r', ' ')
                    match = re.search(r"\d{4}년\s*\d{1,2}월", li_text)
                    pub_date = match.group() if match else "출판일 없음"
                except:
                    pub_date = "출판일 없음"

                try:
                    price = box.find_element(By.CSS_SELECTOR, ".ss_p2 em").text.strip()
                except:
                    price = "가격 정보 없음"

                try:
                    img_url = box.find_element(By.CSS_SELECTOR, "img.front_cover").get_attribute("src")
                    # 이미지 저장 실행
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

            except Exception as e:
                print("오류 :", e)
                continue

    driver.quit()
    return pd.DataFrame(all_data)

# 실행 
def crawl_aladin(keyword, max_pages=1):
    df_aladin = fetch_aladin(keyword, max_pages)
    file_name = "aladin_books.csv"
    df_aladin.to_csv(file_name, index=False, encoding='utf-8-sig')
    print("알라딘 데이터가 저장되었습니다.")
    print(df_aladin.head())

# 실행
if __name__ == "__main__":
    crawl_aladin("파이썬", 3)
