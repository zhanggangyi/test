from selenium import webdriver
from selenium.webdriver.common.by import By
import json

browser = webdriver.Chrome()
url = 'https://www.11meigui.com/tools/currency#google_vignette'
browser.get(url)

res = dict()

for i in range(5):
    j = 3
    while True:
        try:
            cur_name = browser.find_element(By.XPATH, f'//*[@id="desc"]/table[{i}]/tbody/tr[{j}]/td[2]').text
            cur_name = cur_name.replace("圆", "元")

            cur_code = browser.find_element(By.XPATH, f'//*[@id="desc"]/table[{i}]/tbody/tr[{j}]/td[5]').text
            res[cur_code] = cur_name
            j = j + 1
        except:
            break

with open('table.txt', 'w') as file_to_write:
    # 进行json序列化,然后写入simple_dict.txt文件中
    json.dump(res, file_to_write)
