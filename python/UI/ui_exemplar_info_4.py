# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ver_1_exemplar_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExemplarInfo(object):
    def setupUi(self, ExemplarInfo):
        ExemplarInfo.setObjectName("ExemplarInfo")
        ExemplarInfo.resize(530, 155)
        font = QtGui.QFont()
        font.setPointSize(9)
        ExemplarInfo.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(ExemplarInfo)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ExemplarInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.exemplarID = QtWidgets.QLabel(ExemplarInfo)
        self.exemplarID.setObjectName("exemplarID")
        self.horizontalLayout.addWidget(self.exemplarID)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(ExemplarInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.bookID = QtWidgets.QLabel(ExemplarInfo)
        self.bookID.setObjectName("bookID")
        self.horizontalLayout_3.addWidget(self.bookID)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(ExemplarInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.bookName = QtWidgets.QLabel(ExemplarInfo)
        self.bookName.setObjectName("bookName")
        self.horizontalLayout_4.addWidget(self.bookName)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)

        self.retranslateUi(ExemplarInfo)
        QtCore.QMetaObject.connectSlotsByName(ExemplarInfo)

    def retranslateUi(self, ExemplarInfo):
        _translate = QtCore.QCoreApplication.translate
        ExemplarInfo.setWindowTitle(_translate("ExemplarInfo", "???????????????????? ?? ????????????????????"))
        self.label.setText(_translate("ExemplarInfo", "ID ????????????????????: "))
        self.exemplarID.setText(_translate("ExemplarInfo", "TextLabel"))
        self.label_3.setText(_translate("ExemplarInfo", "ID ??????????: "))
        self.bookID.setText(_translate("ExemplarInfo", "TextLabel"))
        self.label_2.setText(_translate("ExemplarInfo", "???????????????? ??????????: "))
        self.bookName.setText(_translate("ExemplarInfo", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExemplarInfo = QtWidgets.QDialog()
    ui = Ui_ExemplarInfo()
    ui.setupUi(ExemplarInfo)
    ExemplarInfo.show()
    sys.exit(app.exec_())
