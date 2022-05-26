from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://www.mtgstocks.com/interests"
card_keys = ["Name", "Set", "New_Price", "Old Price", "PCT"]
chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)
time.sleep(2)

table = driver.find_elements(By.XPATH, '//*[@id="wrapper"]/div/div/div/div[1]/ng-component/div[2]/div/tabset/div/tab[1]/tab-contents-component/interests-table-component[2]/table')
table_html = table[0].get_attribute('innerHTML')
soup = BeautifulSoup(table_html, "html.parser")
top_cards = soup.find_all('td')

card_dict = {}
num = 1
count = 0
card_dict[num] = {}
for i in top_cards[:50]:
    if count > 4:
        count = 0
        num += 1
        card_dict[num] = {}
    card_dict[num][card_keys[count]] = i.text
    count += 1

top_gainers_df = pd.DataFrame.from_dict(card_dict, orient="index")
top_gainers_df.to_csv("top_gainers.csv")

card_dict = {}
num = 1
count = 0
card_dict[num] = {}
for i in top_cards[-50:]:
    if count > 4:
        count = 0
        num += 1
        card_dict[num] = {}
    card_dict[num][card_keys[count]] = i.text
    count += 1
print(card_dict)
losers_df = pd.DataFrame.from_dict(card_dict, orient="index")
losers_df_reverse = losers_df.iloc[::-1]
losers_df_reverse.to_csv("top_losers.csv")
driver.close()
