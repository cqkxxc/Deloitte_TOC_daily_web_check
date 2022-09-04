from CheckController import CheckController


class CheckView:
    def __init__(self):
        self.check_controller = CheckController()

    def __display(self):
        print("检查控制器启动，准备进行检查")
        print("即将检查所有Web页面")
        # print("GapView检查结果：" + self.check_controller.check_gap_view())
        # print("Mar检查结果：" + self.check_controller.check_mars())
        # print("SH monitor文件检查结果：" + self.check_controller.check_camera_file())
        # print("AAT检查结果:" + self.check_controller.check_aat())
        print("DAD检查结果:" + self.check_controller.check_dad())
        # print("EMS Online检查结果:" + self.check_controller.check_ems_online())
        print("检查完成")

    def main(self):
        self.__display()
