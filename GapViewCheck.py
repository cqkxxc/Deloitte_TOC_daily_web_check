from selenium.webdriver.common.by import By
from Browser import Browser


class GapView:
    """
    检查GapView网站
    """
    @staticmethod
    def check():
        """
            获取EMS版本号并比较US和CN是否一致
        :return: str, EMS版本号检查结果（正常或异常）
        """
        # 打开浏览器并访问地址
        driver = Browser.open("https://daalerts1.da.deloitteresources.com/AlertsDashboard/Views/CDSGapView.aspx")
        # 进入检查页面
        driver.find_element(By.XPATH, "/html/body/div/form/div[3]/div[2]/div[1]/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "/html/body/div/form/div[5]/div/div[1]/a[2]").click()
        # 判断检查项有无异常
        # 获取US版本号
        us_number = driver.find_element(By.XPATH,
                                        "/html/body/div/form/div[5]/div/div[4]/div[2]/div/div/div[1]/div[1]/table/tbody/tr[2]/td[12]/div").text
        # 获取CN版本号
        cn_number = GapView.__get_edition_number(driver)
        # 比较有无版本号异常,若有异常，则打印信息
        for number in cn_number:
            if number != us_number:
                return "EMS版本号异常!!请确认https://daalerts1.da.deloitteresources.com/AlertsDashboard/Views/CDSGapView.aspx"
            else:
                return "EMS版本号正常"

    @staticmethod
    def __get_edition_number(driver):
        """
            获取EMS CN版本号
        :param driver: webdriver类型
        :return: CN版本号
        """
        cn_number = (
            # HK
            driver.find_element(By.XPATH,
                                "/html/body/div/form/div[5]/div/div[4]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[5]/td[12]").text,
            # ICBC
            driver.find_element(By.XPATH,
                                "/html/body/div/form/div[5]/div/div[4]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[6]/td[12]").text,
            # SH
            driver.find_element(By.XPATH,
                                "/html/body/div/form/div[5]/div/div[4]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[10]/td[12]").text,
            # SOE
            driver.find_element(By.XPATH,
                                "/html/body/div/form/div[5]/div/div[4]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[11]/td[12]").text)
        return cn_number
