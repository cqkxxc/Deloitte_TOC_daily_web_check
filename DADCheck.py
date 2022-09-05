# "https://auditqualityhk.cn.deloitte.cn/",
# "https://auditqualityprc.cn.deloitte.cn/",
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Browser import Browser


class DAD:

    @staticmethod
    def check():
        result = ""

        driver = Browser.open("https://auditqualityhk.cn.deloitte.cn/")
        result = DAD.get_date_time(driver, result)
        driver.quit()

        driver = Browser.open("https://auditqualityprc.cn.deloitte.cn/")
        result = DAD.get_date_time(driver, result)
        driver.quit()
        return result

    @staticmethod
    def get_date_time(driver, result):
        # TODO
        sleep(10)
        driver.find_element(By.LINK_TEXT, "Audit Quality Milestones").click()
        result += driver.find_element(By.XPATH,
                                      "/html/body/app-root/div/div[2]/div/ng-component/div/app-subheader/div[1]/div[4]").text+"/"
        return result
