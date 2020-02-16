# coding=utf-8
import serial
import binascii
import threading
import time
import re
import datetime
import serial.tools.list_ports
import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqt_mainwindow_window import *
import traceback
import csv
import threading
import configparser


class serial_setting():
   def __init__(self):
       
        self.ser=serial.Serial()#baudrate=9600,port='COM1')
        #串口设置
        self.ser.baudrate=9600
        
        self.ser.bytesize=serial.EIGHTBITS#数据位
        self.ser.parity=serial.PARITY_NONE#检验方式
        self.ser.stopbits=serial.STOPBITS_ONE#停止位
        self.ser.timeout=0#设置读取超时
        self.ser.writetimeout=None#设置写入超时
        self.ser.interCharTimeout=None#设置当前字节间超时
        self.ser.xonxoff=False#软件数据流控制
        self.ser.rtscts=False#硬件数据流控制（需要接线），用于提升数据精度
        self.ser.dsrdtr=False#连接控制，用于建立连接
        self.ser.port=''
        self.dtu=0
        self.dtu1=0
        self.dtu2=0
        self.dtu3=0
        self.dtu4=0#保存参数后的判定
        self.dtu1500_count=0
       
        #其他设置
        self.serstr=''
        self.nothing_num=0#锁住只能发一条
   #波特率改变
   def baudrate_change(self):
         
         self.ser.baudrate=int(self.baudrate_comboBox.currentText())#波特率
         print(self.ser)#输出串口信息
   
      
   
       
     #正则匹配com号
   def rematch_com(self):
       com=re.match(r'^(COM)(\d{0,99999})',self.portcomboBox_2.currentText())
       com1=com.group(0)
       return com1
      
  #打开串口
   def port_open(self):
      
       print(self.rematch_com())
       self.ser.port=self.rematch_com()
       print(self.ser)
       try:
                   self.ser.open()
                 
                   
       except serial.SerialException:
                     #正常串口关闭
                    if self.ser.isOpen():
                        self.ser.close()
                        QMessageBox.warning(self, '警告',"串口关闭成功！", QMessageBox.Yes)
                        self.textEdit_4.append('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+"█████"+str(self.ser.port)+'关闭成功')
                        
                        print('串口情况'+str(self.ser.is_open))#输出串口是否开启
                        print(self.ser)#输出串口信息
                       
                    else:#弹窗显示串口重复打开
                        
                        self.port_close_open_5.setText('串口打开')
                        self.label_16.setPixmap(QtGui.QPixmap("../icon/红灯.bmp"))#红灯提示
                        self.more_setting_2.setEnabled(True)
                        QMessageBox.warning(self, '警告',"串口已被打开！请检查", QMessageBox.Yes)
                        self.textEdit_4.append('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+"◆◆◆◆◆"+str(self.ser.port)+'串口打开失败')
                       
                       
       else: #正常串口打开
                    #print('串口打开成功')
                    self.textEdit_4.append('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+"★★★★★"+str(self.ser.port)+'打开成功')
                    print('串口情况'+str(self.ser.is_open))#输出串口是否开启
                    print(self.ser)#输出串口信息
   
           
      #串口检测模块(要while循环执行）
   def port_cheak(self):
        
        self.port_info_list = list(serial.tools.list_ports.comports())#获取串口信息#serial.tools.list_ports.grep(r'^(COM)(\d{0,20})')
        #qt界面显示用的com口数据，未简化
        print(self.port_info_list)
        for qt_port_info in self.port_info_list:
            print('所有串口:'+str(qt_port_info))
            qt_port_info=str(qt_port_info)
            #模组用的com口数据，用正则提取的
            self.portcomboBox_2.addItem(str(qt_port_info))#ui事件，输出文本到组合框内
        #开启hex发送
   def hexsend_handle(self):
         if  self.hex_send_button.isChecked():
           self.sthread.hexsend(1)
         else:
             self.sthread.hexsend(0)
     #dtu设置界面隐藏与显示
   def showhide_dtu_settingwindow(self):
         if self.dtu_setting.isChecked():
            self.frame_44.show()
         else:
            self.frame_44.hide()
    #更改串口其他信息
   def ser_info(self,parity,bytesize,stopbits,xonxoff,rtscts,dsrdtr):
         self.ser.parity=parity
         self.ser.bytesize=bytesize
         self.ser.stopbits=stopbits
         self.ser.xonxoff=xonxoff
         self.ser.rtscts=rtscts
         self.ser.dsrdtr=dsrdtr
         print(self.ser)

 #dtu1200 处理
   def dtu1200_handle(self):
       self.frame_47.setEnabled(True)
       self.dtu_high_2.setEnabled(False)
       self.dtu_set_rfspeed_3.removeItem(9)
       self.dtu_set_rfspeed_3.removeItem(8)
      
       self.dtu_mode_set_2.removeItem(5)
       self.dtu_mode_set_2.removeItem(4)
       self.dtu_mode_set_2.removeItem(3)
       self.dtu_mode_set_2.removeItem(2)
       self.dtu1500_count=0
       
      
 #dtu1500处理
   def dtu1500_handle(self):
       self.frame_47.setEnabled(True)
       self.dtu_high_2.setEnabled(True)
       self.dtu1500_count+=1
       if self.dtu1500_count<2:
           self.dtu_set_rfspeed_3.addItem('DR8    50K')
           self.dtu_set_rfspeed_3.addItem('DR9    100K')
           self.dtu_mode_set_2.addItem('HOST模式')
           self.dtu_mode_set_2.addItem('简单中继模式')
           self.dtu_mode_set_2.addItem('主从中继模式')
           self.dtu_mode_set_2.addItem('简单路由模式')
          
      
       #print(self.dtu_mode_set_2.currentIndex(7))
      
  #串口dtu退出at命令设置模式
   def at_out_setting(self):
       if self.ser.isOpen():
                self.frist_rthread.sleeptime(0.03)
                self.ser.write(bytes('AT+PTM\r\n',encoding='gbk'))
                self.dtu1=1
                print('结束收到')
   def work_mhz_scan(self):
    if self.ser.isOpen() and self.dtu_mode_show_2.text()=='AT设置状态':
        self.ser.write(bytes('AT+SCAN\r\n',encoding='gbk'))
 #dtu保存参数   
   def at_save(self):
       if self.ser.isOpen() and self.dtu_mode_show_2.text()=="AT设置状态":
        dtu_set_rfspeed_3=self.dtu_set_rfspeed_3.currentText()
        dtu_set_rfspeed_3=dtu_set_rfspeed_3[2]
        self.frist_rthread.sleeptime(0.03)
        #改波特率
        if self.singalsave_6.isChecked():
            self.ser.write(bytes('AT+UART='+self.dtu_set_bar_3.currentText()+'\r\n',encoding='gbk'))
            time.sleep(0.9)
            self.progressBar_2.setValue(15)
            self.dtu_bar_4.setText(self.dtu_set_bar_3.currentText())
        #改对方地址
        if self.singalsave_9.isChecked():
            self.ser.write(bytes('AT+DST_ADDR='+self.dtu_set_otheraddress_2.text()+'\r\n',encoding='gbk'))
            time.sleep(0.9)
            self.progressBar_2.setValue(25)
            self.other_dtu_address_4.setText(self.dtu_set_otheraddress_2.text())
        #改自身地址
        if self.singalsave_10.isChecked():
            self.ser.write(bytes('AT+MODULE_ADDR='+self.dtu_set_ownaddress_2.text()+'\r\n',encoding='gbk'))
            time.sleep(0.9)
            self.progressBar_2.setValue(35)
            self.own_dtu_address_4.setText(self.dtu_set_ownaddress_2.text())
        #改dr
        if self.singalsave_11.isChecked():
            self.ser.write(bytes('AT+RF_DR='+dtu_set_rfspeed_3+'\r\n',encoding='gbk'))
            time.sleep(0.9)
            self.progressBar_2.setValue(45)
            self.rf_speed_5.setText('DR'+dtu_set_rfspeed_3)
       #改工作频率
        if self.singalsave_12.isChecked():
            self.ser.write(bytes('AT+RF_FREQ='+self.dtu_set_workmhz_2.text()+'\r\n',encoding='gbk'))
            time.sleep(0.9)
            self.progressBar_2.setValue(55)
            work_mhz_4=re.search(r'(\d{1,100})',self.dtu_set_workmhz_2.text())
            self.work_mhz_4.setValue(float(work_mhz_4.group(0)))
        #保存userkey
        if self.singalsave_15.isChecked():
           self.ser.write(bytes('AT+USER_KEY='+self.dtu_set_user_key_2.text()+'\r\n',encoding='gbk'))
           time.sleep(0.9)
           self.progressBar_2.setValue(57)
        self.dtu_mode_show_2.setText("透传状态")
           
        
       #改dtu模式
        if    self.singalsave_13.isChecked():
            
            if self.dtu_mode_set_2.currentText()=='HOST模式':
               self.ser.write(bytes('AT+DTU_WORK_MODE=HOST_MODE\r\n',encoding='gbk'))
            if self.dtu_mode_set_2.currentText()=='简单中继模式':
               self.ser.write(bytes('AT+DTU_WORK_MODE=SIMPLE_REPEATER_MODE\r\n',encoding='gbk'))
            if self.dtu_mode_set_2.currentText()=='主从中继模式':
                 self.ser.write(bytes('AT+DTU_WORK_MODE=MASTER_SLAVE_REPEATER_MODE\r\n',encoding='gbk'))
            if self.dtu_mode_set_2.currentText()=='简单路由模式':
                self.ser.write(bytes('AT+DTU_WORK_MODE=SIMPLE_ROUTER_MODE\r\n',encoding='gbk'))
            if self.dtu_mode_set_2.currentText()=='普通透传模式':
                self.ser.write(bytes('AT+DTU_WORK_MODE=GENERAL_MODE\r\n',encoding='gbk'))
            if self.dtu_mode_set_2.currentText()=='回环模式':
                self.ser.write(bytes('AT+DTU_WORK_MODE=LOOP_MODE\r\n',encoding='gbk'))
            time.sleep(0.9)
            self.progressBar_2.setValue(80)
         #改dtu发送超时时间
        if self.dtu1500_2.isChecked() and  self.singalsave_14.isChecked():
             self.ser.write(bytes('AT+PACKET_COMBINED_TIME='+self.dtu_set_datatime_2.text(),encoding='gbk'))
             time.sleep(0.9)
             self.data_time_2.setText(self.dtu_set_datatime_2.text())
             self.progressBar_2.setValue(85)
             self.mode_show_2.setText(self.dtu_mode_set_2.currentText())
        #1.6版本保存模式
       #最后保存
        if self.singalsave_15.isChecked() or self.singalsave_6.isChecked()or self.singalsave_9.isChecked()or self.singalsave_10.isChecked()or self.singalsave_11.isChecked()or self.singalsave_12.isChecked()or self.singalsave_13.isChecked()or self.singalsave_14.isChecked():
            
            self.ser.write(bytes('AT+SAVE\r\n',encoding='gbk'))
            self.progressBar_2.setValue(90)
            self.dtu4=1#开启判断
        else:
              QMessageBox.information(self, '未选择保存项','请勾选要保存的参数', QMessageBox.Yes)
       
             
   def dtu_ping(self):
       if self.ser.isOpen() and self.dtu_mode_show_2.text()=='AT设置状态':
            self.ser.write(bytes('AT+PING='+self.ping_address_2.text()+'\r\n',encoding='gbk'))

# 串口dtu进入at命令设置模式
   def at_setting1(self):
        if self.ser.isOpen():
           self.frist_rthread.sleeptime(0.03)
           print('发送at命令1')
           self.nothing_num=0#锁住只能发一条
           self.ser.write(bytes('++++++\r\n',encoding='gbk'))
           time.sleep(0.15)
           self.ser.write(bytes('def\r\n',encoding='gbk'))
           self.dtu1=1#开启锁
           print(self.dtu1)
           print('发送at命令结束')
 #dtu设置界面按钮信号
   def dtu_setting_mode(self):           
         self.ping_2.released.connect(self.dtu_ping)#ping指令
         self.dtu_in_setting_4.released.connect( self.at_setting1)#at模式进入1
         self.dtu_save_2.released.connect( self.at_save)#at模式进入1
          
         self.dtu_out_setting_3.released.connect(self.at_out_setting)#退出at模式
         self.dtu_info_search1_3.released.connect(self.dtu_info_search)#搜索dtu信息以及单前模式
         self.dtu_reset_2.released.connect(self.dtu_reset_event)#重置dtu参数
         self.dtu_restart_2.released.connect(self.dtu_restart_event)#dtu重启

     #保存到csv文件
   def dtu_csv_save(self):
       a=0
       dtu_csv=QFileDialog.getSaveFileName(self,#这里为st类型
                                    "DTU设置参数",#名称
                                    "./save",#目标地址
                                    "Text Files (*.csv)")#文件类型
       
       first_data=[('DTU编码号','自身DTU地址','对方DTU地址','DTU波特率','空口速率','无线频道','DTU工作模式','UID','固件版本','USER_KEY')]
       data = [
            
            ('',self.own_dtu_address_4.text(), self.other_dtu_address_4.text(),self.dtu_bar_4.text(),self.rf_speed_5.text(),self.work_mhz_4.text(),self.mode_show_2.text(),self.uid_2.text(),self.firmwareversion_14.text(),
             self.none_2.text())
                ]
       try:#创建csv并判断参数
            with open(dtu_csv[0], 'a', newline='') as csv_file:
                print('创建成功')
            with open(dtu_csv[0], 'r', newline='') as csv_file:
                    dtu_csv_read=csv.reader(csv_file)
                    for row in dtu_csv_read:
                        if '自身DTU地址'and '对方DTU地址'and'DTU波特率'and '空口速率'in row:
                            a=1
                    print('读取成功')
                    print(a)
            if a==1:#判断是否要追加标题
                 with open(dtu_csv[0], 'a', newline='') as csv_file:
                     dtu_csv_write=csv.writer(csv_file)
                     for list in  data :
                         print(list)
                         dtu_csv_write.writerow(list)
                 print('没有创建了标题')
            else:
                with open(dtu_csv[0], 'a', newline='') as csv_file:
                     dtu_csv_write=csv.writer(csv_file)
                     for list in  first_data :
                         print(list)
                         dtu_csv_write.writerow(list)
                     for list in  data :
                         print(list)
                         dtu_csv_write.writerow(list)
                     print('创建标题')  
       except:
            traceback.print_exc() 
            QMessageBox.warning(self, '保存失败','未指定保存目录', QMessageBox.Yes)

#dtu重置
   def dtu_reset_event(self):
       if self.ser.isOpen() and self.dtu_mode_show_2.text()=="AT设置状态":
          reply = QMessageBox.question(self, '重置DTU', '是否确定将DTU参数重置？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
          if reply == QMessageBox.Yes:
             #print('ssssssssssssssssssssssssssssssssssssssssfafasfasfa')
              self.ser.write(bytes('AT+SYS\r\n',encoding='gbk'))
              time.sleep(2)
              self.ser.write(bytes('AT+RST\r\n',encoding='gbk'))
              self.dtu_mode_show_2.setText("透传状态")
#dtu重启
   def dtu_restart_event(self):
        if self.ser.isOpen() and self.dtu_mode_show_2.text()=="AT设置状态":
            
            reply = QMessageBox.question(self, '重启DTU', '是否确定重启DTU？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:

                #print('ssssssssssssssssssssssssssssssssssssssssfafasfasfa')
                self.ser.write(bytes('AT+RST\r\n',encoding='gbk'))
                self.dtu_mode_show_2.setText("透传状态")
                self.dtu4=1  
   


#发送线程,处理完后发送信号输出到qt界面
class send_thread(QThread):

   sd_data_output = pyqtSignal(str, bytes)#数据输出信号
 
   def __init__(self):
        super(send_thread, self).__init__()
        self.send_text1=bytes()
        self.hexsend(0)
        self.encode_choose('GBK')
        self.next_row_open(0)
   def encode_choose(self,code):
       self.coding=code
   def work(self,text_input,ser1):#处理run函数不能处理的东西
       self.send_text=text_input
       self.ser1=ser1
   def hexsend(self,hsb):
       self.hex_send_button=hsb
   def next_row_open(self,next_row_p):
       self.next_row_p=next_row_p
      
   def run(self):
            #print("输入正常")
        if self.ser1.isOpen():
            
            if self.hex_send_button==1:
                self.send_text=self.send_text.replace('\n','')#清除回车一定要放在最前
                self.send_text=self.send_text.replace(' ','')#其次清除空白
                self.send_text_length=int(len(self.send_text))#最后才统计字数才不会出错
           
                print('输入区字符数'+str(self.send_text_length))
                    #判断字符数，如果是基数就截取最后一位数据出来不发
               
                if self.send_text_length%2==0:
                   
                        self.send_text=self.send_text[0:self.send_text_length]
                else:
                    
                        self.send_text=self.send_text[0:self.send_text_length-1]
                         #转换成ascii编码的16进制的byte类型,消除所有空格
                self.send_text1=binascii.a2b_hex(self.send_text)
               
                #显示部分
                second_send_data= binascii.b2a_hex(self.send_text1).decode() #乱序解码，借用编译好的acii码16进制重新输出（消除不规则空格和合并字符）
                pattern = re.compile('.{1,2}')#匹配出两个字符（数据类型为列表型）
                second_send_data=(' '.join(pattern.findall(second_send_data)))#匹配出两个字符后在后面加空格（顺序以排好）
                #qtshow_send_data=('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+'发→○'+ self.send_text+"  ")#加上显示时间和发标签
                self.ser1.write(self.send_text1)
                qtshow_send_data=('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+'发→○'+ second_send_data+"  ")#加上显示时间和发标签
            else:
                
              
                if  self.next_row_p==1:
                    self.send_text1=bytes(self.send_text+'\r\n',encoding= self.coding)
                else:
                    try:
                        self.send_text1=bytes(self.send_text,encoding= self.coding)
                    except:
                        print('解码错误')
            #写入
                #qtshow_send_data=('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+'发→○'+ self.send_text+"  ")#加上显示时间和发标签
                self.ser1.write(self.send_text1)
                qtshow_send_data=('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+'发→○'+ self.send_text+"  ")#加上显示时间和发标签
            print(self.send_text1)
            self.ser1.flushOutput()
            self.sd_data_output.emit(qtshow_send_data,self.send_text1)#发送数据出去进行添加到显示框和信标定位
     
 #接收线程,处理完后输出qt显示    
class first_receive_thread(QThread):
   fre_data_output = pyqtSignal(bytes,str)#数据输出信号
   fre2_data_output = pyqtSignal()#数据输出信号
   
   
   def __init__(self):
        super(first_receive_thread, self).__init__()  
        self.first_receive_data=bytes()
        self.hex(0)
   
      
        
   def sleeptime(self,sleep_time):#传递睡眠时间
       self.ser1.timeout=sleep_time
       
   def hex(self,hex_button):
       self.hex_button777=hex_button
   def first_work(self,ser1,port_switch,port_refresh_switch,combobox_switch,dtu_test):#传递一次串口数据
        self.dtu_test=dtu_test
        self.ser1=ser1
        self.port_switch=port_switch#开启开关
        self.port_refresh_switch=port_refresh_switch#刷新开关
        self.combobox_switch=combobox_switch#随意变换串口开关

        #self.hex_button777=1
   
  
   def run(self):
       while self.ser1.isOpen() and  self.dtu_test==0:
           
             try:
                self.n=self.ser1.inWaiting()
                if self.n>0:
                    print('接收时间'+'['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+str(self.first_receive_data))
                    #print(str(self.n)+'字符数量')
                    #self.full_re_time=datetime.datetime.now()
                    #hardware_real_time=str('硬实时时间○●○'+'['+str(self.full_re_time.strftime('%H:%M:%S.%f'))+']')#此为串口数据进入时间
                    #print('睡眠时间'+str(self.sleep_time))
                    first_receive_data=self.ser1.readline()#读取睡眠后的缓冲区数据
                    receive_time='['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+'收←●'
                    print(receive_time)
                    #print(first_receive_data)
                    #start=datetime.datetime.now()
                    if  self.hex_button777==1:
                        second_receive_data=binascii.b2a_hex(first_receive_data).decode('utf-8') #将acii码形式的byte类型转为16进制的str类型
                        pattern = re.compile('.{1,2}')#最多匹配出两个字符，
                        hex_data=(' '.join(pattern.findall(second_receive_data)))#匹配出两个字符后在后面加空格（顺序以排好）
                        receive_data=(receive_time+hex_data)
                    else:
                         try:
                             receive_data=first_receive_data.decode('gbk')
                             
                         except:
                                receive_data=(receive_time+'显示内容错误，请勾选hex显示或更换编码或调大超时时间')#加上显示时间和发标签
                         else:
                                receive_data=(receive_time+str(receive_data))#加上显示时间和发标签
                    
                    #self.ser1.flushInput()       
                    self.fre_data_output.emit(first_receive_data,receive_data)#调用接收数据处理程序   
             except :
                traceback.print_exc() 
                #print(e)
                print("Unexpected error:", sys.exc_info()[0])
                print('串口情况'+str(self.ser1.is_open))#输出串口是否开启
                print(self.ser1)#输出串口信息
                print('qqqqqq')
                self.ser1.close()
                print('储存区结果'+str(self.port_switch))
                if self.port_refresh_switch==4 and self.port_switch==1 and self.combobox_switch==5 or self.port_refresh_switch==3 and self.port_switch==2 and self.combobox_switch==5 or self.port_refresh_switch==3 and self.port_switch==1 and self.combobox_switch==6 :
             #防止在刷新串口时和关闭串口时错误调用
                   print('1')
                else:
                   self.fre2_data_output.emit()#调用串口错误处理事件