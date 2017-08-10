# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

from pages import *
from driver import ChromeDriver

class TestPages(ChromeDriver):

    def setUp(self):
        super(TestPages, self).setUp()


    def test_search_site_tensor(self):
        '''Поиск в Яндексе
        1) Зайти на yandex.ru
        2) Проверить наличия поля поиска
        3) Ввести в поиск Тензор
        4) Проверить, что появилась таблица с подсказками (suggest)
        5) При нажатии Enter появляется таблица результатов поиска
        # 6)  1 ссылка ведет на сайт tensor.ru'''
        page = SearchPage(self.driver)
        self.driver.get(self.base_url)
        page.check_search_box() #
        page.enter_tensor_in_search_box(text=u'Тензор')
        page.check_search_result()
        page.button_enter_and_check()
        page.click_first_link()
        page.switch_tabs()
        self.assertEqual("https://tensor.ru/", page.get_url())

    def test_image(self):
        '''Картинки на яндексе
        1) Зайти на yandex.ru
        2) Ссылка «Картинки» присутствует на странице
        3) Кликаем на ссылку
        4) Перешли на url https://yandex.ru/images/
        5) При нажатии кнопки назад меняется картинка
        6) При нажатии кнопки вперед  картинка меняется на ту, что была на шаге'''
        page = SearchPage(self.driver)
        self.driver.get(self.base_url)
        page.check_link_image()
        page.click_link_image()
        time.sleep(5)
        attr_image1 = page.get_attr_image_1(attr='src')
        page.click_back()
        attr_image2 = page.get_attr_image_2(attr='src')
        if attr_image1 != attr_image2:
            page.click_forward()
            attr_image3 = (page.get_attr_image_1(attr='src'))
            self.assertEqual(attr_image1, attr_image3)

    def tearDown(self):
        super(TestPages,self).tearDown()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
