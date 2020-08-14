import os, sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.file_page import FilePage

class Test_File:
    def setup(self):
        self.driver = init_driver()
        self.filepage = FilePage(self.driver)

    # 测试刷新功能是否正常
    def test_refresh(self):
        # 先获取当前屏幕目录列表中,第一个目录的名字
        name = self.filepage.get_first_dir_name()
        # 模拟屏幕中的下滑操作
        self.filepage.scroll_page_one_time('down')
        # 点击菜单栏中的刷新
        self.filepage.menu_click()
        self.filepage.refresh_click()
        # 再次获取屏幕目录列表中,第一个目录的名字,比较两次名字是否相同
        # 如果相同那么就证明刷新可用
        name2 = self.filepage.get_first_dir_name()
        print(name)
        print(name2)
        assert name == name2

    # 测试添加书签功能是否正常
    # 思路
    def test_book_mark(self):
        # 获取path的最后一个name
        name = self.filepage.get_last_path_name()
        # 点击菜单
        self.filepage.menu_click()
        # 点击添加到书签
        self.filepage.mark_book_click()
        # 点击侧边栏
        self.filepage.side_menu_click()
        # 判断书签是否添加成功
        assert name in self.filepage.get_side_menu_book_marks()

