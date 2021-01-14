## r=requests.get("https://newyork.craigslist.org/d/jobs/search/jjj")
## r.status_code
## print(r)
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Sardor/Documents/Softwares/Chrome WebDriver/chromedriver.exe')

driver.get("https://oxylabs.io/blog")
results = []
results_2 = []
content = driver.page_source
#easily readable format
soup = BeautifulSoup(content, features="html.parser")
driver.quit()

for x in soup.findAll(attrs='blog-card_content-wrapper'):
    name = x.find('h2')
    if name in results:
        #keeps adding to the list
        results.append(name.text)
for y in soup.findAll(attrs='blog-card__user-info__name'):
    by = y.find('p')
    if by in results:
        results.append(by.text)

df = pd.DataFrame({'Names': results, 'Author': results_2})
df.to_csv('names_2.csv', index=False, encoding='utf-8')