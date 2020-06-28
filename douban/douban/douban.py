import logging
import time
import numpy as np
from douban.settings import *
import cv2
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium import webdriver
verify_url = 'https://www.douban.com/'
# headers={
#     'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
#
# }
# response=requests.get(url,headers=headers)
# print(response.status_code)
# driver=webdriver.Chrome()
# wait=WebDriverWait(driver,15)
# driver.get(url)
# driver.switch_to_frame(0)
# diot=driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
# diot.click()
# username=driver.find_element_by_id('username')
# username.send_keys('1549181296@qq.com')
# password=driver.find_element_by_id('password')
# password.send_keys('714823812words')
#
# buttom=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a')
# # buttom=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.account-body.login-wrap.login-start.account-anonymous > div.account-tabcon-start > div.account-form > div.account-form-field-submit > a')))
# buttom.click()
# driver.implicitly_wait(5)
#
#
# frame=driver.find_element_by_xpath('//*[@id="TCaptcha"]/iframe')
# driver.switch_to_frame(frame)
# # time.sleep(10)
# # driver.switch_to_frame(0)
# print(driver.page_source)
#
#
#
# # driver.switch_to_frame()
# s=driver.find_element_by_id('slideBkg').get_attribute('src')
# # s=driver.find_element_by_id('slideBkg')
# print(s)
# # driver.switch_to_default_content()
def get_distance():
    bkg = cv2.imread('bkg.png', 0)
    block = cv2.imread('block.png', 0)
    cv2.imwrite('template.jpg', bkg)
    cv2.imwrite('block.jpg', block)
    block = cv2.imread('block.jpg', 0)
    block = cv2.cvtColor(block, cv2.COLOR_BAYER_BG2GRAY)
    block = abs(255 - block)
    cv2.imwrite('block.jpg', block)
    block = cv2.imread('block.jpg')
    template = cv2.imread('template.jpg')
    result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    y = y/2-60
    print(y)
    return y, template


def get_track(distance):

    mid = distance* 4/5
    v = 0
    t = 0.3
    tracks = []
    current = 0
    while current <= distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0 * t + 0.5 * a * t * t
        current += s

        tracks.append(round(s))
        v = v0 + a * t
    return tracks


def run(url):
    slideblock=0
    slidebkg=0
    mycookie = {}
    if url==verify_url:
        driver = webdriver.Chrome()


        driver.get(url)

        driver.switch_to_frame(0)
        diot = driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
        diot.click()
        username = driver.find_element_by_id('username')
        username.send_keys(USERNAME)
        password = driver.find_element_by_id('password')
        password.send_keys(PASSWORD)
        buttom = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a')
        buttom.click()

        driver.implicitly_wait(5)
        try:
            frame =driver.find_element_by_xpath('//*[@id="TCaptcha"]/iframe')
            driver.switch_to_frame(frame)

            slidebkg = driver.find_element_by_id('slideBkg').get_attribute('src')
            slideblock = driver.find_element_by_id('slideBlock').get_attribute('src')

            time.sleep(1)
        except Exception as e:
            pass
        if slideblock and slidebkg:

            Bkg = requests.get(slidebkg)
            Block = requests.get(slideblock)

            with open('bkg.png', 'wb') as f:
                f.write(Bkg.content)
            with open('block.png', 'wb') as f:
                f.write(Block.content)

            distance, template = get_distance()
            tracks = get_track(distance)

            block = driver.find_element_by_id('tcaptcha_drag_thumb')



            ActionChains(driver).click_and_hold(on_element=block).perform()
            for track in tracks:
                ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()

            ActionChains(driver).release(on_element=block).perform()

            time.sleep(0.2)
        cookies=driver.get_cookies()

        for cookie in cookies:
            mycookie[cookie['name']]=cookie['value']
        print(mycookie)
        print(cookies)
        return mycookie
if __name__ == '__main__':
    run(verify_url)


