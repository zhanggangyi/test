import json
import sys
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 读取命令行参数
date = sys.argv[1]
# 将字符串转换为日期时间对象
try:
    date_obj = datetime.datetime.strptime(date, "%Y%m%d")
except:
    print("时间输入格式错误")
    exit(0)
date = date_obj.strftime("%Y-%m-%d")

# 读取货币代码-货币名对照表
current_type = sys.argv[2]
with open('table.txt', 'r') as file_to_read:
    table = json.load(file_to_read)
    current_type = table[current_type]

browser = webdriver.Chrome()
url = 'https://www.boc.cn/sourcedb/whpj/'
browser.get(url)

# 输入查询框的时间
input_box1 = browser.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[2]/div/input')
input_box1.clear()
input_box1.send_keys(date)
input_box2 = browser.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[4]/div/input')
input_box2.clear()
input_box2.send_keys(date)

try:
    # 输入货币类型
    select_box = Select(browser.find_element(By.XPATH, '//*[@id="pjname"]'))
    select_box.select_by_value(current_type)
except:
    print("不支持的货币代码")
    exit(0)

# 点击查询
btn = browser.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[7]/input')
btn.click()

try:
    # 获取第一条数据
    price = browser.find_element(By.XPATH, '/html/body/div/div[4]/table/tbody/tr[2]/td[4]').text
    print(price)

    # 写入文件
    file = open("result.txt", "w")
    file.write(price)
    file.close()
except:
    print("没有当日数据")
    exit(0)


