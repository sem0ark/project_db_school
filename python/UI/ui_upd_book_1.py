from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateBook(object):
    def setupUi(self, UpdateBook,
                name, year, publisher_name, publisher_town, pages, subject,
                genres, authors, UDK, BBK, ISBN, authorMark):
        UpdateBook.setObjectName("UpdateBook")
        UpdateBook.resize(700, 550)
        font = QtGui.QFont()
        font.setPointSize(10)
        UpdateBook.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(UpdateBook)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.lineEdit_year = QtWidgets.QLineEdit(str(year), UpdateBook)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.horizontalLayout_6.addWidget(self.lineEdit_year)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.lineEdit_pages = QtWidgets.QLineEdit(str(pages), UpdateBook)
        self.lineEdit_pages.setObjectName("lineEdit_pages")
        self.horizontalLayout_7.addWidget(self.lineEdit_pages)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.lineEdit_name = QtWidgets.QLineEdit(name, UpdateBook)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_9.addWidget(self.lineEdit_name)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_subject = QtWidgets.QLineEdit(subject, UpdateBook)
        self.lineEdit_subject.setObjectName("lineEdit_subject")
        self.horizontalLayout_8.addWidget(self.lineEdit_subject)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.lineEdit_publisherName = QtWidgets.QLineEdit(publisher_name, UpdateBook)
        self.lineEdit_publisherName.setObjectName("lineEdit_publisherName")
        self.horizontalLayout_13.addWidget(self.lineEdit_publisherName)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.lineEdit_publisherTown = QtWidgets.QLineEdit(publisher_town, UpdateBook)
        self.lineEdit_publisherTown.setObjectName("lineEdit_publisherTown")
        self.horizontalLayout_12.addWidget(self.lineEdit_publisherTown)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_authors = QtWidgets.QLineEdit(','.join(authors), UpdateBook)
        self.lineEdit_authors.setObjectName("lineEdit_authors")
        self.horizontalLayout_5.addWidget(self.lineEdit_authors)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_genres = QtWidgets.QLineEdit(','.join(genres), UpdateBook)
        self.lineEdit_genres.setObjectName("lineEdit_genres")
        self.horizontalLayout_2.addWidget(self.lineEdit_genres)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_9 = QtWidgets.QLabel(UpdateBook)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_18.addWidget(self.label_9)
        self.lineEdit_UDK = QtWidgets.QLineEdit(UDK, UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_UDK.setFont(font)
        self.lineEdit_UDK.setObjectName("lineEdit_UDK")
        self.horizontalLayout_18.addWidget(self.lineEdit_UDK)
        self.label_10 = QtWidgets.QLabel(UpdateBook)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.lineEdit_BBK = QtWidgets.QLineEdit(BBK, UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_BBK.setFont(font)
        self.lineEdit_BBK.setObjectName("lineEdit_BBK")
        self.horizontalLayout_18.addWidget(self.lineEdit_BBK)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_11 = QtWidgets.QLabel(UpdateBook)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        self.lineEdit_ISBN = QtWidgets.QLineEdit(ISBN, UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_ISBN.setFont(font)
        self.lineEdit_ISBN.setObjectName("lineEdit_ISBN")
        self.horizontalLayout_14.addWidget(self.lineEdit_ISBN)
        self.label_12 = QtWidgets.QLabel(UpdateBook)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.lineEdit_authorMark = QtWidgets.QLineEdit(authorMark, UpdateBook)
        self.lineEdit_authorMark.setObjectName("lineEdit_authorMark")
        self.horizontalLayout_14.addWidget(self.lineEdit_authorMark)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(UpdateBook)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(UpdateBook)
        self.buttonBox.accepted.connect(UpdateBook.accept)
        self.buttonBox.rejected.connect(UpdateBook.reject)
        QtCore.QMetaObject.connectSlotsByName(UpdateBook)

    def retranslateUi(self, UpdateBook):
        _translate = QtCore.QCoreApplication.translate
        UpdateBook.setWindowTitle(_translate("UpdateBook", "??????. ??????????"))
        self.label.setText(_translate("UpdateBook", "?????? \n"
"??????????????"))
        self.lineEdit_year.setToolTip(_translate("UpdateBook", "<html><head/><body><p>?????????????? ?????? ?????????????? ???????????? ??????????</p></body></html>"))
        self.label_2.setText(_translate("UpdateBook", "??????-???? \n"
"??????????????"))
        self.lineEdit_pages.setToolTip(_translate("UpdateBook", "<html><head/><body><p>?????????????? ??????-???? ?????????????? ?? ??????????</p></body></html>"))
        self.label_3.setText(_translate("UpdateBook", "????????????????"))
        self.lineEdit_name.setToolTip(_translate("UpdateBook", "<html><head/><body><p>?????????????? ???????????????? ??????????</p></body></html>"))
        self.label_8.setText(_translate("UpdateBook", "????????????????????\n"
"??????????????"))
        self.lineEdit_subject.setToolTip(_translate("UpdateBook", "<html><head/><body><p>?????????????? ???????????????????? ?????????????? ??????????</p><p>????????????????: ????????????</p></body></html>"))
        self.label_6.setText(_translate("UpdateBook", "????????????????????????"))
        self.lineEdit_publisherName.setToolTip(_translate("UpdateBook", "<html><head/><body><p>?????????????? ???????????????? ????????????????????????</p></body></html>"))
        self.label_7.setText(_translate("UpdateBook", "??????????"))
        self.lineEdit_publisherTown.setToolTip(_translate("UpdateBook", "<html><head/><body><p>?????????????? ?????????? ????????????????????????</p></body></html>"))
        self.label_4.setText(_translate("UpdateBook", "??????????(??)\n"
"(??????)"))
        self.lineEdit_authors.setToolTip(_translate("UpdateBook", "<html><head/><body><p>?????????????? ?????????? &quot;,&quot;</p></body></html>"))
        self.label_5.setText(_translate("UpdateBook", "????????(??)"))
        self.lineEdit_genres.setToolTip(_translate("UpdateBook", "<html><head/><body><p>?????????????? ?????????? &quot;,&quot;</p></body></html>"))
        self.label_9.setText(_translate("UpdateBook", "??????"))
        self.label_10.setText(_translate("UpdateBook", "??????"))
        self.label_11.setText(_translate("UpdateBook", "ISBN"))
        self.label_12.setText(_translate("UpdateBook", "??????????????????\n"
"????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateBook = QtWidgets.QDialog()
    ui = Ui_UpdateBook()
    ui.setupUi(UpdateBook, 'Physics 10 garde', 2001, '??????????', '????????????', 200, 'physics',
        ['study','study2','study3'],
        ['zxczxc dasd xcvx','zhhxczxc dassdd xggdcvx','zxffczxc dassdd xcvx'],
        '121kbf12l', '23780=-+-[]:????????????', '23798-231-1231-11', '??48')
    UpdateBook.show()
    sys.exit(app.exec_())
