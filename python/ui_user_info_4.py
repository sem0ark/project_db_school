# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver_1_user_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserInfo(object):
    def setupUi(self, UserInfo):
        UserInfo.setObjectName("UserInfo")
        UserInfo.resize(601, 260)
        font = QtGui.QFont()
        font.setPointSize(9)
        UserInfo.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(UserInfo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(UserInfo)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 577, 236))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.userID = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.userID.setObjectName("userID")
        self.horizontalLayout_8.addWidget(self.userID)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        # self.given_table_place = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.given_table_place.setObjectName("given_table_place")
        # self.gridLayout.addWidget(self.given_table_place, 7, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.sName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sName.sizePolicy().hasHeightForWidth())
        self.sName.setSizePolicy(sizePolicy)
        self.sName.setObjectName("sName")
        self.horizontalLayout_3.addWidget(self.sName)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.fName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fName.sizePolicy().hasHeightForWidth())
        self.fName.setSizePolicy(sizePolicy)
        self.fName.setObjectName("fName")
        self.horizontalLayout_2.addWidget(self.fName)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.pName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pName.sizePolicy().hasHeightForWidth())
        self.pName.setSizePolicy(sizePolicy)
        self.pName.setObjectName("pName")
        self.horizontalLayout_4.addWidget(self.pName)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.regData = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.regData.setObjectName("regData")
        self.horizontalLayout_9.addWidget(self.regData)
        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(UserInfo)
        QtCore.QMetaObject.connectSlotsByName(UserInfo)

    def retranslateUi(self, UserInfo):
        _translate = QtCore.QCoreApplication.translate
        UserInfo.setWindowTitle(_translate("UserInfo", "Информация о пользователе"))
        self.label_8.setText(_translate("UserInfo", "ID: "))
        self.userID.setText(_translate("UserInfo", "TextLabel"))
        # self.given_table_place.setText(_translate("UserInfo", "PushButton"))
        self.label_4.setText(_translate("UserInfo", "Фамилия: "))
        self.sName.setText(_translate("UserInfo", "TextLabel"))
        self.label.setText(_translate("UserInfo", "Имя: "))
        self.fName.setText(_translate("UserInfo", "TextLabel"))
        self.label_7.setText(_translate("UserInfo", "Отчество: "))
        self.pName.setText(_translate("UserInfo", "TextLabel"))
        self.label_6.setText(_translate("UserInfo", "Дата рег. : "))
        self.regData.setText(_translate("UserInfo", "TextLabel"))
        self.label_2.setText(_translate("UserInfo", "Выданные книги: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserInfo = QtWidgets.QDialog()
    ui = Ui_UserInfo()
    ui.setupUi(UserInfo)
    UserInfo.show()
    sys.exit(app.exec_())
