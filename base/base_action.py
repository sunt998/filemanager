from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click(self,loc):
        ele = self.find_element(loc)
        ele.click()

    def input_text(self,loc,text):
        ele = self.find_element(loc)
        ele.send_keys(text)

    def find_elements(self, loc, timeout=5.0, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_elements(loc[0], loc[1]))

    def find_element(self, loc, timeout=5.0, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_element(loc[0], loc[1]))

    def screenshot(self,filename):
        self.driver.get_screenshot_as_file("./screen/"+filename+".png")

    # 模拟滑动手机屏幕,一次滑一页
    def scroll_page_one_time(self, direction='down'):
        window_size = self.driver.get_window_size()
        window_height = window_size['height']
        window_width = window_size['width']
        up_y = window_height*0.25
        down_y = up_y*3
        left_x = window_width*0.25
        right_x = left_x * 3
        center_x = window_width * 0.5
        center_y = window_height * 0.5
        if direction == 'down':
            # 由下向上滑一页
            self.driver.swipe(center_x,down_y,center_x,up_y)
        elif direction == 'up':
            # 由上向下滑一页
            self.driver.swipe(center_x,up_y,center_x,down_y)
        elif direction == 'left':
            # 由左向右滑一页
            self.driver.swipe(left_x,center_y,right_x,center_y)
        elif direction == 'right':
            # 由右向左滑一页
            self.driver.swipe(right_x,center_y,left_x,center_y)
        else:
            raise Exception('请输入正确的direction参数 down、up、left、right')




