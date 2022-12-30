import os
from selenium import webdriver
import json

os.environ["PATH"] = r'' #selenium path
driver = webdriver.Chrome()
linkList = []
mainList = []

def doList():
    driver.get("https://www.investing.com/news/commodities-news")
    articleTable = driver.find_element_by_class_name("largeTitle")
    articles = articleTable.find_elements_by_class_name("js-article-item")
    for i in range(len(articles)):
        article = articles[i].find_element_by_tag_name("a")
        linkList.append(article.get_attribute("href"))

def run():
    for link in linkList:
        textDict = {}
        counter = 1
        driver.get(link)
        tittle = driver.find_element_by_class_name("articleHeader")
        textElements = driver.find_elements_by_xpath('//*[@id="leftColumn"]/div[3]/p')
        for index in range(len(textElements)):
            if textElements[index].text != "":
                pIndex = "p"+str(counter)
                textDict[pIndex] = textElements[index].text
                counter +=1
        article_dictionary = dict(tittle = tittle.text, link = link, text = textDict)
        mainList.append(article_dictionary)
    with open("articlesData.json", "w") as f:
        json.dump(mainList, f)
    driver.quit()

doList()
run()
