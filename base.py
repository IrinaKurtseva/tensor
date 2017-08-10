# -*- coding: utf-8 -*-
import datetime
import os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    wait_for_timeout = 10
    waiter = None

    def __init__(self, driver):
        base_url = 'https://www.yandex.ru/'
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.verificationErrors = []
        self.accept_next_alert = True

    def is_element_present(self, *locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False


    def find_element_by_xpath(self, *locator):
        return self.driver.find_element(*locator)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def clear_element(self, *locator):
        return self.find_element(*locator).clear()

    def click_element(self, *locator):
        return self.find_element(*locator).click()



    def open(self, url):
        url = self.base_url + url
        return self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def switch_tabs(self, *locator):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()


    def wait_for_visible_and_click(self, locator):
        try:
            element = WebDriverWait(self.driver, 100).until(
                EC.element_to_be_clickable(locator))
            return element.click()
        except TimeoutException:
            raise Exception('Never saw element %s become visible' % (locator))

