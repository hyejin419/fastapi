import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl_yanolja_reviews(name, url):
    review_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    scroll_count = 3
    for i in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')  
        # 자바스크립트 문법(브라우저가 사용할 수 있는 최대의 스크롤까지 이동) 
        time.sleep(2)

    html = driver.page_source # html페이지 읽어오기
    soup = BeautifulSoup(html, 'html.parser')

    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div')
    # print(review_containers)
    review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p')

    for i in range(len(review_containers)):
        review_text = review_containers[i].find('p', class_= 'content-text').text   # 복습!
        # print(review_text)
        # print('-' * 30)
        date = review_date[i].text
        review_empty_stars = review_containers[i].find_all('path', {'fill-rule':'evenodd'}) 
        # (별점) 전체 별에서 흰색 별 찾기
        # [] : 5점
        # 코드가 길수록 흰 별이 많음. 즉 점수가 낮음
        stars = 5 - len(review_empty_stars)
        # print(review_empty_stars)
        # print('-' * 30)
        review_dict = {
            'review' : review_text,
            'stars' : stars,
            'date' : date 
        }
        review_list.append(review_dict)  # review_list라는 리스트에 review_dict라는 딕셔너리를 추가
    return review_list

total_review = crawl_yanolja_reviews('광안리 더퍼스트 효이스테이', 'https://nol.yanolja.com/reviews/domestic/10054189')
print(total_review)