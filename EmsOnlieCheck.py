from time import sleep

from selenium.webdriver.common.by import By

from Browser import Browser


class EmsOnline:
    """
        EMS在线平台检查
    """

    @staticmethod
    def check():
        """
            检查三个EMS平台并检查有无页面元素生成
        :return: str, 检查结果
        """
        result = ""
        # 打开浏览器并访问地址
        driver = Browser.open("https://daemsolcft.cn.deloitteresources.com/")
        # 进入HK检查页面
        sleep(5)
        driver.find_element(By.XPATH,
                            "/html/body/ems-app/div/nova-master/div/div/div[1]/nova-portfolio/div/div[3]/aoui-dialog/div/div/div[2]/portfolio-switcher-server/div/div[2]/div/div/div[1]").click()

        sleep(5)
        if driver.find_element(By.XPATH,
                               "/html/body/ems-app/div/nova-master/div/div/div[1]/nova-portfolio/div/div[3]/div/ems-portfolio-engagements/div/div[2]/nova-ui-table/table").is_displayed():
            result += 'hongkong节点正常\n'
        else:
            result += 'hongkong节点异常！！!\n'

        # 切换SOE节点
        driver.find_element(By.XPATH,
                            "/html/body/ems-app/div/nova-master/div/div/div[1]/nova-portfolio/div/div[1]/div/span[2]/aoui-dicon/div").click()
        sleep(5)
        driver.find_element(By.XPATH,
                            "/html/body/ems-app/div/nova-master/div/div/div[1]/nova-portfolio/div/div[3]/aoui-dialog/div/div/div[2]/portfolio-switcher-server/div/div[2]/div/div/div[2]").click()
        sleep(5)
        if driver.find_element(By.XPATH,
                               "/html/body/ems-app/div/nova-master/div/div/div[1]/nova-portfolio/div/div[3]/div/ems-portfolio-engagements/div/div[2]/nova-ui-table/table").is_displayed():
            result += 'SH SOE节点正常\n'
        else:
            result += 'SH SOE节点异常！！!\n'
        # 切换SH节点
        driver.find_element(By.XPATH,
                            "/html/body/ems-app/div/nova-master/div/div/div[1]/nova-portfolio/div/div[1]/div/span[2]/aoui-dicon/div").click()
        sleep(5)
        driver.find_element(By.XPATH,
                            "/html/body/ems-app/div/nova-master/div/div/div[1]/nova-portfolio/div/div[3]/aoui-dialog/div/div/div[2]/portfolio-switcher-server/div/div[2]/div/div/div[3]").click()
        sleep(5)
        if driver.find_element(By.XPATH,
                               "/html/body/ems-app/div/nova-master/div/div/div[1]/nova-portfolio/div/div[3]/div/ems-portfolio-engagements/div/div[2]/nova-ui-table/table").is_displayed():
            result += 'SH SOE节点正常\n'
        else:
            result += 'SH SOE节点异常！！!\n'

        return result
