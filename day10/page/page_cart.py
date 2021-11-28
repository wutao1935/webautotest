from time import sleep

import page
from base.base import Base


class PageCart(Base):
    # 打开首页
    def page_open_index(self):
        # 注意：由于业务问题，必须暂停2秒，否则正在登录时，改变url
        sleep(2)
        self.base_index()

    # 输入搜索内容 小米手机
    def page_input_search(self, value="小米手机"):
        self.base_input(page.cart_search, value)

    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click(page.cart_search_btn)

    # 点击添加购物车 跳转到商品详情页
    def page_click_add_cart_info(self):
        self.base_click(page.cart_add_info)

    # 点击添加购物车
    def page_click_add_cart(self):
        self.base_click(page.cart_add)

    # 获取添加结果
    def page_get_text(self):
        # 切换frame表单 以name属性切换 由于电脑配置问题，导致加载比较慢 不建议使用；
        # self.base_switch_frame(page.cart_frame_name)
        # 以元素切换 推荐
        self.base_switch_frame(self.base_find(page.cart_frame_id))
        # 获取结果并返回
        return self.base_get_text(page.cart_add_result)

    # 关闭窗口
    def page_close_window(self):
        # 回到默认目录
        self.base_default_content()
        # 点击关闭操作
        self.base_click(page.cart_close_window)

    # 组合业务调用方法
    def page_add_cart(self):
        self.page_input_search()
        self.page_click_search_btn()
        self.page_click_add_cart_info()
        self.page_click_add_cart()
