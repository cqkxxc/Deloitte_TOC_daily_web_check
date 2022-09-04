from selenium.webdriver.common.by import By
import time
from Browser import Browser


class SH_Camera:
    """
        检查上海摄像头
    """

    @staticmethod
    def check():
        """
            判断是否生成名称为今天日期的视频文件
        :return:
        """
        # 生成今天的日期
        today = time.strftime("%Y%m%d", time.localtime()) + "/"
        # 打开浏览器
        driver = Browser.open("file://cnshawins19t01/RecordFile/")
        # 获取所有日期
        date = SH_Camera.__get_all_date(driver)
        # 判断并返回结果
        return SH_Camera.__return_result(date, driver, today)

    @staticmethod
    def __return_result(date, driver, today):
        """
            遍历所有日期，判断是否产生今天日期的文件
        :param date: webdriver对象列表
        :param driver: webdriver对象
        :param today: time对象
        :return: 正常或未正常生成视频截图文件
        """
        for i in range(len(date)):
            if date[i].find_element(By.TAG_NAME, "a").text == today:
                driver.quit()
                return "正常生成视频截图文件"
        else:
            driver.quit()
            return "未正常生成截图文件!!"

    @staticmethod
    def __get_all_date(driver):
        """
            获取所有文件的名称
        :param driver: webdriver对象
        :return: webdriver对象列表
        """
        all_date = driver.find_element(By.XPATH, "/html/body/table/tbody")
        date = all_date.find_elements(By.TAG_NAME, "tr")
        return date
