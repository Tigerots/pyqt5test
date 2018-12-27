from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from automation_test_setting import *
from moudle_pysierial import *
import random
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import smtplib
import configparser


#from main_setting import *
class automation2_test(QDialog,Ui_Dialog,Ui_MainWindow):#串口窗口
     at_output = pyqtSignal()
     at2_output= pyqtSignal()
     at3_output= pyqtSignal()
     def __init__(self):#串口窗口的执行
         super(automation2_test,self).__init__()
         self.setupUi(self)
         
         #self.show_model.setText()
         self.lost_limit.setValidator(QIntValidator(0,9999999))
         self.send_time.setValidator(QIntValidator(0,9999999))
         self.textnumber.setValidator(QIntValidator(0,9999999))
         self.responsetime.setValidator(QIntValidator(0,9999999))
         self.model=0#发送或接收模式
         self.random_text=''#随机字符
         self.lost_number=0
         self.response_time=0#响应时间
         self.limit_lost=0#极限丢失条数
         self.send_limit=0#发送锁计时器
         self.sendtime=0#发送时间
     def  automation2_test_singal (self):
          self.atuo_send.released.connect(self.send_test_open)
          self.auto_receive.released.connect(self.receiver_test_open)
          self.offtest.released.connect(self.testclose)
          self.buttonBox.rejected.connect(self.reject1)
          self.buttonBox.accepted.connect(self.accept1)
        #发送
     def send_test_open(self):
         self.show_model.setText('发送端')
         self.model=1#发送
      #接收
     def receiver_test_open(self):
         self.show_model.setText('接收端')
         self.model=2#接收
    #关闭测试程序
     def testclose(self):
         self.model=0
         self.send_limit=0
         self.show_model.setText('关闭')
         self.at2_output.emit()#停止计时器
    #ok
     def accept1(self):
         if self.show_model.text()=='':
              QMessageBox.information(self, '没选模式','请选模式', QMessageBox.Yes)
         else:
                 self.text_number=int(self.textnumber.text())
                 self.sendtime=int(self.send_time.text())
                 self.limit_lost=int(self.lost_limit.text())
                 self.response_time=int(self.responsetime.text())
                 self.at_output.emit()#传出模式和接收端字符
                 self.close()
         
      #取消  
     def reject1(self):
         self.close()
    #生成随机字符
     def create_randomstr(self):
         #发送端
         if self.model==1:
             if self.text_number-8>0:
                 for i in range(self.text_number-8):
                     r_str= random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
                     self.random_text+=str(r_str)
             self.random_text='send'+self.random_text+'test'
             print( self.random_text)
             #接收端
         if self.model==2:
             if self.text_number-11>0:
                 for i in range(self.text_number-8):
                     r_str= random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
                     self.random_text+=str(r_str)
             self.random_text='receive'+self.random_text+'test'

             
     #超时发送
     def testtimeout(self):
         self.lost_number+=1
         print('丢失承购sssssssssssssssssssss')
         self.at3_output.emit()
         if self.lost_number>self.limit_lost:#若现丢失值大于设定的丢失值
             print('测试失败')
            
             self.lost_number=0
             
 
            

         



