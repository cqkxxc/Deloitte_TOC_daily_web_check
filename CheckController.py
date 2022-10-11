from AATCheck import AAT
from DADCheck import DAD
from EmsOnlieCheck import EmsOnline
from GapViewCheck import GapView
from MarsCheck import Mars
from SHCameraCheck import SH_Camera


class CheckController:
    """
        检查流程控制器
    """

    @staticmethod
    def check_gap_view():
        """
            检查GapView页面
        :return: 页面检查结果正常或异常
        """
        result = GapView.check()
        return result

    @staticmethod
    def check_mars():
        """
            检查Mars页面
        :return: 页面检查结果正常或异常
        """
        result = Mars.check()
        return result

    @staticmethod
    def check_camera_file():
        """
            检查sh monitor视频生成文件页面
        :return: 页面检查结果正常或异常
        """
        result = SH_Camera.check()
        return result

    @staticmethod
    def check_aat():
        """
            检查3个AAT页面
        :return: 页面检查结果正常或异常
        """
        result = AAT.check()
        return result

    @staticmethod
    def check_dad():
        """
            检查DAD页面
        :return: 页面检查结果正常或异常
        """
        result = DAD.check()
        return result

    @staticmethod
    def check_ems_online():
        """
            检查EMS ONLINE页面
        :return: 页面检查结果正常或异常
        """
        try:
            result = EmsOnline.check()
            return result
        except Exception:
            return "Audit ONLINE检查流程出错,请手动检查https://daemsolcft.cn.deloitteresources.com/"
