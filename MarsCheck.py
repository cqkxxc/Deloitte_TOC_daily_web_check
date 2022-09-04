from selenium.webdriver.common.by import By

from Browser import Browser


class Mars:
    """
    检查Mars的TRAVEL & EXPENSE和Timesheet模块是否正常运行，通过页面元素是否正常加载进行判断
    """
    result = ""

    @staticmethod
    def check():
        """
            检查TRAVEL & EXPENSE和Timesheet模块
        :return: str,拼接TRAVEL & EXPENSE和Timesheet的检查结果
        """
        driver = Browser.open("https://mars.deloitte.com.cn/mars-platform-web/s")
        # 接受cookie
        driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[2]").click()
        # 检查TRAVEL & EXPENSE
        windows = Mars.check_travel_expense(driver)
        # 切换回首页
        driver.switch_to.window(windows[0])
        # 检查Timesheet
        Mars.check_timesheet(driver)
        # 关闭浏览器
        driver.quit()
        # 返回检查结果
        return Mars.result

    @staticmethod
    def check_timesheet(driver):
        """
            检查Timesheet
        :param driver: selenium的webdriver对象
        :return: str,Timesheet正常或异常
        """
        # 点击Timesheet
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div/img").click()
        # 获取所有标签页标识
        windows = driver.window_handles
        # 切换到新标签页Timesheet
        driver.switch_to.window(windows[1])
        if driver.find_element(By.ID, "iframepage").is_displayed():
            Mars.result += "Timesheet正常"
            driver.close()
        else:
            Mars.result += "Timesheet异常!!!"
            driver.close()

    @staticmethod
    def check_travel_expense(driver):
        """
            检查TRAVEL & EXPENSE
        :param driver: selenium的webdriver对象
        :return: str,TRAVEL & EXPENSE正常或异常
        """
        # 点击TRAVEL & EXPENSE
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/img").click()
        # 获取所有标签页标识
        windows = driver.window_handles
        # 切换到新标签页TRAVEL & EXPENSE
        driver.switch_to.window(windows[1])
        if driver.find_element(By.ID, "iframepage").is_displayed():
            Mars.result += "TRAVEL & EXPENSE正常,"
            driver.close()
        else:
            Mars.result += "TRAVEL & EXPENSE异常!!!,"
            driver.close()
        return windows
