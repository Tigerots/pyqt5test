# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automation_test_setting.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(608, 620)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textnumber = QtWidgets.QLineEdit(Dialog)
        self.textnumber.setObjectName("textnumber")
        self.gridLayout.addWidget(self.textnumber, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.send_time = QtWidgets.QLineEdit(Dialog)
        self.send_time.setObjectName("send_time")
        self.gridLayout.addWidget(self.send_time, 5, 3, 1, 1)
        self.offtest = QtWidgets.QPushButton(Dialog)
        self.offtest.setObjectName("offtest")
        self.gridLayout.addWidget(self.offtest, 1, 0, 1, 1)
        self.show_model = QtWidgets.QLineEdit(Dialog)
        self.show_model.setText("")
        self.show_model.setObjectName("show_model")
        self.gridLayout.addWidget(self.show_model, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.lost_limit = QtWidgets.QLineEdit(Dialog)
        self.lost_limit.setObjectName("lost_limit")
        self.gridLayout.addWidget(self.lost_limit, 6, 3, 1, 1)
        self.auto_receive = QtWidgets.QPushButton(Dialog)
        self.auto_receive.setObjectName("auto_receive")
        self.gridLayout.addWidget(self.auto_receive, 0, 3, 1, 1)
        self.atuo_send = QtWidgets.QPushButton(Dialog)
        self.atuo_send.setObjectName("atuo_send")
        self.gridLayout.addWidget(self.atuo_send, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.responsetime = QtWidgets.QLineEdit(Dialog)
        self.responsetime.setObjectName("responsetime")
        self.gridLayout.addWidget(self.responsetime, 7, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "自动化测试（2）持续测试"))
        self.textnumber.setText(_translate("Dialog", "10"))
        self.label_3.setText(_translate("Dialog", "自动发送时间间隔/ms"))
        self.label.setText(_translate("Dialog", "当前端显示"))
        self.send_time.setText(_translate("Dialog", "100"))
        self.offtest.setText(_translate("Dialog", "关闭"))
        self.label_4.setText(_translate("Dialog", "丢失多少包为通讯失败"))
        self.lost_limit.setText(_translate("Dialog", "30"))
        self.auto_receive.setText(_translate("Dialog", "此为接收端"))
        self.atuo_send.setText(_translate("Dialog", "此为发送端"))
        self.label_2.setText(_translate("Dialog", "接收发送返回字节"))
        self.responsetime.setText(_translate("Dialog", "1000"))
        self.label_5.setText(_translate("Dialog", "超过多少ms没回答为丢一包"))

