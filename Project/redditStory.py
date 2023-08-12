import time, random
from bs4 import BeautifulSoup
from selenium import webdriver

"""
Scrapes subreddit of post, op's username , post's rating and comments
"""

def getPostContent(sub_reddit):
    driver = webdriver.Chrome()
    driver.get(sub_reddit)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    url = soup.findAll("shreddit-post")
    url = (url[random.randint(0, len(url))]).attrs["content-href"]
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    post = soup.find("shreddit-title").parent
    post_title = soup.find("shreddit-title").attrs["title"]
    post_author = post.findChild("shreddit-post").attrs["author"]
    post_score = int(post.findChild("shreddit-post").attrs["score"])
    comments = soup.find_all("div", id="-post-rtjson-content")
    comment_text = []
    for comment in comments:
        comment_text.append(comment.text.strip())
    return [post_title, post_author, post_score, comment_text]


sub_reddit = "https://www.reddit.com/r/AskReddit/"