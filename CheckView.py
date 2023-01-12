from CheckController import CheckController


class CheckView:
    """
        信息输出
    """

    def __init__(self):
        self.check_controller = CheckController()

    def __display(self):
        # print("检查控制器启动，准备进行检查")
        # print("即将检查所有Web页面\n")
        # print("GapView检查结果：\n" + self.check_controller.check_gap_view()+"\n")
        # print("Mar检查结果：\n" + self.check_controller.check_mars()+"\n")
        # print("SH monitor文件检查结果：\n" + self.check_controller.check_camera_file()+"\n")
        # print("AAT检查结果:\n" + self.check_controller.check_aat()+"\n")
        # print("DAD检查结果:\n" + self.check_controller.check_dad())
        # print("EMS Online检查结果:\n" + self.check_controller.check_ems_online())
        # print("检查完成")

        result = "Web页面检查结果：" + "\n" + "GapView检查结果：" + self.check_controller.check_gap_view() + "\n" + "Mar检查结果：" + self.check_controller.check_mars() + "\n" + "SH monitor文件检查结果：" + self.check_controller.check_camera_file() + "\n" + "AAT检查结果:" + self.check_controller.check_aat() + "\n" + "DAD检查结果:" + self.check_controller.check_dad() + "\n" + "Audit Online检查结果:" + self.check_controller.check_ems_online()

        return result

    def main(self):
        result = self.__display()
        return result
