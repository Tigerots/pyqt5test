
from pyqt_mainwindow_setting import *
from moudle_pysierial import *
import sys
import time
import chardet

import os


class main_window(QMainWindow, serial_setting, Ui_MainWindow):#主界面
     def __init__(self, sthread, sw,aw,frist_rthread,at2):#主窗口的执行
        super(main_window, self).__init__()
        self.setupUi(self) 
        self.sw = sw
        self.aw = aw
        
        self.timer = QTimer(self)
        self.at2 = at2#自动测试模式
        self.sthread=sthread#发送线程
        self.sthread.work(bytes(),self.ser)
      
        self.frist_rthread=frist_rthread#接收串口数据线程
      
     
        self.receiveswitch=False#串口接收开启开关
        self.refresh_switch=False#刷新时间判断
       
        self.input_hex_list=[]#hex发送储存列表
      
        self.input_hex_show=''#hex发送存储显示
        self.hex_text=''#hex发送文本
        self.normal_text=''#普通发送文本
        self.port_switch=1#关闭串口锁
        self.port_refresh_switch=3#刷新串口锁
        self.combobox_switch=5#随意切换锁
        self.hardware_real_time=""#硬实时显示
        self.num_refresh=0#刷新计数
        self.send_numbers=0#发送统计字节
        self.receive_numbers=0#接收统计字节
        self.show_cache=0#显示缓存
        self.show_cache2=0#自动保存的统计
        self.auto_save_number=0#自动保存条数
        self.atuo_save_filename=''#自动保存文件目录
        self.atuo_save_switch=False#自动保存开关
        self.cacheclean_switch=False#清除缓存时候的自动保存开关
        self.auto_save_clean=0#自动保存首次清空
        self.received_strip=0#接收条数
        self.send_strip=0#发送条数
        self.dtu_test=0#线程关闭（不能移动）\
        #自动化测试参数
        self.testtime= QTimer(self)#测试用计时器
        self.ini_info_import()
     def closeEvent(self, event):
            # 加载现有配置文件
        conf = configparser.ConfigParser()
        # 写入配置文件
        conf.add_section('custom_content') #添加section
    # 添加值
        print(self.o1.text())
        print(self.o2.text())
        conf.set('custom_content', 'v1', str(self.o1.text()))
        conf.set('custom_content', 'v2', self.o2.text())
        conf.set('custom_content', 'v3', self.o3.text())
        conf.set('custom_content', 'v4', self.o4.text())
        conf.set('custom_content', 'v5', self.o5.text())
        conf.set('custom_content', 'v6', self.o6.text())
        conf.set('custom_content', 'v7', self.o7.text())
        conf.set('custom_content', 'v8', self.o8.text())
        conf.set('custom_content', 'v9', self.o9.text())
        conf.set('custom_content', 'v10', self.o10.text())
        conf.set('custom_content', 'v11', self.o11.text())
        conf.set('custom_content', 'v12', self.o12.text())
        conf.set('custom_content', 'v13', self.o13.text())
        conf.set('custom_content', 'v14', self.o14.text())
        conf.set('custom_content', 'v15', self.o15.text())
        conf.set('custom_content', 'v16', self.o16.text())
        conf.set('custom_content', 'v17', self.o17.text())
        conf.set('custom_content', 'v18', self.o18.text())
        conf.set('custom_content', 'v19', self.o19.text())
        conf.set('custom_content', 'v20', self.o20.text())
        conf.add_section('custom_text') #添加section
        conf.set('custom_text', 's1', self.s1.text())
        conf.set('custom_text', 's2', self.s2.text())
        conf.set('custom_text', 's3', self.s3.text())
        conf.set('custom_text', 's4', self.s4.text())
        conf.set('custom_text', 's5', self.s5.text())
        conf.set('custom_text', 's6', self.s6.text())
        conf.set('custom_text', 's7', self.s7.text())
        conf.set('custom_text', 's8', self.s8.text())
        conf.set('custom_text', 's9', self.s9.text())
        conf.set('custom_text', 's10', self.s10.text())
        conf.set('custom_text', 's11', self.s11.text())
        conf.set('custom_text', 's12', self.s12.text())
        conf.set('custom_text', 's13', self.s13.text())
        conf.set('custom_text', 's14', self.s14.text())
        conf.set('custom_text', 's15', self.s15.text())
        conf.set('custom_text', 's16', self.s16.text())
        conf.set('custom_text', 's17', self.s17.text())
        conf.set('custom_text', 's18', self.s18.text())
        conf.set('custom_text', 's19', self.s19.text())
        conf.set('custom_text', 's20', self.s20.text())
       #普通设置
        conf.add_section('setting') #添加section
        conf.set('setting','input_area',self.textEdit.toPlainText())
# 写入文件
        with open('conf.ini', 'w') as fw:
          conf.write(fw)
     def ini_info_import(self):
        try:
                conf1 = configparser.ConfigParser()
                conf1.read("conf.ini")
                self.o1.setText (conf1.get('custom_content', 'v1'))
                self.o2.setText (conf1.get('custom_content', 'v2'))
                self.o3.setText (conf1.get('custom_content', 'v3'))
                self.o4.setText (conf1.get('custom_content', 'v4'))
                self.o5.setText (conf1.get('custom_content', 'v5'))
                self.o6.setText (conf1.get('custom_content', 'v6'))
                self.o7.setText (conf1.get('custom_content', 'v7'))
                self.o8.setText (conf1.get('custom_content', 'v8'))
                self.o9.setText (conf1.get('custom_content', 'v9'))
                self.o10.setText (conf1.get('custom_content', 'v10'))
                self.o11.setText (conf1.get('custom_content', 'v11'))
                self.o12.setText (conf1.get('custom_content', 'v12'))
                self.o13.setText (conf1.get('custom_content', 'v13'))
                self.o14.setText (conf1.get('custom_content', 'v14'))
                self.o15.setText (conf1.get('custom_content', 'v15'))
                self.o16.setText (conf1.get('custom_content', 'v16'))
                self.o17.setText (conf1.get('custom_content', 'v17'))
                self.o18.setText (conf1.get('custom_content', 'v18'))
                self.o19.setText (conf1.get('custom_content', 'v19'))
                self.o20.setText (conf1.get('custom_content', 'v20'))
                self.s1.setText (conf1.get('custom_text', 's1'))
                self.s2.setText (conf1.get('custom_text', 's2'))
                self.s3.setText (conf1.get('custom_text', 's3'))
                self.s4.setText (conf1.get('custom_text', 's4'))
                self.s5.setText (conf1.get('custom_text', 's5'))
                self.s6.setText (conf1.get('custom_text', 's6'))
                self.s7.setText (conf1.get('custom_text', 's7'))
                self.s8.setText (conf1.get('custom_text', 's8'))
                self.s9.setText (conf1.get('custom_text', 's9'))
                self.s10.setText (conf1.get('custom_text', 's10'))
                self.s11.setText (conf1.get('custom_text', 's11'))
                self.s12.setText (conf1.get('custom_text', 's12'))
                self.s13.setText (conf1.get('custom_text', 's13'))
                self.s14.setText (conf1.get('custom_text', 's14'))
                self.s15.setText (conf1.get('custom_text', 's15'))
                self.s16.setText (conf1.get('custom_text', 's16'))
                self.s17.setText (conf1.get('custom_text', 's17'))
                self.s18.setText (conf1.get('custom_text', 's18'))
                self.s19.setText (conf1.get('custom_text', 's19'))
                self.s20.setText (conf1.get('custom_text', 's20'))
                self.textEdit.setPlainText(conf1.get('setting', 'input_area'))
        except:
            print('sss')
        

     def mian_window_singal(self):#主窗口的信号
         
         self.other_main_setting()#调用窗口其他设定事件
         
         self.hex_send_button.toggled.connect(self.input_area_change)#输入区变换事件
         self.port_refresh_3.released.connect(self.port_refresh_event)#刷新串口事件
         self.textEdit.textChanged.connect(self.input_hex_check)#hex输入检查事件
         self.port_close_open_5.released.connect(self.port_open_close)#串口打开/关闭按钮事件
         self.sendbutton_2.released.connect(self.send_ready_send)#点击发送事件
         self.timingswitch.toggled.connect(self.timing_send)#定时发送预处理
         self.timer.timeout.connect(self.send_ready_send)#lambda:print('timing_send'))#定时发送事件
         self.sthread.sd_data_output.connect(self.send_out)#发送多线程数据输出事件
         self.frist_rthread.fre_data_output.connect(self.receive_handle)#串口数据处理多线程数据输出事件
         self.frist_rthread.fre2_data_output.connect(self.sierial_break)#接收过程中意外处理事件
         self.dtu_setting.triggered.connect(self.showhide_dtu_settingwindow)#dtu设置界面隐藏与显示事件
         self.more_setting_2.released.connect(self.serial_window_show)#显示其他串口设置窗口
         self.outtimeline_2.textChanged.connect(self.receive_time)#串口显示超时时间实时改变事件
         self.portcomboBox_2.currentIndexChanged.connect(self.combobox_port_change)#随意改变串口事件
         self.baudrate_comboBox.currentIndexChanged.connect(self.baudrate_change)#随意改波特率事件
         self.sw.sw_output.connect(self.ser_info)#更改串口其他信息事件
         self.function_setting.triggered.connect(self.showhide_settingwindow)#显示参数设置区事件
         self.clean_received_show.released.connect(self.clean_receivenumbers)#清除接收字符显示
         self.clean_send_show.released.connect(self.clean_sendnumbers)#清除发送字符显示
         self.savefile_2.released.connect(self.save_file)#手动保存文件事件
         self.auto_save.triggered.connect(self.auto_save_close)#关闭自动保存模式
         self.aw.aw_output.connect(self.atuo_save_file)
         self.dtu_setting_mode()#dtu设置
     
     def custom_send(self):
        #if self.ser.isOpen():
            self.p1.released.connect(lambda:self.custom_hex_send(str(self.o1.text())) )
            self.p2.released.connect(lambda:self.custom_hex_send(str(self.o2.text())) )
            self.p3.released.connect(lambda:self.custom_hex_send(str(self.o3.text())) )
            self.p4.released.connect(lambda:self.custom_hex_send(str(self.o4.text())) )
            self.p5.released.connect(lambda:self.custom_hex_send(str(self.o5.text())) )
            self.p6.released.connect(lambda:self.custom_hex_send(str(self.o6.text())) )
            self.p7.released.connect(lambda:self.custom_hex_send(str(self.o7.text())) )
            self.p8.released.connect(lambda:self.custom_hex_send(str(self.o8.text())) )
            self.p9.released.connect(lambda:self.custom_hex_send(str(self.o9.text())) )
            self.p10.released.connect(lambda:self.custom_hex_send(str(self.o10.text())) )
            self.p11.released.connect(lambda:self.custom_hex_send(str(self.o11.text())) )
            self.p12.released.connect(lambda:self.custom_hex_send(str(self.o12.text())) )
            self.p13.released.connect(lambda:self.custom_hex_send(str(self.o13.text())) )
            self.p14.released.connect(lambda:self.custom_hex_send(str(self.o14.text())) )
            self.p15.released.connect(lambda:self.custom_hex_send(str(self.o15.text())) )
            self.p16.released.connect(lambda:self.custom_hex_send(str(self.o16.text())) )
            self.p17.released.connect(lambda:self.custom_hex_send(str(self.o17.text())) )
            self.p18.released.connect(lambda:self.custom_hex_send(str(self.o18.text())) )
            self.p19.released.connect(lambda:self.custom_hex_send(str(self.o19.text())) )
            self.p20.released.connect(lambda:self.custom_hex_send(str(self.o20.text())) )
            
            
           #self.sthread.work(self.text_input,self.ser)#把数据转进去多线程里面处理
           
         
    
    #切换发送编码
     def code_handle(self):
         if self.gbk.isChecked():
             print('gbk')
             self.gb2312.setChecked(False)
             self.utf_8.setChecked(False)
         if self.gb2312.isChecked():
              print('gb2312')
              self.gbk.setChecked(False)
              self.utf_8.setChecked(False)
         if  self.utf_8.isChecked():
             print('utf-8')
             self.gb2312.setChecked(False)
             self.gbk.setChecked(False)
    #hex显示
     def hex_show(self):
        if  self.hex_show_button_2.isChecked():
           self.frist_rthread.hex(1)
        else:
            self.frist_rthread.hex(0)

    #关闭和开启自动保存模式
     def auto_save_close(self):
          if self.atuo_save_switch==True:
               print('ssss')
               #self.auto_save.setChecked(False)
               QMessageBox.information(self, '自动保存模式关闭','关闭成功', QMessageBox.Yes)
               self.atuo_save_switch=False
         #if self.auto_save.isChecked()==False:
          #print(self.auto_save.isChecked())
               self.auto_save.setChecked(False)
          else:
             self.aw.show()
             self.auto_save.setChecked(False)
             print('bbbbb')
            
           
             
    #自动保存事件
     def atuo_save_file(self,atuo_save_filename,auto_save_number,atuo_save_switch):
         self.auto_save_number=auto_save_number#自动保存字节数
        
         self.atuo_save_filename=atuo_save_filename#自动保存路径
         self.atuo_save_switch=atuo_save_switch#自动保存开关
         self.auto_save.setChecked(True)#设置为true
         QMessageBox.information (self, '自动保存模式开启','开启成功', QMessageBox.Yes)
         self.auto_save_clean=1#先清空内容
     def nextrow_handle(self):
       if self.nextrow.isChecked():
           self.sthread.next_row_open(1)
           
       else:
           self.sthread.next_row_open(0)
           
         
    #保存显示窗内容到txt
     def save_file(self):
         filename=QFileDialog.getSaveFileName(self,#这里为st类型
                                    "文件保存",#名称
                                    "./save",#目标地址
                                    "Text Files (*.txt)")#文件类型
         print(filename)
         #判断是否创建了文件
         
         try:
            with open(filename[0],'w') as f:#filename第一项是文件名，第二项是类型名
                my_text=self.textEdit_4.toPlainText()
                f.write(my_text)
          
         except:
            QMessageBox.warning(self, '保存失败','未指定保存目录', QMessageBox.Yes)
         else:
               QMessageBox.information(self, '保存成功',str(filename[0])+'保存成功', QMessageBox.Yes)
    #清除接收字符区
     def clean_receivenumbers(self):
         self.receive_number_3.clear()
         self.lineEdit_5.clear()
         self.receive_number_2.clear()
         self.received_strip=0
         self.receive_numbers=0
    #清除发送字符区
     def clean_sendnumbers(self):
         self.send_number_4.clear()
         self.lineEdit_6.clear()
         self.send_number_3.clear()
         self.send_numbers=0
         self.send_strip=0
#窗口非主要设定
     def other_main_setting(self):
         self.testtime.timeout.connect(self.at2.testtimeout)#自动化测试2超时设定
         self.at2.at_output.connect(self.atuotest)#自动化测试2事件
         self.at2.at2_output.connect(lambda:self.testtime.stop()or  self.timingswitch.setChecked(False))#自动化测试停止事件
         self.at2.at3_output.connect(lambda:self.textEdit_4.append('▲▲▲▲▲▲▲发生丢包▼▼▼▼▼▼▼'))#自动化测试停止事件
         self.at2test.triggered.connect(lambda:self.at2.show() )
         self.custom_send()#定制发送
         self.dtu_info_savetocsv_2.clicked.connect(self.dtu_csv_save)
         self.hex_send_button.clicked.connect(self.hexsend_handle)#
         self.nextrow.clicked.connect(self.nextrow_handle)
         self.hex_show_button_2.clicked.connect(self.hex_show)#
         self.frame_47.setEnabled(False)#隐藏dtu设置
         self.dtu1200_2.clicked.connect(self.dtu1200_handle)#dtu模式选择
         self.dtu1500_2.clicked.connect(self.dtu1500_handle)
         self.timing.setValidator(QIntValidator(self))#限制定时时间输入框为整数型数据
         self.outtimeline_2.setValidator(QIntValidator(1,9999))#限制超时时间输入框为4位整数型数据
         self.dtu_set_ownaddress_2.setValidator(QIntValidator(1,9999))#限制dtu自身地址为4位整数型数据
         self.dtu_set_otheraddress_2.setValidator(QIntValidator(1,9999))#限制dtu对方地址为4位整数型数据
         self.dtu_set_datatime_2.setValidator(QIntValidator(1,9999))#限制dtu发送超时时间为4位整数型数据
         self.ping_address_2.setValidator(QIntValidator(1,9999))#限制ping地址为4位整数型数据
         self.dtu_set_user_key_2.setValidator(QIntValidator(1,9999))#限制ping地址为4位整数型数据
         self.clean_receive_2.released.connect( self.clean_show_receive)#清除窗口显示
         self.clean_send.released.connect(lambda:self.textEdit.clear())#清除发送区
         self.action200.triggered.connect(lambda:self.action500.setChecked(False) or self.action1000.setChecked(False))#选定为200万
         self.action500.triggered.connect(lambda:self.action200.setChecked(False) or self.action1000.setChecked(False))#选定为500万
         self.action1000.triggered.connect(lambda:self.action500.setChecked(False) or self.action200.setChecked(False))#选定为1000万
         self.dtu_scan.released.connect(self.work_mhz_scan)#信道扫描
         self.gbk.triggered.connect(lambda:print('gbk') or self.gb2312.setChecked(False)or self.utf_8.setChecked(False)or self.sthread.encode_choose('gbk'))
         self.gb2312.triggered.connect(lambda:print('gb2312')or self.gbk.setChecked(False)or self.utf_8.setChecked(False)or self.sthread.encode_choose('gb2312'))
         self.utf_8.triggered.connect(lambda:print('utf-8')or self.gbk.setChecked(False)or self.gb2312.setChecked(False) or self.sthread.encode_choose('utf-8'))
         self.label_23.setText(u'<a href="http://www.logi-iot.com/" ><b> ★★伦图科技--物联网无线通讯解决方案专家★★ </b></a>')
    #自动化测试2显示
     def atuotest(self):
         self.at2.create_randomstr()
         self.textEdit.setPlainText(self.at2.random_text)
         if self.at2.model==1:
                self.timing.setText(str(self.at2.sendtime))
                self.timingswitch.setChecked(True)
         
                 




     #清空显示窗口
     def clean_show_receive(self):
         self.textEdit_4.clear()
         self.show_cache2=0
     #自动保存文件操作
     def auto_save_write_file(self):
         if  self.auto_save_clean==1:#先清空内容
             with open(self.atuo_save_filename,'w') as g:
                 nonetext=''
                 g.write(nonetext)
             self.auto_save_clean=0
         if self.atuo_save_switch==True:#自动保存写入
           with open(self.atuo_save_filename,'a') as f:
                  my_text=self.textEdit_4.toPlainText()
                  if self.cacheclean_switch:#清空缓存时候的自动保存
                     print('当前已保存值'+str(self.show_cache2))
                     print('总缓存'+str(self.show_cache))
                     my_text1=my_text[self.show_cache2:self.show_cache]
                     print('清除缓存保存完成')
                     self.cacheclean_switch=False
                  else:#非清空缓存的自动保存
                      my_text1=my_text[self.show_cache2:self.show_cache]
                      print('清除完成')
                  self.show_cache2=self.show_cache
                  print('总缓存'+str(self.show_cache))
                  print('当前已保存值'+str(self.show_cache2))
                  print('设置值'+str(self.auto_save_number))
                  print(my_text1)
                  f.write(my_text1)
    #显示缓存处理
     def show_cache_handle(self):
         self.show_cache=len(self.textEdit_4.toPlainText())#所有字符
         self.all_cache.setText( str(self.show_cache))
         print('当前已保存值'+str(self.show_cache2))
         print('设置值'+str(self.auto_save_number))
         print('总缓存'+str(self.show_cache))
         
         if self.show_cache-self.show_cache2 >= self.auto_save_number and self.atuo_save_switch==True:#判断当前值减去储存值是否等于设定值
            self.auto_save_write_file()
              
            print('保存成功')

      #500万字节判定
         if self.action200.isChecked() and self.show_cache>=5000000:
             full_text=self.textEdit_4.toPlainText()
             cut_text=full_text[4000000:]
             self.cacheclean_switch=True
             self.auto_save_write_file()
             self.textEdit_4.clear()
             self.textEdit_4.setText(cut_text)
             #重新获取清空缓存后的当前值
             self.show_cache=len(self.textEdit_4.toPlainText())
             self.show_cache2=self.show_cache
             print('当前已保存值'+str(self.show_cache2))
             print('显示缓存为500万')
       #1千万字节判定
         if self.action500.isChecked()and self.show_cache>=10000000:
             full_text=self.textEdit_4.toPlainText()
             cut_text=full_text[9000000:]
             self.cacheclean_switch=True
             self.auto_save_write_file()
             
             
             self.textEdit_4.clear()
             self.textEdit_4.setText(cut_text)
             self.show_cache=len(self.textEdit_4.toPlainText())
             self.show_cache2=self.show_cache
             print('显示缓存为1000万')
      #2000千万字节判定
         if self.action1000.isChecked()and self.show_cache>=20000000:
             full_text=self.textEdit_4.toPlainText()
             cut_text=full_text[19000000:]
             self.cacheclean_switch=True
             self.auto_save_write_file()
             self.textEdit_4.clear()
             self.textEdit_4.setText(cut_text)
             self.show_cache=len(self.textEdit_4.toPlainText())
             self.show_cache2=self.show_cache
             print('显示缓存为2000万')
    #参数设置页面隐藏与显示
     def showhide_settingwindow(self):
         if self.function_setting.isChecked():
            self.frame_2.show()
         else:
            self.frame_2.hide()
    #显示串口其他设置窗口
     def serial_window_show(self):
         self.sw.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
         self.sw.show()
    
#普通和hex输入区切换     
     def input_area_change(self):
        
         if self.hex_send_button.isChecked():
             self.textEdit.setPlainText(self.input_hex_show)
             print('hex发送'+str(self.input_hex_show))
         else:
             self.textEdit.setPlainText(self.normal_text)
             print('普通发送'+str(self.normal_text))
 #定制发送hex检查
     def custom_hex_send(self,custom):
         if self.hex_send_button.isChecked():
            input_hex_text=custom
         #判断不为列表元素有1个时候再删除，保持永远只有一个数据
            if len(self.input_hex_list)>0:
                del self.input_hex_list[0]
            self.input_hex_list.append(input_hex_text)
         #遍历列表元素清除换行符使其成为一行好让正则匹配
            for iht in  self.input_hex_list:
                   iht1=iht.replace("\n","")
            input_hex_match=re.compile(r'[^0-9a-fA-F\s\t]')
            iht2=input_hex_match.findall(iht1)#用findall可以全局匹配
         #输出参数内容（可删除）
            b1=''.join(iht2)
            print(self.input_hex_list)
            print('列表转换'+iht1)
            print('非法字符数量'+str(len(iht2)))
            print('nimbi'+self.input_hex_show)
        #判断有否有非法字符，如果有弹窗，然后读取最后正确输入保存的内容当做撤回
            if len(iht2)>0:
              print('非法字符'+b1)
              QMessageBox.warning(self, 
                                 'hex字符输入错误',"不是有效的Hex字符，有效字符为[0-9],[a-z],[A-Z],[空格],请每两个字符最好空一个空格    ", 
                                  QMessageBox.Yes)
            else:
                self.sthread.work(custom,self.ser)
                self.sthread.start()

         else:  
                self.sthread.work(custom,self.ser)
                self.sthread.start()
               
#hex输入检查检查，正则匹配非法hex字符然后删除（光标有些问题，无法锁定最后更改位置）
     def input_hex_check(self):
         if self.hex_send_button.isChecked():
            input_hex_text=str(self.textEdit.toPlainText())
        
         #判断不为列表元素有1个时候再删除，保持永远只有一个数据

            if len(self.input_hex_list)>0:
                del self.input_hex_list[0]
            self.input_hex_list.append(input_hex_text)
         #遍历列表元素清除换行符使其成为一行好让正则匹配
            for iht in  self.input_hex_list:

                   iht1=iht.replace("\n","")
            input_hex_match=re.compile(r'[^0-9a-fA-F\s\t]')
            iht2=input_hex_match.findall(iht1)#用findall可以全局匹配

         #输出参数内容（可删除）
            b1=''.join(iht2)
            print(self.input_hex_list)
            print('列表转换'+iht1)
            print('非法字符数量'+str(len(iht2)))
            print('nimbi'+self.input_hex_show)

        #判断有否有非法字符，如果有弹窗，然后读取最后正确输入保存的内容当做撤回
            if len(iht2)>0:
             
              print('非法字符'+b1)
             
              QMessageBox.warning(self, 
                                 'hex字符输入错误',"不是有效的Hex字符，有效字符为[0-9],[a-z],[A-Z],[空格],请每两个字符最好空一个空格    ", 
                                  QMessageBox.Yes)
            
              self.textEdit.setPlainText(self.input_hex_show)
              #保持游标在最后
              self.textEdit.moveCursor(QTextCursor.End)
              
              

            else:
                print('正常')
                #输入正常的时候储存一次，保持为最新
                self.input_hex_show=input_hex_text
               
         else:
              self.normal_text=str(self.textEdit.toPlainText())

 #随意改变串口事件
     def combobox_port_change(self):
         
         print('sssssss')
         print('随意aaa'+str(self.combobox_switch))
         print('刷新串口bbb'+str(self.port_refresh_switch))
        
         if self.port_refresh_switch==3:#防止刷新事件调用
           
            print('66666666666666')

            
            try:
               
               if self.ser.isOpen():#!=self.portcomboBox_2.currentText():
                    self.combobox_switch=6
                    print('随意进入串口')
                    self.dtu_test=1
                    self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
                    self.port_change()
                    print('随意出来串口')
                  
                    self.combobox_switch=5
                    self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
                    print('随意2'+str(self.combobox_switch))
                    print('999999999999999')
                   
            except:#防止在开启串口刷新时候刷新错误的信息区分刷新状态时候的串口跟新和普通状态下的串口刷新
               
               if self.refresh_switch:
                    #锁切换状态下
                    self.refresh_switch=False
                    QMessageBox.warning(self, '警告',"串口已被打开！请检查", QMessageBox.Yes)
                    print('ccccccccccccccccccccc')
                    self.combobox_switch=5
                    self.dtu_test=0
                    self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
                    print('随意2'+str(self.combobox_switch))
             
              
               else:
                     self.port_close_open_5.setText('串口关闭')
                     print('ddddddddddddd')
                     self.label_16.setPixmap(QtGui.QPixmap("../icon/红灯.bmp"))#红灯提示
                     self.more_setting_2.setEnabled(True)
                     QMessageBox.warning(self, '警告',"串口已被打开或拔除！请检查", QMessageBox.Yes)
                     self.combobox_switch=5
                     self.dtu_test=0
                     self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
                     print('随意2'+str(self.combobox_switch))
                     
#定时接收处理      
     def receive_time(self):
         #使输入框的数一直为1，防止出现bug
            try:
                self.re_outtime=int(self.outtimeline_2.text())  
                print('超时时间'+str(self.re_outtime))
                self.re_outtime=self.re_outtime/1000#时间必须除1000
                self.frist_rthread.sleeptime(self.re_outtime)
            except: 
                self.outtimeline_2.setText('1')
    #dtu信息以及模式搜查
     def dtu_info_search(self):
         #关闭接收主线程做判断先然后再开回主线程
       if self.ser.isOpen():
          self.dtu_test=1
          self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
        
          print('开始搜查模式5555555555555555555555555555555555')
          self.ser.write(bytes('check\r\n',encoding='gbk')) #查询语句 
          time.sleep(0.1)#睡眠等待完整数据包获取
          
          dtu_receive=self.ser.readline()#读取睡眠后的缓冲区数据
          dtu_receive=str(dtu_receive)
          print(type(dtu_receive))
          if dtu_receive=="b''":

               QMessageBox.information(self, '在透传状态','DTU当前在透传状态中', QMessageBox.Yes)
               self.dtu_mode_show_2.setText("透传状态")
          if r"b'+ERR+Not AT CMD!Do Nothing!\r\n'" ==dtu_receive :#判断是否at命令中
                            
                            self.frist_rthread.sleeptime(0.03)
                            
                            self.dtu_mode_show_2.setText("AT设置状态")
                            #QMessageBox.information(self, '不在透传状态','DTU当前不在透传状态中', QMessageBox.Cancel)
                            self.ser.write(bytes('AT+ALL_PAR\r\n',encoding='gbk'))#查dturf参数
                            self.dtu2=1#开始判断dtu查询信息
          self.dtu_test=0           
          self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
          self.frist_rthread.start()
     

              
#串口接收处理
     def receive_handle(self, first_receive_data, qt_show_receive_data):
            #接收事件是串口打开后一直开启的，通过它检测串口是否中途拔出
                    #print('接收时间'+'['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']')
                    print(qt_show_receive_data)
                    self.serstr=str(first_receive_data)
                    #自动化测试2
                    #接收端回信息
                    if self.at2.model!=0:
                        if self.at2.model==2:
                            if 'send'and 'test'in self.serstr:
                                self.sthread.work(self.at2.random_text,self.ser)
                                self.sthread.start()
                                print('返回成功')
                    #发送端判断是否有接收端回的信息
                        if self.at2.model==1:
                            if 'receive'or 'test'  in self.serstr:
                                self.testtime.stop()
                                self.at2.send_limit=0
                      #DTU设置界面开启的时候再开启判断
                    if self.dtu_setting.isChecked():      
                        if self.dtu4==1:#保存后的判断
                             print('caooooosjdoisajdoajodhaoshdas')
                             if re.search(r"(POWER)", self.serstr):
                                    self.progressBar_2.setValue(100)
                                    print('重启成功78878787678667867867676767868768786767687687866646')
                                    self.frist_rthread.sleeptime(self.re_outtime)
                                    QMessageBox.information(self, 'DTU重启成功','DTU已重启成功', QMessageBox.Yes)
                                    self.progressBar_2.setValue(0)
                                    self.singalsave_6.setCheckState(False)
                                    self.singalsave_9.setCheckState(False)
                                    self.singalsave_10.setCheckState(False)
                                    self.singalsave_11.setCheckState(False)
                                    self.singalsave_12.setCheckState(False)
                                    self.singalsave_13.setCheckState(False)
                                    self.singalsave_14.setCheckState(False)
                                    self.dtu4=0 
                             if re.search(r"(\+OK\+SAVE)", self.serstr) and self.singalsave_6.isChecked():
                                 if self.dtu_set_bar_3.currentText()=='1200':
                                    self.baudrate_comboBox.setCurrentIndex(4)
                                 if self.dtu_set_bar_3.currentText()=='2400':
                                     self.baudrate_comboBox.setCurrentIndex(5)
                                 if self.dtu_set_bar_3.currentText()=='4800':
                                     self.baudrate_comboBox.setCurrentIndex(6)
                                 if self.dtu_set_bar_3.currentText()=='9600':
                                     self.baudrate_comboBox.setCurrentIndex(7)
                                 if self.dtu_set_bar_3.currentText()=='19200':
                                     self.baudrate_comboBox.setCurrentIndex(9)
                                 if self.dtu_set_bar_3.currentText()=='38400':
                                     self.baudrate_comboBox.setCurrentIndex(10)
                                 if self.dtu_set_bar_3.currentText()=='57600':
                                     self.baudrate_comboBox.setCurrentIndex(11)
                                 if self.dtu_set_bar_3.currentText()=='115200':
                                     self.baudrate_comboBox.setCurrentIndex(12)
                                 if self.dtu_set_bar_3.currentText()=='256000':
                                     self.baudrate_comboBox.setCurrentIndex(15)
                         #at命令进入退出的判断
                        if self.dtu1==1 :
                            #a=r"b'+ERR+Not AT CMD!Do Nothing!\r\n'"
                            if re.search(r"(\+ERR\+Not\s)(AT\s)(CMD\!)", self.serstr)  and self.nothing_num==0 :
                                 self.nothing_num+=1
                                 QMessageBox.information(self, '在AT设置状态中','在AT设置状态中或指令错误，请检查', QMessageBox.Yes)
                                 self.dtu_mode_show_2.setText("AT设置状态")
                                 self.dtu1=0
                            if r"b'+OK+PTM\r\n'"== self.serstr:
                                QMessageBox.information(self, '已退出AT设置状态','已退出AT设置状态', QMessageBox.Yes)
                                self.dtu_mode_show_2.setText("透传状态")
                            print('sasdadsaaaaaaaaaaaaaaa')
                            if r"b'+ok=AT MODE ACTIVE!\r\n'"== self.serstr:
                                QMessageBox.information(self, '进入AT设置状态成功','已进入AT设置状态', QMessageBox.Yes)
                                self.dtu_mode_show_2.setText("AT设置状态")
                                self.dtu1=0
                            print('进入了设置专区')
                            self.frist_rthread.sleeptime(self.re_outtime)
                            print(self.dtu1)
                       #查询dtu所有参数功能
                        if   self.dtu2==1:
                            #print('进入开始时间'+'['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']')
                            own_address = re.search(r'(\*MODULE_ADDR)(\s*\=\s*)(0X)(\d{1,99})',self.serstr)#查询自身地址
                            other_side_address= re.search(r'(\*DST_ADDR)(\s*\=\s*)(0X)(\d{1,99})',self.serstr) #查询对方地址
                            channel_number=re.search(r'(\*RF_FREQ)(\s*\=\s*)(\d{1,99}\.\d{1,99})',self.serstr)#查询信道
                            communication_rate=re.search(r'(\*RF_DR)(\s*\=\s*)(\d{1,99})',self.serstr)#查询通讯速率
                            dtu_baudrate=re.search(r'(\*UART_BANDRATE)(\s*\=\s*)(\d{1,99})',self.serstr)#查波特率
                            dtumode=re.search(r'(\*DTU_MODE)(\s*\=\s*)([0-9a-zA-Z\_]*)',self.serstr)#查询当前模式
                            dtu_uid=re.search(r'(\*UID)(\s*\=\s*)([0-9a-zA-Z\_]*)',self.serstr)#查询当前uid
                            #查询固件版本
                            dtu_firmware=re.search(r'(\*DTU\d{1,9999}\_VER)(\s*\=\s*)([0-9a-zA-Z\_\.]*)',self.serstr)
                            #1500查询超时发送时间
                            dtu_send_delaytime=re.search(r'(\*PACKET_COMBINED_TIME)(\=)(\d{1,99})',self.serstr)#查询延迟发送时间
                             #查询dtu固件
                            if dtu_firmware:
                               print('固件显示')
                               self.firmwareversion_14.setText(dtu_firmware.group(3))
                            #查询自身地址
                            if  own_address : 
                                print(own_address.group(3))
                                print('进入查询所有指令了111111111111')
                                print(self.serstr)
                                self.own_dtu_address_4.setText(own_address.group(4))
                            #查询对方地址
                            if other_side_address:
                                self.other_dtu_address_4.setText(other_side_address.group(4))
                                print('查询对方地址')
                                print(self.serstr)
                                print(other_side_address.group(4))
                            #查询工作频率
                            if  channel_number:
                                final_channel_number=float(channel_number.group(3))
                                self.work_mhz_4.setValue( final_channel_number)
                                print('查询工作信道')
                                print(self.serstr)
                                print(channel_number.group(3))
                            #查询通讯速率
                            if  communication_rate:
                                self.rf_speed_5.setText('DR'+communication_rate.group(3))
                                print('查询dr')
                                print(self.serstr)
                                print(communication_rate.group(3))
                            #查询波特率
                            if  dtu_baudrate:
                                self.dtu_bar_4.setText(dtu_baudrate.group(3))
                                print('查询波特率')
                                print(self.serstr)
                                print(dtu_baudrate.group(3))
                            #查询工作模式
                            if dtumode:
                                print('查询模式')
                                print(self.serstr)
                                print(dtumode.group(3))
                                if dtumode.group(3)=='HOST_MODE':#不接受广播模式
                                    self.mode_show_2.setText('HOST模式')
                                if dtumode.group(3)=='MASTER_SLAVE_REPEATER_MODE':#主从中继模式
                                    self.mode_show_2.setText('主从中继模式')
                                if dtumode.group(3)=='SIMPLE_ROUTER_MODE':#简单路由模式
                                    self.mode_show_2.setText('简单路由模式')
                                if dtumode.group(3)=='GENERAL_MODE':#普通模式
                                    self.mode_show_2.setText('普通透传模式')
                                if dtumode.group(3)=='SIMPLE_REPEATER_MODE':#简单中继模式
                                    self.mode_show_2.setText('简单中继模式')
                                if dtumode.group(3)=='LOOP_MODE':#回环模式
                                    self.mode_show_2.setText('回环模式')
                                if self.dtu1200_2.isChecked():#1200的结束
                                     self.frist_rthread.sleeptime(self.re_outtime)
                                     print('1200的结束')
                                     self.dtu2=0#结束查询
                            #查询uid
                            if  dtu_uid:
                                print('uid_显示')
                                self.uid_2.setText(dtu_uid.group(3))
 
                            #查询dtu超时时间
                            if dtu_send_delaytime:
                                self.data_time_2.setText(dtu_send_delaytime.group(3))
                                self.frist_rthread.sleeptime(self.re_outtime)
                                print('1500结束')
                                self.dtu2=0#结束查询
                       
 #接收显示部分
                    self.receive_numbers=int(self.receive_numbers)+((len(first_receive_data)))#计算收到的字节
                    single_receive_numbers=str(len(first_receive_data))#单次接收
                    self.receive_numbers=str(self.receive_numbers)#统计接收
                    #self.hardware_real_time=hardware_real_time#硬件实时时间
                    #print(hardware_real_time)#此硬件实时已经处理好
                    self.receive_number_3.setText(self.receive_numbers)#显示统计接收字节
                    self.show_cache_handle()#调用显示缓存处理
                    self.lineEdit_5.setText(single_receive_numbers)#显示单个接收字节
                    self.received_strip+=1#接收条数
                    self.receive_number_2.setText(str(self.received_strip))
                    self.textEdit_4.append(qt_show_receive_data)
                    self.textEdit_4.moveCursor(QTextCursor.End)#控制输出光标,保持底部显示





#输入区字符预处理（剔除hex发送非法字符和缺位情况），预处理完后交给PYQT多线程进行数据转换
     def send_ready_send(self):
         if self.ser.isOpen():
           self.text_input=str(self.textEdit.toPlainText())
           self.sthread.work(self.text_input, self.ser)#把数据转进去多线程里面处理
           self.sthread.start()
        
#串口发送数据出去
     def send_out(self,show_data,send_data):
         self.textEdit_4.append(show_data)#将处理好的数据放进pyqt组件显示
         self.textEdit_4.moveCursor(QTextCursor.End)#控制输出光标，保持底部显示
         self.send_numbers=int(self.send_numbers)+len(send_data)#统计发送字符
         single_send_numbers=str(len(send_data))
         self.send_numbers=str(self.send_numbers)#累计统计发送字符
         self.send_strip+=1
         self.lineEdit_6.setText(single_send_numbers)#添加进单个发送显示
         self.send_number_3.setText(str(self.send_strip))#发送条数显示
         self.send_number_4.setText(self.send_numbers)#添加进累计发送显示
         self.show_cache_handle()#调用显示缓存处理
         if self.at2.model==1 and self.at2.send_limit<1:#发送模式且只有一个计时器存在
             self.at2.send_limit+=1
             self.testtime.start(self.at2.response_time)#计时器开启(响应时间）
         
            
           

    

 #定时发送预处理事件   
     def timing_send(self):
         #判断定时发送开关是否开启来控制定时发送 
                if self.timingswitch.isChecked() :
                     #检查输入框是否有输入值
                    try:
                            self.timing.setEnabled(False)
                            timings=int(self.timing.text()) 
                            self.timer.start(timings)
                    except:
                            self.timingswitch.setChecked(False)
                            #弹窗提示输入输入框数值
                            QMessageBox.warning(self, '警告',"请输入数值", QMessageBox.Yes)
                else:
                        self.timer.stop()
                        self.timing.setEnabled(True)          
 #控制串口关闭和开启
     def port_open_close(self):
         #判断串口是否开启来控制串口开启和定时发送
         if self.ser.isOpen():#关闭
            self.port_switch=2
            self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
            #执行过程
            self.more_setting_2.setEnabled(True)
            self.port_close_open_5.setText('串口打开')
            self.label_16.setPixmap(QtGui.QPixmap("../icon/红灯.bmp"))#红灯提示
            self.port_open()#调用串口开启事件
            self.timingswitch.setChecked(False)#关闭串口时关闭定时发送
            self.receiveswitch=False#关闭串口时关闭定时发送
            self.receive_time()#调用定时发送
            self.port_switch=1
            self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
         else:#开启
             self.more_setting_2.setEnabled(False)
             self.port_close_open_5.setText('串口关闭')
             self.label_16.setPixmap(QtGui.QPixmap("../icon/绿灯.bmp"))#绿灯提示
             self.port_open()#调用串口开启函数
            
             self.receiveswitch=True#开启串口时开启定时发送
             self.receive_time()#调用定时发送
             self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
             
             self.frist_rthread.start()#开启串口数据接收线程
#刷新串口事件
     def port_refresh_event(self):
         self.num_refresh+=1     
         print('刷新串口111'+str(self.port_refresh_switch))
         self.port_refresh_switch=4#刷新串口锁
         self.dtu_test=1
         self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
         if self.ser.isOpen:
            self.refresh_switch=True#防止在开启串口时候进行刷新，显示错误信息
         if self.num_refresh==1:#开始指定波特率
             self.baudrate_comboBox.setCurrentIndex(12)
             self.ser.baudrate=int(self.baudrate_comboBox.currentText())#波特率
         self.portcomboBox_2.clear()#清除多余的串口
         self.port_cheak()
         #刷新完串口应该关闭
         if self.num_refresh>1:
            QMessageBox.warning(self, '刷新成功',"串口刷新成功", QMessageBox.Yes)
            if self.ser.isOpen():
                self.textEdit_4.append('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+"▼▼▼▼▼"+str(self.ser.port)+'串口关闭成功')
         self.ser.close()
         self.more_setting_2.setEnabled(True)
         self.port_close_open_5.setText('串口打开')
         self.label_16.setPixmap(QtGui.QPixmap("../icon/红灯.bmp"))#红灯提示
         print('刷新串口222'+str(self.port_refresh_switch))
         self.port_refresh_switch=3#刷新串口锁
         time.sleep(0.005)#防止线程刷新来不及
         self.dtu_test=0
         self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)
#串口中途拔出事件
     def sierial_break(self):
                print('nijij')
                print('刷新串口'+str(self.port_refresh_switch))
                print('开关'+str(self.port_switch))
                print('随意'+str(self.combobox_switch))
                self.ser.close()#再停串口
                self.port_close_open_5.setText('串口打开')
                self.label_16.setPixmap(QtGui.QPixmap("../icon/红灯.bmp"))#红灯提示
                self.textEdit_4.append('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+"▼▼▼▼▼"+str(self.ser.port)+'串口被拔出')
                QMessageBox.warning(self, '警告',"串口不正常，可能被拔出",QMessageBox.Yes)
                self.port_refresh_event()
                print('串口情况'+str(self.ser.is_open))#输出串口是否开启
                print(self.ser)#输出串口信息
#不通过关闭串口改变串口事件
     def port_change(self):
         #先关闭串口，再停定时接收，变关闭字符，输出信息，然后获取新的串口号信息，打开串口，输出信息，变打开字符
         self.ser.close()
         self.port_close_open_5.setText('串口打开')
         self.label_16.setPixmap(QtGui.QPixmap("../icon/红灯.bmp"))#红灯提示
         print('sssssssssssssssssssssss222222222222222222')
         self.textEdit_4.append('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+"▼▼▼▼▼"+str(self.ser.port)+'串口关闭成功')
         print('串口情况'+str(self.ser.is_open))#输出串口是否开启
         print(self.ser)#输出串口信息
         self.ser.port=self.rematch_com()
         self.ser.open()
         print('sssssssssssssss')
         self.textEdit_4.append('['+str(datetime.datetime.now().strftime('%H:%M:%S.%f'))+']'+"★★★★★"+str(self.ser.port)+'打开成功')
         self.port_close_open_5.setText('串口关闭')
         self.label_16.setPixmap(QtGui.QPixmap("../icon/绿灯.bmp"))#红灯提示
         print('串口情况'+str(self.ser.is_open))#输出串口是否开启
         print(self.ser)#输出串口信息
         print('0000000000000000000')
         self.dtu_test=0
         self.frist_rthread.first_work(self.ser,self.port_switch,self.port_refresh_switch,self.combobox_switch,self.dtu_test)#硬锁
         self.frist_rthread.start()#开启串口数据接收线程
    