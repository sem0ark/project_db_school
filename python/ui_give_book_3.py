# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver_1_give_book.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GiveBook(object):
    def setupUi(self, GiveBook):
        GiveBook.setObjectName("GiveBook")
        GiveBook.resize(458, 245)
        self.verticalLayout = QtWidgets.QVBoxLayout(GiveBook)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(GiveBook)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_userID = QtWidgets.QLineEdit(GiveBook)
        self.lineEdit_userID.setObjectName("lineEdit_userID")
        self.horizontalLayout_2.addWidget(self.lineEdit_userID)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout_3.setSpacing(24)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(GiveBook)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_exemplarID = QtWidgets.QLineEdit(GiveBook)
        self.lineEdit_exemplarID.setObjectName("lineEdit_exemplarID")
        self.horizontalLayout_3.addWidget(self.lineEdit_exemplarID)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(GiveBook)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_givenTime = QtWidgets.QLineEdit(GiveBook)
        self.lineEdit_givenTime.setObjectName("lineEdit_givenTime")
        self.horizontalLayout.addWidget(self.lineEdit_givenTime)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(GiveBook)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(GiveBook)
        self.buttonBox.accepted.connect(GiveBook.accept)
        self.buttonBox.rejected.connect(GiveBook.reject)
        QtCore.QMetaObject.connectSlotsByName(GiveBook)

    def retranslateUi(self, GiveBook):
        _translate = QtCore.QCoreApplication.translate
        GiveBook.setWindowTitle(_translate("GiveBook", "Выдать книгу"))
        self.label.setText(_translate("GiveBook", "ID пользователя"))
        self.lineEdit_userID.setToolTip(_translate("GiveBook", "<html><head/><body><p>Введите ID пользователя</p></body></html>"))
        self.label_2.setText(_translate("GiveBook", "ID экземпляра"))
        self.lineEdit_exemplarID.setToolTip(_translate("GiveBook", "<html><head/><body><p>Введите ID экземпляра данной книги</p></body></html>"))
        self.label_3.setText(_translate("GiveBook", "Срок выдачи\n"
"(в днях)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GiveBook = QtWidgets.QDialog()
    ui = Ui_GiveBook()
    ui.setupUi(GiveBook)
    GiveBook.show()
    sys.exit(app.exec_())
