
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from auto_save_setting import *


class auto_save_window(QDialog,Ui_Dialog):#串口窗口
     aw_output = pyqtSignal(str,int,bool)
     def __init__(self):#串口窗口的执行
         super(auto_save_window,self).__init__()
         self.setupUi(self)
         self.auto_filename=''#保存路径
         self.save_auto_filename=""
         self.auto_time=0 #设置的时间
         self.save_numbers.setValidator(QIntValidator(0,9999999999999))#限制超时时间输入框为整数型数据
         self.atuosave_switch=False
     def  serial_window_singal (self):
         self.cancel.clicked.connect(self.no_save)#取消保存事件
         self.sure.clicked.connect(self.save)#保存事件
         self.save_path_button.clicked.connect(self.auto_file_save)#调用保存文件路径
#取消操作
     def no_save(self):
         self.save_numbers.setText(str(self.auto_time))
         self.save_path.setText(self.save_auto_filename)
         self.close()
         self.atuosave_switch=False
         #self.auto_save.setChecked(False)
#保存操作
     def save(self):
       
         #判断是否为非0值
         if len(self.save_numbers.text())>0 and int(self.save_numbers.text())-1==-1:
                QMessageBox.warning(self, '警告',"每多少字节参数请设置一个非0值，", QMessageBox.Cancel)
               
         #判断是否有输入值
         elif len(self.save_path.text())<1 or len(self.save_numbers.text())<1: 
              QMessageBox.warning(self, '警告',"请检查参数是否设置正常，", QMessageBox.Cancel)
            
         else:
                 # QMessageBox.information(self, '设置成功',"设置成功，自动保存功能开启", QMessageBox.Cancel)
                  self.save_auto_filename=self.auto_filename[0]#保存路径
                  self.auto_time=int(self.save_numbers.text())#保存设置字节数
                  self.close()
                  self.atuosave_switch=True
                  self.aw_output.emit(self.save_auto_filename,self.auto_time,self.atuosave_switch)#传递保存设置

                  
        
#保存文件路径
     def auto_file_save(self):
         
         self.auto_filename=QFileDialog.getSaveFileName(self,#这里为st类型
                                    "文件保存",#名称
                                    "./autosave",#目标地址
                                    "Text Files (*.txt)")#文件类型
         print(self.auto_filename)
         if len(self.auto_filename[0])<=1:
             print(len(self.auto_filename[0]))

             
             QMessageBox.warning(self, '警告',"保存目录未指定开启失败，请重新开启", QMessageBox.Cancel)
             self.save_path.clear()
             #self.auto_save.setChecked(False)
                  
            #QMessageBox.warning(self, '自动','未指定保存目录', QMessageBox.Cancel)
         else:
             QMessageBox.information(self, '自动保存开启成功',"自动保存目录为"+str(self.auto_filename[0]), QMessageBox.Cancel)
             self.save_path.setText(self.auto_filename[0])
