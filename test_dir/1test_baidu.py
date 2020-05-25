"""
@author:  虫师
@data: 2019-10-17
@function python 基本用法
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))  #os.path.dirname可以获取到除文件名以外的路径，我们使用2次，就可以得到父父级目录，现在我们获得了父父级目录，我们把目录加到 sys.path去
from page.baidu_page import BaiduPage


'''
获取路径名：os.path.dirname()

获取文件所在目录的完整路径：os.path.dirname(__file__)

os.path.abspath(__file__)返回的是.py文件的绝对路径
'''
global driver

class TestSearch:
    """百度搜索"""

    def test_baidu_search_case(self, browser, base_url):
        """
        名称：百度搜索"pytest"
        步骤：
        1、打开浏览器
        2、输入"pytest"关键字
        3、点击搜索按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input = "pytest"
        page.search_button.click()
        sleep(2)
        assert browser.title == "pytest_百度搜索"


# class TestSearchSettings:
#     """百度搜索设置"""
#
#     def test_baidu_search_setting(self, browser, base_url):
#         """
#         名称：百度搜索设置
#         步骤：
#         1、打开百度浏览器
#         2、点击设置链接
#         3、在下拉框中"选择搜索"
#         4、点击"保存设置"
#         5、对弹出警告框保存
#         检查点：
#         * 检查是否弹出提示框
#         """
#         page = BaiduPage(browser)
#         page.get(base_url)
#         page.settings.click()
#         page.search_setting.click()
#         sleep(2)
#         page.save_setting.click()
#
#         alert_text = page.get_alert_text
#         page.accept_alert()
#         assert alert_text == "已经记录下您的使用偏好"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_baidu.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
