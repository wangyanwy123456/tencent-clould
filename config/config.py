#!usr/bin/env python3
# _*_ coding:utf-8 _*_
import sys

sys.path.append('.')
__author__ = '1185095441@qq.com'


import sys

sys.path.append('.')
import os
from selenium.webdriver.common.by import By

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#allure报告目录
ALLURE_REPORT = os.path.join(BASE_DIR,'report/html')

#allure原始数据
ALLURE_RESULTS = os.path.join(BASE_DIR,'report/html')
