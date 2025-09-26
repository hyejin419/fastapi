import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=834369&no=31&week=tue')
time.sleep(2)
print('** 베스트 댓글 **')
xpath = '/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/section/ul/li'
best_comment_elements = driver.find_elements(By.XPATH, xpath)
for li in best_comment_elements:
    try:
        comment_p = li.find_element(By.XPATH, './div/div[2]/div/p')
        comment_text = comment_p.text.strip()
        print(comment_text)
        print('-' * 30)
    except Exception as e:
        print(e)
driver.find_element(By.XPATH, '//*[@id="wcc_root"]/section/div[4]/button[2]').click()
time.sleep(2)
print('** 전체 댓글 **')
xpath = '/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/section/ul/li'
total_comment_elements = driver.find_elements(By.XPATH, xpath)
for li in total_comment_elements:
    try:
        comment_p = li.find_element(By.XPATH, './div/div[2]/div/p')
        comment_text = comment_p.text.strip()
        print(comment_text)
        print('-' * 30)
    except Exception as e:
        print(e)



# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://example.com")

# # ID로 요소 찾기
# element = driver.find_element(By.ID, "element_id")

# # 클래스 이름으로 요소 찾기
# element = driver.find_element(By.CLASS_NAME, "class_name")

# # 태그 이름으로 여러 요소 찾기
# elements = driver.find_elements(By.TAG_NAME, "a")

# # XPath로 요소 찾기
# element = driver.find_element(By.XPATH, "//div[@id='content']")
