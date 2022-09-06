from selenium import webdriver
from selenium.webdriver.common.by import By
from Browser import Browser


class AAT:

    @staticmethod
    def check():


        result = ""

        driver = webdriver.Edge()
        driver.get("https://aatsh.cn.deloitteresources.com")
        try:
            if driver.find_element(By.XPATH,
                                   "/html/body/form/table[2]/tbody/tr/td[2]/div/table/tbody/tr[1]/td/span").is_displayed():
                result += "sh节点正常。"
                driver.quit()
        except Exception:
            result += "sh节点异常!!!"
            driver.quit()

        driver = webdriver.Edge()
        driver.get("https://aatse.cn.deloitteresources.com")
        try:
            if driver.find_element(By.XPATH,
                                   "/html/body/form/table[2]/tbody/tr/td[2]/div/table/tbody/tr[1]/td/span").is_displayed():
                result += "se节点正常。"
                driver.quit()
        except Exception:
            result += "se节点异常!!!"
            driver.quit()

        driver = webdriver.Edge()
        driver.get("https://aathk.cn.deloitteresources.com")
        try:
            if driver.find_element(By.XPATH,
                                   "/html/body/form/table[2]/tbody/tr/td[2]/div/table/tbody/tr[1]/td/span").is_displayed():
                result += "hk节点正常。"
                driver.quit()
        except Exception:
            result += "hk节点异常!!!"
            driver.quit()

        return result
    #
    #     aat_dict = {"sh": "https://aatsh.cn.deloitteresources.com",
    #                 "se": "https://aatse.cn.deloitteresources.com",
    #                 "hk": "https://aathk.cn.deloitteresources.com"}
    #     result = ""
    #     for site in aat_dict:
    #         driver = Browser.open(aat_dict[site])
    #     result = AAT.__get_element(driver, result, site)
    #     return result
    #
    # @staticmethod
    # def __get_element(driver, result, site):
    #     try:
    #         if driver.find_element(By.XPATH,
    #                                "/html/body/form/table[2]/tbody/tr/td[2]/div/table/tbody/tr[1]/td/span").is_displayed():
    #             result += "%s节点正常。" % site
    #         driver.quit()
    #         return result
    #     except Exception:
    #         result += "%s节点异常!!!" % site
    #         driver.quit()
    #         return result
