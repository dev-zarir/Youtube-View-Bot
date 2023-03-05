from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint
from selenium import webdriver
from threading import Thread
from fp.fp import FreeProxy
from time import sleep
import sys

dop = print
URL_OPENED = 0
ROUND = 0

def print(*args, **kwargs):
    kwargs['flush'] = True
    dop(*args, **kwargs)

def launch_video(link:str):
    global URL_OPENED
    options = webdriver.ChromeOptions()
    if randint(1,10) > 3:
        options.add_argument("--proxy-server=" + FreeProxy(rand=True).get())
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
    driver=webdriver.Chrome(options=options)
    driver.set_window_size(400, 400)
    driver.get(link)
    try:
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Play"]'))).click()
    except: pass
    sleep(60)
    driver.close()
    URL_OPENED += 1
    print(f'URL OPENED: {URL_OPENED} times')

link=sys.argv[1]
while True:
    for i in range(6):
        t = Thread(target=lambda: launch_video(link))
        t.setDaemon(True)
        t.start()
    sleep(60 + 10)
    ROUND += 1
    print(f'ROUND: {ROUND} times')


