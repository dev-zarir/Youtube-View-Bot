from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint
from seleniumwire import webdriver
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

def interceptor(request):
    del request.headers['Referer']
    request.headers['Referer'] = 'https://www.youtube.com/'

def launch_video(link:str):
    global URL_OPENED
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--log-level=3')
    proxy_options = {}
    if randint(1,10) > 3:
        proxy_options = {'proxy': {'http': FreeProxy(rand=True).get()}}
    driver=webdriver.Chrome(options=options, seleniumwire_options=proxy_options)
    driver.request_interceptor = interceptor
    driver.set_window_size(400, 400)
    driver.get(link + '&autoplay=1')
    sleep(60)
    driver.close()
    URL_OPENED += 1
    print(f'URL OPENED: {URL_OPENED} times')

link=sys.argv[1]
while True:
    for i in range(6):
        t = Thread(target=lambda: launch_video(link))
        t.daemon = True
        t.start()
    sleep(60 + 10)
    ROUND += 1
    print(f'ROUND: {ROUND} times')


