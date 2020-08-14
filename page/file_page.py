import os, sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(os.getcwd())
from base.base_action import BaseAction
class FilePage(BaseAction):
    # 菜单
    menu_btn = By.ID, 'com.cyanogenmod.filemanager:id/ab_actions'
    # 刷新
    refresh_btn = By.XPATH, "//*[contains(@text,'刷新')]"
    # 添加到书签
    book_mark_btn = By.XPATH, "//*[contains(@text,'添加到书签')]"
    # 添加到快捷方式
    short_cut_btn = By.XPATH, "//*[contains(@text,'添加快捷方式')]"
    # set as home
    set_as_home_btn = By.XPATH, "//*[contains(@text,'Set as home')]"
    # 侧边栏
    side_menu_btn = By.ID, 'android:id/home'
    # 文件列表的标题
    dir_list_btn = By.ID, 'com.cyanogenmod.filemanager:id/navigation_view_item_name'
    # 目录imageview的特征
    path_name = By.ID, 'com.cyanogenmod.filemanager:id/breadcrumb_item'
    # 侧边栏书签的特征
    side_menu_book_mark = By.ID, 'com.cyanogenmod.filemanager:id/bookmarks_item_name'

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 点击菜单栏
    def menu_click(self):
        self.click(self.menu_btn)

    # 点击刷新
    def refresh_click(self):
        self.click(self.refresh_btn)

    # 点击添加到书签
    def mark_book_click(self):
        self.click(self.book_mark_btn)

    # 点击添加到快捷方式
    def short_cut_click(self):
        self.click(self.short_cut_btn)

    # 点击set_as_home
    def set_as_home_btn_click(self):
        self.click(self.set_as_home_btn)

    # 点击侧边栏
    def side_menu_click(self):
        self.click(self.side_menu_btn)

    # 获取当前屏幕目录列表中,第一个目录的名字
    def get_first_dir_name(self):
        dir_ele= self.find_elements(self.dir_list_btn)
        return dir_ele[0].text

    # 获取目录的最后一个名字
    def get_last_path_name(self):
        path_ele = self.find_elements(self.path_name)
        return path_ele[-1].text

    # 判断书签是否添加成功
    def get_side_menu_book_marks(self):
        book_marks = self.find_elements(self.side_menu_book_mark)
        book_mark_list = list()
        for i in book_marks:
            book_mark_list.append(i.text)
        return book_mark_list