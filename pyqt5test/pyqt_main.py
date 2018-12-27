from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import  PyQt5.sip
import sys
from pyqt_mainwindow_window import *
from serial_conf_window import *

from auto_save_window import *
from automation_test_window import *

#主程序  
while True:
         #显示窗口
    if __name__ == '__main__':#本文件当成模块被其他文件加载时将不执行下面程序，只有本py文件作为单独开启的时候才加载
        
        QApplication.setStyle(QStyleFactory.create('Fusion'))#统一程序风格
        app = QApplication(sys.argv)
        sthread=send_thread()#发送处理线程
       
        frist_rthread=first_receive_thread()#第一次串口数据线程
        at2=automation2_test()#调用自动化测试类
        sw=sierial_window()#调用串口画面类
        aw=auto_save_window()#调用自动保存设置类
        mw=main_window(sthread,sw,aw,frist_rthread,at2)#调用主画面类
        mw.port_refresh_event()#进入程序时先刷新一次串口获取
        #调用信号
        mw.mian_window_singal()#调用主窗口信号
        sw.serial_window_singal()#调用更多串口设置窗口信号
        aw.serial_window_singal()
        at2.automation2_test_singal()
        mw.show()#显示主画面
        sys.exit(app.exec_()) #可以捕获异常做清理工作

        
        

        
 
      



