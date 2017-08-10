# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class PageLocators(object):
    IMAGE_1             = (By.XPATH, '/html/body/div[6]/div[1]/div/div[1]/div[3]/div[4]/div[3]/div[3]/img')
    IMAGE_2             = (By.XPATH, '/html/body/div[6]/div[1]/div/div[1]/div[3]/div[4]/div[3]/div[2]/img')
    LINK_IMAGE          = (By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div/a[5]')
    SEARCH_BOX          = (By.ID, 'text')
    SEARCH_RESULT       = (By.ID, 'suggest')
    FIRST_LINK          = (By.XPATH, '//div[@class="content__left"]/ul/li[1]/div/h2/a')
    TABLE_RESULT        = (By.CLASS_NAME, 'content__left')
    BACK                = (By.XPATH, '/html/body/div[6]/div[1]/div/div[1]/div[3]/div[4]/div[1]')
    FORWARD             = (By.XPATH, '/html/body/div[6]/div[1]/div/div[1]/div[3]/div[4]/div[2]')