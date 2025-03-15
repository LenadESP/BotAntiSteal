from asyncio import wait_for

from selenium import webdriver

def __main__():
    SearchList = [
        'Ordenador'
    ]

    PageList = [
        'https://es.wallapop.com/app/search?order_by=closest&keywords='
    ]

    driver = webdriver.Chrome()
    driver.get(PageList[0])
    driver.implicitly_wait(5)

__main__()