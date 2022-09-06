from selenium import webdriver


class Browser:
    """
        打开浏览器并设置各种参数
    """

    @staticmethod
    def open(url):
        # 设置终端不打印DevTools信息
        option = webdriver.EdgeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        # 打开浏览器并自动最大化
        driver = webdriver.Edge(options=option)
        driver.maximize_window()
        # 设置全局等待元素时间为10秒
        driver.implicitly_wait(10)
        # 进入检查页面
        driver.get(url)

        return driver
