import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 사용자 정보
USERNAME = 'hyejin12344'  
PASSWORD = '10041004'  
search_tag = 'food'  

# 브라우저 실행
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(5)

# 로그인
def instagram_login(username, password):
    # 입력 필드 대기 후 입력
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
    login_button.click()
    time.sleep(5)

    # 로그인 후 팝업 무시
    try:
        not_now = driver.find_element(By.XPATH, "//button[contains(text(), '나중에 하기')]")
        not_now.click()
        time.sleep(5)
    except:
        pass

# 해시태그 검색
def search_hashtag(search_tag):
    try:
        driver.get("https://www.instagram.com/")  # 다시 홈으로 이동
        time.sleep(5)

        search_button = driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a')
        search_button.click()
        time.sleep(5)

        search_input = driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/input')

        search_input.send_keys(f"#{search_tag}")
        time.sleep(2)

        first_result = driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/a[1]')
        first_result.click()
        time.sleep(10)

    except Exception as e:
        print("❌ 검색 실패:", e)


# 게시물 선택
def first_post():
    try:
        first_post = driver.find_element(By.XPATH, '//a[contains(@href, "/p/")]')
        first_post.click()
        time.sleep(5)
    except Exception as e:
        print("게시물 선택 실패: ", e)


# 좋아요, 댓글 추가
# def like_and_comment():
#     try:
#         # 좋아요 버튼 클릭
#         like_btn = driver.find_element(By.XPATH, '//section/span/button')
#         like_btn.click()
#         time.sleep(2)

#         # 댓글창 찾기 (CSS 셀렉터로 대체)
#         comment_box = driver.find_element(By.CSS_SELECTOR, 'textarea')
#         comment_box.click()
#         time.sleep(1)
#         comment_box.send_keys("안녕하세요")
#         comment_box.send_keys(Keys.ENTER)
#         time.sleep(3)

#     except Exception as e:
#         print("❌ 좋아요/댓글 실패:", e)


# 실행
instagram_login(USERNAME, PASSWORD)
search_hashtag(search_tag)
first_post()
# like_and_comment()

