import unittest
import pytest

# 定义测试类
from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin


class TestCart(unittest.TestCase):
    # 定义 setup
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 实例化 PageCart页面
        self.cart = PageCart(self.driver)
        # 调用成功登录 依赖
        PageLogin(self.driver).page_login_success()
        # 跳转到首页
        self.cart.page_open_index()

    # 定义 teardown
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()

    # 定义测试购物车方法
    def test_add_cart(self):
        # 调用 组合添加购物车业务方法
        self.cart.page_add_cart()
        # 断言是否添加成功
        msg = self.cart.page_get_text()
        self.assertEqual(msg, "添加成功")
        # 关闭窗口
        self.cart.page_close_window()
