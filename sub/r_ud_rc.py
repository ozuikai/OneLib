# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'r_ud.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_r_ud_Form(object):
    def setupUi(self, r_ud_Form):
        r_ud_Form.setObjectName("r_ud_Form")
        r_ud_Form.resize(410, 369)
        self.gridLayout_2 = QtWidgets.QGridLayout(r_ud_Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_18 = QtWidgets.QLabel(r_ud_Form)
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/Icon/load.png"))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.label_18)
        self.load_photo_btn = QtWidgets.QPushButton(r_ud_Form)
        self.load_photo_btn.setEnabled(True)
        self.load_photo_btn.setAutoFillBackground(False)
        self.load_photo_btn.setAutoRepeat(False)
        self.load_photo_btn.setObjectName("load_photo_btn")
        self.verticalLayout_4.addWidget(self.load_photo_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(r_ud_Form)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(r_ud_Form)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(r_ud_Form)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_11 = QtWidgets.QLabel(r_ud_Form)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_9 = QtWidgets.QLabel(r_ud_Form)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(r_ud_Form)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(r_ud_Form)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(r_ud_Form)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(r_ud_Form)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(r_ud_Form)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_17 = QtWidgets.QLabel(r_ud_Form)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(r_ud_Form)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.id_le = QtWidgets.QLineEdit(r_ud_Form)
        self.id_le.setEnabled(False)
        self.id_le.setObjectName("id_le")
        self.verticalLayout_2.addWidget(self.id_le)
        self.name_le = QtWidgets.QLineEdit(r_ud_Form)
        self.name_le.setObjectName("name_le")
        self.verticalLayout_2.addWidget(self.name_le)
        self.sex_cb = QtWidgets.QComboBox(r_ud_Form)
        self.sex_cb.setObjectName("sex_cb")
        self.sex_cb.addItem("")
        self.sex_cb.addItem("")
        self.verticalLayout_2.addWidget(self.sex_cb)
        self.type_cb = QtWidgets.QComboBox(r_ud_Form)
        self.type_cb.setObjectName("type_cb")
        self.type_cb.addItem("")
        self.type_cb.addItem("")
        self.type_cb.addItem("")
        self.type_cb.addItem("")
        self.type_cb.addItem("")
        self.verticalLayout_2.addWidget(self.type_cb)
        self.dept_le = QtWidgets.QLineEdit(r_ud_Form)
        self.dept_le.setObjectName("dept_le")
        self.verticalLayout_2.addWidget(self.dept_le)
        self.phone_le = QtWidgets.QLineEdit(r_ud_Form)
        self.phone_le.setObjectName("phone_le")
        self.verticalLayout_2.addWidget(self.phone_le)
        self.email_le = QtWidgets.QLineEdit(r_ud_Form)
        self.email_le.setObjectName("email_le")
        self.verticalLayout_2.addWidget(self.email_le)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.date_le = QtWidgets.QLineEdit(r_ud_Form)
        self.date_le.setEnabled(False)
        self.date_le.setObjectName("date_le")
        self.horizontalLayout_3.addWidget(self.date_le)
        self.date_cb = QtWidgets.QCheckBox(r_ud_Form)
        self.date_cb.setCheckable(True)
        self.date_cb.setObjectName("date_cb")
        self.horizontalLayout_3.addWidget(self.date_cb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.status_cb = QtWidgets.QComboBox(r_ud_Form)
        self.status_cb.setObjectName("status_cb")
        self.status_cb.addItem("")
        self.status_cb.addItem("")
        self.status_cb.addItem("")
        self.verticalLayout_2.addWidget(self.status_cb)
        self.bwqty_le = QtWidgets.QLineEdit(r_ud_Form)
        self.bwqty_le.setEnabled(False)
        self.bwqty_le.setObjectName("bwqty_le")
        self.verticalLayout_2.addWidget(self.bwqty_le)
        self.psw_le = QtWidgets.QLineEdit(r_ud_Form)
        self.psw_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.psw_le.setObjectName("psw_le")
        self.verticalLayout_2.addWidget(self.psw_le)
        self.roles_cb = QtWidgets.QComboBox(r_ud_Form)
        self.roles_cb.setObjectName("roles_cb")
        self.roles_cb.addItem("")
        self.roles_cb.addItem("")
        self.roles_cb.addItem("")
        self.roles_cb.addItem("")
        self.roles_cb.addItem("")
        self.verticalLayout_2.addWidget(self.roles_cb)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.update_btn = QtWidgets.QPushButton(r_ud_Form)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout_4.addWidget(self.update_btn)
        self.delete_btn = QtWidgets.QPushButton(r_ud_Form)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_4.addWidget(self.delete_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(r_ud_Form)
        self.type_cb.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(r_ud_Form)

    def retranslateUi(self, r_ud_Form):
        _translate = QtCore.QCoreApplication.translate
        r_ud_Form.setWindowTitle(_translate("r_ud_Form", "详情"))
        self.load_photo_btn.setText(_translate("r_ud_Form", "载入照片"))
        self.label_6.setText(_translate("r_ud_Form", "编号："))
        self.label_7.setText(_translate("r_ud_Form", "姓名："))
        self.label_8.setText(_translate("r_ud_Form", "性别："))
        self.label_11.setText(_translate("r_ud_Form", "类别："))
        self.label_9.setText(_translate("r_ud_Form", "单位名称："))
        self.label_10.setText(_translate("r_ud_Form", "电话号码："))
        self.label_12.setText(_translate("r_ud_Form", "电子邮箱："))
        self.label_13.setText(_translate("r_ud_Form", "登记日期："))
        self.label_14.setText(_translate("r_ud_Form", "证件状态："))
        self.label_15.setText(_translate("r_ud_Form", "已借数量："))
        self.label_17.setText(_translate("r_ud_Form", "登陆密码："))
        self.label_16.setText(_translate("r_ud_Form", "管理角色："))
        self.sex_cb.setItemText(0, _translate("r_ud_Form", "男"))
        self.sex_cb.setItemText(1, _translate("r_ud_Form", "女"))
        self.type_cb.setItemText(0, _translate("r_ud_Form", "老师"))
        self.type_cb.setItemText(1, _translate("r_ud_Form", "博士生"))
        self.type_cb.setItemText(2, _translate("r_ud_Form", "硕士生"))
        self.type_cb.setItemText(3, _translate("r_ud_Form", "本科生"))
        self.type_cb.setItemText(4, _translate("r_ud_Form", "专科生"))
        self.date_le.setText(_translate("r_ud_Form", "更新为当前时间"))
        self.date_cb.setText(_translate("r_ud_Form", "更新"))
        self.status_cb.setItemText(0, _translate("r_ud_Form", "有效"))
        self.status_cb.setItemText(1, _translate("r_ud_Form", "挂失"))
        self.status_cb.setItemText(2, _translate("r_ud_Form", "注销"))
        self.roles_cb.setItemText(0, _translate("r_ud_Form", "读者"))
        self.roles_cb.setItemText(1, _translate("r_ud_Form", "借书证管理员"))
        self.roles_cb.setItemText(2, _translate("r_ud_Form", "图书管理员"))
        self.roles_cb.setItemText(3, _translate("r_ud_Form", "借阅管理员"))
        self.roles_cb.setItemText(4, _translate("r_ud_Form", "系统管理员"))
        self.update_btn.setText(_translate("r_ud_Form", "更新信息"))
        self.delete_btn.setText(_translate("r_ud_Form", "删除用户"))

import img_rcc_rc
