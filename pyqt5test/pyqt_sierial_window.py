from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from serial_conf_setting import *

from pyqt_mainwindow_window import *
class sierial_window(QWidget,Ui_serial_window):#串口窗口
     sw_output = pyqtSignal(str,int,int,bool,bool,bool)
     def __init__(self):#串口窗口的执行
         super(sierial_window,self).__init__()
         
         self.setupUi(self)
         self.chcekbit1=0
         self.stopbit1=0
         self.databit1=0
         self.RTS_CTS1=False
         self.DSR_DTR1=False
         self.XON_XOFF1=False
         self.parity_list=[serial.PARITY_NONE,serial.PARITY_EVEN,serial.PARITY_ODD,serial.PARITY_MARK,serial.PARITY_SPACE]
         self.bytesize_list=[serial.EIGHTBITS,serial.SEVENBITS,serial.SIXBITS,serial.FIVEBITS]
         self.stopbits_list=[serial.STOPBITS_ONE,serial.STOPBITS_ONE_POINT_FIVE,serial.STOPBITS_TWO]
     def no_save_close(self):#不保存设置
         self.checkbit.setCurrentIndex(self.chcekbit1)
         self.stopbit.setCurrentIndex(self.databit1)
         self.databit.setCurrentIndex(self.stopbit1)
         self.RTS_CTS.setChecked(self.RTS_CTS1)
         self.DSR_DTR.setChecked(self.DSR_DTR1)
         self.XON_XOFF.setChecked(self.XON_XOFF1)
         self.close()
       
     def save_close(self):#保存设置
         self.chcekbit1=self.checkbit.currentIndex()#检验位
         self.databit1=self.databit.currentIndex()#数据位
         self.stopbit1=self.stopbit.currentIndex()#停止位
         self.RTS_CTS1=self.RTS_CTS.isChecked()
         self.DSR_DTR1=self.DSR_DTR.isChecked()
         self.XON_XOFF1=self.XON_XOFF.isChecked()
         
         self.other_setting()
       
     def other_setting(self):
         
         parity=self.parity_list[self.chcekbit1]#检验位
         bytesize=self.bytesize_list[self.databit1]#数据位
         stopbits=self.stopbits_list[self.stopbit1]#停止位
         xonxoff=self.RTS_CTS1#软件数据流控制
         rtscts=self.DSR_DTR1#硬件数据流控制（需要接线），用于提升数据精度
         dsrdtr=self.XON_XOFF1#连接控制，用于建立连接
         self.sw_output.emit(parity,bytesize,stopbits,xonxoff,rtscts,dsrdtr)
         self.close()
     def serial_window_singal(self):#串口窗口的信号
         self.cancel.released.connect(self.no_save_close)#调用不保存事件
        
         self.sure.released.connect(self.save_close)#调用保存事件

     def test(self):#端口号组合框信号
         self.cc=self.port.currentText()
         if self.cc=="115200":
            print('ok')
         if self.cc=="9600":
            print('fuck')
         print(self.cc)
