# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver_1_reg_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterReader(object):
    def setupUi(self, RegisterReader):
        RegisterReader.setObjectName("RegisterReader")
        RegisterReader.resize(600, 194)
        font = QtGui.QFont()
        font.setPointSize(12)
        RegisterReader.setFont(font)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(RegisterReader)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, 10, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.surname = QtWidgets.QLabel(RegisterReader)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.surname.setFont(font)
        self.surname.setObjectName("surname")
        self.horizontalLayout_5.addWidget(self.surname)
        self.lineEdit_sName = QtWidgets.QLineEdit(RegisterReader)
        self.lineEdit_sName.setObjectName("lineEdit_sName")
        self.horizontalLayout_5.addWidget(self.lineEdit_sName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.first_name = QtWidgets.QLabel(RegisterReader)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.first_name.setFont(font)
        self.first_name.setObjectName("first_name")
        self.horizontalLayout_4.addWidget(self.first_name)
        self.lineEdit_fName = QtWidgets.QLineEdit(RegisterReader)
        self.lineEdit_fName.setObjectName("lineEdit_fName")
        self.horizontalLayout_4.addWidget(self.lineEdit_fName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.p_name = QtWidgets.QLabel(RegisterReader)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p_name.setFont(font)
        self.p_name.setObjectName("p_name")
        self.horizontalLayout_6.addWidget(self.p_name)
        self.lineEdit_pName = QtWidgets.QLineEdit(RegisterReader)
        self.lineEdit_pName.setObjectName("lineEdit_pName")
        self.horizontalLayout_6.addWidget(self.lineEdit_pName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(RegisterReader)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(RegisterReader)
        self.buttonBox.accepted.connect(RegisterReader.accept)
        self.buttonBox.rejected.connect(RegisterReader.reject)
        QtCore.QMetaObject.connectSlotsByName(RegisterReader)

    def retranslateUi(self, RegisterReader):
        _translate = QtCore.QCoreApplication.translate
        RegisterReader.setWindowTitle(_translate("RegisterReader", "??????????. ????????????????????????"))
        self.surname.setText(_translate("RegisterReader", "??????????????"))
        self.lineEdit_sName.setToolTip(_translate("RegisterReader", "<html><head/><body><p><span style=\" font-size:8pt;\">?????????????? ?????????????? ???????????????????????? (??????????????)</span></p></body></html>"))
        self.first_name.setText(_translate("RegisterReader", "??????"))
        self.lineEdit_fName.setToolTip(_translate("RegisterReader", "<html><head/><body><p><span style=\" font-size:8pt;\">?????????????? ?????? ???????????????????????? (??????????????)</span></p></body></html>"))
        self.p_name.setText(_translate("RegisterReader", "????????????????"))
        self.lineEdit_pName.setToolTip(_translate("RegisterReader", "<html><head/><body><p><span style=\" font-size:8pt;\">?????????????? ???????????????? ???????????????????????? (??????????????)</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterReader = QtWidgets.QDialog()
    ui = Ui_RegisterReader()
    ui.setupUi(RegisterReader)
    RegisterReader.show()
    sys.exit(app.exec_())
