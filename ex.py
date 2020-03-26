import csv
import time
from selenium import webdriver
with open('result.csv','w',encoding="utf-8") as f:
        f.write("Name , Date \n")
chrome_path=r"C:\Users\KARTHIK\Desktop\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.get("https://www.goodreads.com/book/show/136251.Harry_Potter_and_the_Deathly_Hallows");
page_count=0
for i in range(1,11):
    posts=driver.find_elements_by_class_name("user")
    time.sleep(5)
    posts_date=driver.find_elements_by_xpath('//a[@class="reviewDate createdAt right"]')
    time.sleep(5)
    with open('result.csv','a',encoding="utf-8") as f:
            for j in range(1,len(posts)):
                    f.write(posts[j].text+ "," + posts_date[j].text + "\n")
    time.sleep(10)
    page_count=page_count+1;
    if(page_count<10):
            nxt = driver.find_element_by_xpath('//a[@class="next_page"]')
            time.sleep(15)
            nxt.click()
            time.sleep(15)               
    else:
            break;
driver.close()
