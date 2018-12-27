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
from main_setting import *

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
             self.sendemail()#发送邮件
             self.lost_number=0
             
    #邮件发送
     def sendemail(self):
            msg_from='laosiji230@163.com'                                 
            passwd='qwer1234'                                  
            msg_to="laosiji231@163.com"#'laosiji231@163.com'                                              
            subject="python邮件测试"                                       
            #附近邮件对象
            msg = MIMEMultipart('related')
            msg['Subject'] = Header(subject,'utf-8').encode()#邮件标题
            name, addr = parseaddr('你在做的测试出问题了 <%s>' %msg_from)#编码email头
            msg['From'] =formataddr((Header(name, 'utf-8').encode(), addr))#格式化地址
            msg['To'] = msg_to
            #正文
            content=  """
            <p>你在做的测试断开了，快检查</p>
            #<p><a href="http://www.runoob.com">这是一个链接</a></p>
            <p><img src="cid:image1"></p>  
             """
            text=('设置的丢失极限：'+str( self.limit_lost)+'条\n'
            '设置的响应时间：'+str(self.response_time)+'毫秒\n')
            
            #cid为html插入图片方法
            msg.attach (MIMEText(text, 'html', 'utf-8'))
            
           # # html插入图片
            #msgImage = MIMEText(open('tcp.jpg', 'rb').read(), 'base64', 'utf-8')           
            #msgImage.add_header('Content-ID', '<image1>')
            #msg.attach(msgImage)
          
            ##发送附件方式
            #att2 = MIMEText(open('tcp.jpg', 'rb').read(), 'base64', 'utf-8') 
            #att2["Content-Type"] = 'application/octet-stream' 
            #att2["Content-Disposition"] = 'attachment; filename="tcp.jpg"' 
            #msg.attach(att2) 
            try:
                s = smtplib.SMTP("smtp.163.com",25)#绑定smtp发送服务器
                s.login(msg_from, passwd)#登录账号
                #s.set_debuglevel(1)#打印信息
                s.sendmail(msg_from, msg_to, msg.as_string())#发送邮件
                print ("发送成功")
            except smtplib.SMTPException as e:
                print ("发送失败")
                traceback.print_exc() 
            finally:
                s.quit()

            

         



