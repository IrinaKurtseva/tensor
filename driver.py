from unittest import TestCase

from pyvirtualdisplay import Display
from selenium import webdriver
from sys import platform
import os


class ChromeDriver(TestCase):
    def setUp(self):
        path = os.path.join(os.path.dirname(__file__))
        filename = 'chromedriver.exe' if platform.find('win') > -1 else 'chromedriver'
        driver_path = os.path.join(path, filename)
        print('Chrome driver location: %s' % driver_path)
        '''Для запуска виртульного дисплея раскомментите строки'''
        #self.display = Display(visible=0, size=(2500, 2000))
        #self.display.start()

        self.driver = webdriver.Chrome(driver_path)
        self.verificationErrors = []
        self.base_url = "https://www.yandex.ru/"
        self.driver.get(self.base_url)


    def tearDown(self):
        self.driver.quit()
        #self.display.stop()
        self.assertEqual([], self.verificationErrors)