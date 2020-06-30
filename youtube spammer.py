from selenium import webdriver
from time import sleep
import pyautogui
import time
import random
from pas import uname, pw
from selenium.webdriver.common.keys import Keys


def log_in():
    global driver
    driver = webdriver.Chrome()
    driver.get(
        "https://accounts.google.com/signin/oauth/identifier?client_id=1096011445005-sdea0nf5jvj14eia93icpttv27cidkvk.apps.googleusercontent.com&response_type=token&redirect_uri=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F&state=%7B%22client_id%22%3A%221096011445005-sdea0nf5jvj14eia93icpttv27cidkvk.apps.googleusercontent.com%22%2C%22network%22%3A%22google%22%2C%22display%22%3A%22popup%22%2C%22callback%22%3A%22_hellojs_amey6eoy%22%2C%22state%22%3A%22%22%2C%22redirect_uri%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%22%2C%22scope%22%3A%22basic%22%7D&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fplus.me%20profile&approval_prompt=force&o2v=1&as=qmOFLz7H8JITnWIBhV2KEw&flowName=GeneralOAuthFlow")
    driver.maximize_window()
    email = driver.find_element_by_xpath("//*[@id=\"identifierId\"]")
    email.click()
    email.send_keys("Put username here")
    time.sleep(1)

    submit_button = driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/span/span")
    submit_button.click()
    time.sleep(2)

    password = driver.find_element_by_xpath("//*[@id=\"password\"]/div[1]/div/div[1]/input")
    password.click()
    password.send_keys("Put your password here")
    time.sleep(1)

    next_button = driver.find_element_by_xpath("//*[@id=\"passwordNext\"]/span/span")
    next_button.click()
    time.sleep(2)

    driver.get("https://www.youtube.com/results?search_query=nelk&sp=EgIQAQ%253D%253D")
    time.sleep(3)


def youtube():
    item = driver.find_element_by_css_selector("ytd-search a#video-title")
    item.click()
    time.sleep(2)


def youtube_comment_bot():
    driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(2)
    if driver.find_element_by_id("simplebox-placeholder"):
        comment_box = driver.find_element_by_id("simplebox-placeholder")
        comment_box.click()
        time.sleep(2)
    else:
        next_video()
    if driver.find_element_by_id('contenteditable-root'):
        input_box = driver.find_element_by_id('contenteditable-root')
        f = " "
        send = "https://www.youtube.com/watch?v=ktxh1fIHL_Y" + f + "Free XBOX LIVE GIFTCARDS AT END OF VIDEO" + "FLIGHT TEAM STAND UP DOC"
        input_box.send_keys(send)
        youtube_submit = driver.find_element_by_id("submit-button")
        youtube_submit.click()
        driver.execute_script("window.scrollTo(0, -800)")
        time.sleep(2)
    else:
        next_video()


def next_video():
    next_vid = driver.find_element_by_xpath('//*[@class="ytp-next-button ytp-button"]')
    next_vid.click()
    time.sleep(2)


log_in()
youtube()

while True:
    youtube_comment_bot()
    next_video()
