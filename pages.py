# -*- coding: utf-8 -*-
import os
import time
from sys import platform

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from base import Page
from locators import *


class SearchPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.window_handles = None

    def check_page_loaded(self):
        return True if self.find_element(*PageLocators.LOGO) else False

    def check_search_box(self):
        self.is_element_present(*PageLocators.SEARCH_BOX)

    def enter_tensor_in_search_box(self, text):
        self.find_element(*PageLocators.SEARCH_BOX).send_keys(text)

    def check_search_result(self):
        self.is_element_present(*PageLocators.SEARCH_RESULT)

    def button_enter_and_check(self):
        self.find_element(*PageLocators.SEARCH_BOX).send_keys(Keys.ENTER)
        self.is_element_present(*PageLocators.TABLE_RESULT)

    def click_first_link(self):
        self.click_element(*PageLocators.FIRST_LINK)

    def check_link_image(self):
        self.is_element_present(*PageLocators.LINK_IMAGE)

    def click_link_image(self):
        self.click_element(*PageLocators.LINK_IMAGE)

    def get_attr_image_1(self, attr):
        element = self.find_element(*PageLocators.IMAGE_1).get_attribute(attr)
        return element

    def get_attr_image_2(self, attr):
        element = self.find_element(*PageLocators.IMAGE_2).get_attribute(attr)
        return element

    def click_back(self):
        self.wait_for_visible_and_click(PageLocators.BACK)

    def click_forward(self):
        self.wait_for_visible_and_click(PageLocators.FORWARD)