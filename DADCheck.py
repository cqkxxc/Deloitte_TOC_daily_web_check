# "https://auditqualityhk.cn.deloitte.cn/",
# "https://auditqualityprc.cn.deloitte.cn/",
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Browser import Browser


class DAD:

    @staticmethod
    def check():
        """
            检查两个AUDITONLINE平台的数据同步日期
        :return str, 返回两个平台的数据同步日期
        """
        result = ""

        dad_dict = {"hk节点": "https://auditqualityhk.cn.deloitte.cn/",
                    "prc节点": "https://auditqualityprc.cn.deloitte.cn/"}

        for site in dad_dict:
            driver = Browser.open(dad_dict[site])
            result = DAD.get_date_time(driver, result, site)
            driver.quit()

        # driver = Browser.open("https://auditqualityprc.cn.deloitte.cn/")
        # result = DAD.get_date_time(driver, result)
        # driver.quit()
        return result

    @staticmethod
    def get_date_time(driver, result, site):
        sleep(10)
        driver.find_element(By.LINK_TEXT, "Audit Quality Milestones").click()
        sleep(5)
        try:
            result += "%s同步时间 %s\n" % (site, driver.find_element(By.XPATH,
                                                                "/html/body/app-root/div/div[2]/div/ng-component/div/app-subheader/div[1]/div[4]").text)
            return result
        except Exception:
            return "Quality Dashboard 检查异常，请手动确认"+site


