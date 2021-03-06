from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from process import Process_signal
from validate import Validate_process
# sys.path.append('./ui/version_1_tagged/ui_2/')
import UI.ui_main_13           as ui_main
import UI.ui_reg_user_3       as ui_reg_user
import UI.ui_upd_user_1       as ui_upd_user
import UI.ui_reg_book_3       as ui_reg_book
import UI.ui_upd_book_1       as ui_upd_book
import UI.ui_give_book_3      as ui_give_book
import UI.ui_take_book_4      as ui_take_book
import UI.ui_reg_exemplar_5   as ui_reg_exemplar
import UI.ui_user_info_4      as ui_user_info
import UI.ui_book_info_6      as ui_book_info
import UI.ui_exemplar_info_4   as ui_exemplar_info
import UI.ui_add_time_3   as ui_add_time


class tag_Ui_MainWindow(QtWidgets.QWidget, ui_main.Ui_MainWindow):

    def setupUi(self, MainWindow, process, ctx):
        super().setupUi(MainWindow, ctx)
        # super().closeEvent = self.closeEvent

        # self.label_picture = QtWidgets.QLabel(MainWindow)
        # self.label_picture.setPixmap(QtGui.QPixmap("owl_1.png"))
        # # self.label_picture.setCentralWidget(self.centralwidget)
        # self.label_picture.resize(50, 50)
        # self.horizontalLayout_4.addWidget(self.label_picture)

        self.table = QtWidgets.QTableView()
        font = QtGui.QFont()
        font.setPointSize(9)
        self.table.setFont(font)
        self.table.setModel(self.create_table_model())
        self.verticalLayout_2.addWidget(self.table)        
        self.pr = Process_signal()

    def tag_all(self):
        self.registerBookAction.triggered.connect(self.handle_registerBookAction)
        self.registerUserAction.triggered.connect(self.handle_registerUserAction)
        self.registerExemplarAction.triggered.connect(self.handle_registerExemplarAction)
        self.giveBookAction.triggered.connect(self.handle_giveBookAction)
        self.takeBookAction.triggered.connect(self.handle_takeBookAction)
        self.alfabeticalNameListAction.triggered.connect(self.handle_alfabeticalNameListAction)
        self.alfabeticalAuthorListAction.triggered.connect(self.handle_alfabeticalAuthorListAction)
        self.subjectListAction.triggered.connect(self.handle_subjectListAction)
        self.givenBookListAction.triggered.connect(self.handle_givenBookListAction)
        self.userListAction.triggered.connect(self.handle_userListAction)
        self.userInfoAction.triggered.connect(self.handle_userInfoAction)
        self.bookInfoAction.triggered.connect(self.handle_bookInfoAction)
        self.exemplarInfoAction.triggered.connect(self.handle_exemplarInfoAction)
        self.addTimeAction.triggered.connect(self.handle_addTimeAction)
        self.exemplarListAction.triggered.connect(self.handle_exemplarListAction)
        self.deleteExemplarAction.triggered.connect(self.handle_deleteExemplarAction)
        self.deleteUserAction.triggered.connect(self.handle_deleteUserAction)
        self.deleteBookAction.triggered.connect(self.handle_deleteBookAction)
        self.exportBooksAction.triggered.connect(self.handle_exportBooksAction)
        self.exportUsersAction.triggered.connect(self.handle_exportUsersAction)
        self.updateBookAction.triggered.connect(self.handle_updateBookAction)
        self.updateUserAction.triggered.connect(self.handle_updateUserAction)

        # init standart screen
        self.handle_alfabeticalNameListAction()
        head = ['ID', '????????. ??????????', '?????? ??????-??', '??????', '??????', 'ISBN', '??????????. ????????', '????????. ??????-????', '?????????? ??????-????', '??????????????',]
        info = self.pr.get_alf_name_list('','name','name','asc')
        m = self.create_table_model(info, head)
        self.table.setModel(m)

    def create_table_model(self, data=[], head=tuple()):
        return TableModel(data, head)

    def handle_registerBookAction(self):
        RegisterBook = QtWidgets.QDialog()
        ui = ui_reg_book.Ui_RegisterBook()
        ui.setupUi(RegisterBook)
        RegisterBook.show()
        if RegisterBook.exec_() == RegisterBook.Accepted:
            year = ui.lineEdit_year.text()
            pages = ui.lineEdit_pages.text()
            name = ui.lineEdit_name.text()
            subject = ui.lineEdit_subject.text()
            publisher_name = ui.lineEdit_publisherName.text()
            publisher_town = ui.lineEdit_publisherTown.text()
            authors = ui.lineEdit_authors.text()
            genres = ui.lineEdit_genres.text()
            UDK = ui.lineEdit_UDK.text()
            BBK = ui.lineEdit_BBK.text()
            ISBN = ui.lineEdit_ISBN.text()
            authorMark = ui.lineEdit_authorMark.text()

            genres = Validate_process.val_no_text(genres)
            if genres:
                genres  = list(map(Validate_process.val_strip_lower_text, genres.split(',')))

            authors = Validate_process.val_no_text(authors)
            if authors:
                authors = list(map(Validate_process.val_strip_cap_text, authors.split(',')))

            name = Validate_process.strip_text(name)
            subject = Validate_process.val_strip_lower_text(subject)
            publisher_name = Validate_process.val_strip_cap_text(publisher_name)
            publisher_town = Validate_process.strip_text(publisher_town)
            UDK = Validate_process.strip_text(UDK)
            BBK = Validate_process.strip_text(BBK)
            ISBN = Validate_process.strip_text(ISBN)
            authorMark = Validate_process.strip_text(authorMark)

            name = Validate_process.val_no_text(name)
            if name is None:
                self.illegal_input_info('???????????????? ??????????')
                return None
            year = Validate_process.val_integer(year)
            #print(year)
            if year == -1:
                self.illegal_input_info('??????')
                return None
            pages = Validate_process.val_integer(pages)
            if pages == -1:
                self.illegal_input_info('??????-???? ??????????????')
                return None

            reg_id = self.pr.register_book(name, year, publisher_name,
                                        publisher_town, pages, subject,
                                        genres, authors, UDK, BBK, ISBN, authorMark)
            self.reg_id_info('??????????', reg_id)

            self.handle_alfabeticalNameListAction()
            self.name_search()
        else:
            return None

    def handle_updateBookAction(self):
        bookID = self.integer_input('ID', '?????????????? ID ??????????: ')
        if bookID is None:
            return None

        info = self.pr.get_book_info(bookID)

        info_name = info['name']
        info_year = info['year']
        info_publisher_name = info['publisher'][0]
        info_publisher_town = info['publisher'][1]
        info_pages = info['pages']
        info_subject = info['subject']
        info_genres = info['genres']
        info_authors = info['authors']
        info_UDK = info['UDK']
        info_BBK = info['BBK']
        info_ISBN = info['ISBN']
        info_authorMark = info['authorMark']

        RegisterBook = QtWidgets.QDialog()
        ui = ui_upd_book.Ui_UpdateBook()
        ui.setupUi(RegisterBook,
                info_name, info_year, info_publisher_name, info_publisher_town, info_pages, info_subject,
                info_genres, info_authors, info_UDK, info_BBK, info_ISBN, info_authorMark)
        RegisterBook.show()

        if RegisterBook.exec_() == RegisterBook.Accepted:
            year = ui.lineEdit_year.text()
            pages = ui.lineEdit_pages.text()
            name = ui.lineEdit_name.text()
            subject = ui.lineEdit_subject.text()
            publisher_name = ui.lineEdit_publisherName.text()
            publisher_town = ui.lineEdit_publisherTown.text()
            authors = ui.lineEdit_authors.text()
            genres = ui.lineEdit_genres.text()
            UDK = ui.lineEdit_UDK.text()
            BBK = ui.lineEdit_BBK.text()
            ISBN = ui.lineEdit_ISBN.text()
            authorMark = ui.lineEdit_authorMark.text()

            genres = Validate_process.val_no_text(genres)
            if genres:
                genres  = list(map(Validate_process.val_strip_lower_text, genres.split(',')))

            authors = Validate_process.val_no_text(authors)
            if authors:
                authors = list(map(Validate_process.val_strip_cap_text, authors.split(',')))

            name = Validate_process.strip_text(name)
            subject = Validate_process.val_strip_lower_text(subject)
            publisher_name = Validate_process.val_strip_cap_text(publisher_name)
            publisher_town = Validate_process.strip_text(publisher_town)
            UDK = Validate_process.strip_text(UDK)
            BBK = Validate_process.strip_text(BBK)
            ISBN = Validate_process.strip_text(ISBN)
            authorMark = Validate_process.strip_text(authorMark)

            name = Validate_process.val_no_text(name)
            if name is None:
                self.illegal_input_info('???????????????? ??????????')
                return None
            year = Validate_process.val_integer(year)
            #print(year)
            if year == -1:
                self.illegal_input_info('??????')
                return None
            pages = Validate_process.val_integer(pages)
            if pages == -1:
                self.illegal_input_info('??????-???? ??????????????')
                return None

            reg_id = self.pr.update_book(bookID, name, year, publisher_name,
                                        publisher_town, pages, subject,
                                        genres, authors, UDK, BBK, ISBN, authorMark)
            self.upd_id_info('??????????', bookID)

            self.handle_alfabeticalNameListAction()
            self.name_search()
        else:
            return None

    def handle_registerUserAction(self):
        RegisterReader = QtWidgets.QDialog()
        ui = ui_reg_user.Ui_RegisterReader()
        ui.setupUi(RegisterReader)
        RegisterReader.show()
        if RegisterReader.exec_() == RegisterReader.Accepted:
            fName = ui.lineEdit_fName.text()
            sName = ui.lineEdit_sName.text()
            pName = ui.lineEdit_pName.text()

            fName = Validate_process.val_strip_cap_text(fName)
            sName = Validate_process.val_strip_cap_text(sName)
            pName = Validate_process.val_strip_cap_text(pName)

            fName = Validate_process.val_no_text(fName)
            if fName is None:
                self.illegal_input_info('??????')
                return None

            sName = Validate_process.val_no_text(sName)
            if sName is None:
                self.illegal_input_info('??????????????')
                return None


            reg_id = self.pr.register_user(fName, sName, pName)
            self.reg_id_info('????????????????????????', reg_id)

            self.handle_userListAction()
            self.user_search()
        else:
            return None

    def handle_updateUserAction(self):
        userID = self.integer_input('ID', '?????????????? ID ??????????????????????: ')
        if userID is None:
            return None

        info = self.pr.get_user_info(userID)

        info_fName = info['fName']
        info_sName = info['sName']
        info_pName = info['pName']

        UpdateReader = QtWidgets.QDialog()
        ui = ui_upd_user.Ui_UpdateReader()
        ui.setupUi(UpdateReader, info_fName, info_sName, info_pName)
        UpdateReader.show()
        if UpdateReader.exec_() == UpdateReader.Accepted:
            fName = ui.lineEdit_fName.text()
            sName = ui.lineEdit_sName.text()
            pName = ui.lineEdit_pName.text()

            fName = Validate_process.val_strip_cap_text(fName)
            sName = Validate_process.val_strip_cap_text(sName)
            pName = Validate_process.val_strip_cap_text(pName)

            fName = Validate_process.val_no_text(fName)
            if fName is None:
                self.illegal_input_info('??????')
                return None

            sName = Validate_process.val_no_text(sName)
            if sName is None:
                self.illegal_input_info('??????????????')
                return None


            self.pr.update_user(userID, fName, sName, pName)
            self.upd_id_info('????????????????????????', userID)

            self.handle_userListAction()
            self.user_search()
        else:
            return None

    def handle_registerExemplarAction(self):
        # self.reconnect(self.searchButton.clicked, self.null_search)
        #print('handle_registerExemplarAction triggered')
        RegisterExemplar = QtWidgets.QDialog()
        ui = ui_reg_exemplar.Ui_RegisterExemplar()
        ui.setupUi(RegisterExemplar)
        RegisterExemplar.show()
        if RegisterExemplar.exec_() == RegisterExemplar.Accepted:
            bookID =     ui.lineEdit_bookID.text()
            exemplarID = ui.lineEdit_exemplarId.text()
            #print(bookID, exemplarID)

            bookID = Validate_process.val_integer_no_text(bookID)
            if bookID == -1:
                self.illegal_input_info('ID ??????????')
                return None

            exemplarID = Validate_process.val_integer_no_text(exemplarID)
            if exemplarID == -1:
                self.illegal_input_info('ID ????????????????????')
                return None

            reg_id = self.pr.register_exemplar(bookID, exemplarID)
            if exemplarID is None:
                self.reg_id_info('??????????????????', reg_id)
            else:
                self.reg_id_info('??????????????????', exemplarID)
        else:
            return None

    def handle_giveBookAction(self):
        # self.reconnect(self.searchButton.clicked, self.null_search)
        #print('handle_giveBookAction triggered')
        GiveBook = QtWidgets.QDialog()
        ui = ui_give_book.Ui_GiveBook()
        ui.setupUi(GiveBook)
        GiveBook.show()
        if GiveBook.exec_() == GiveBook.Accepted:
            userID =     ui.lineEdit_userID.text()
            exemplarID = ui.lineEdit_exemplarID.text()
            givenTime = ui.lineEdit_givenTime.text()

            userID = Validate_process.val_integer_no_text(userID)
            if userID == -1:
                self.illegal_input_info('ID ????????????????????????')
                return None

            exemplarID = Validate_process.val_integer_no_text(exemplarID)
            if exemplarID == -1:
                self.illegal_input_info('ID ????????????????????')
                return None

            givenTime = Validate_process.val_integer_no_text(givenTime)
            if givenTime == -1:
                self.illegal_input_info('?????????? ????????????')
                return None

            self.pr.give_book(userID, exemplarID, givenTime)
            self.book_given_info(userID, exemplarID, givenTime)
        else:
            return None
        pass

    def handle_takeBookAction(self):
        # self.reconnect(self.searchButton.clicked, self.null_search)
        #print('handle_takeBookAction triggered')
        TakeBook = QtWidgets.QDialog()
        ui = ui_take_book.Ui_TakeBook()
        ui.setupUi(TakeBook)
        TakeBook.show()
        if TakeBook.exec_() == TakeBook.Accepted:
            # userID =     ui.lineEdit_userID.text()
            exemplarID = ui.lineEdit_exemplarID.text()
            exemplarID = Validate_process.val_integer_no_text(exemplarID)
            if exemplarID == -1:
                self.illegal_input_info('ID ????????????????????')
                return None
            self.pr.take_book(exemplarID)
            self.book_taken_info(exemplarID)
        else:
            return None
        pass

    def handle_addTimeAction(self):
        # self.reconnect(self.searchButton.clicked, self.null_search)
        #print('handle_addTimeAction triggered')
        AddTime = QtWidgets.QDialog()
        ui = ui_add_time.Ui_AddTime()
        ui.setupUi(AddTime)
        AddTime.show()
        if AddTime.exec_() == AddTime.Accepted:
            exemplarID = ui.lineEdit_exemplarId.text()
            addTime = ui.lineEdit_addTime.text()
            exemplarID = Validate_process.val_integer_no_text(exemplarID)
            addTime = Validate_process.val_integer_no_text(addTime)
            if exemplarID == -1:
                self.illegal_input_info('ID ????????????????????')
                return None
            if addTime == -1:
                self.illegal_input_info('??????????')
                return None
            self.pr.add_time(exemplarID, addTime)
            self.book_add_time_info(exemplarID, addTime)
        else:
            return None
        pass

    def handle_givenBookListAction(self):
        # self.reconnect(self.searchButton.clicked, self.null_search)
        _translate = QtCore.QCoreApplication.translate
        #print('handle_givenBookListAction triggered')
        ## print(info)
        self.reconnect(self.searchButton.clicked, self.exemplar_search)
        self.reconnect(self.comboBoxOrderBy.currentIndexChanged, self.exemplar_search)
        self.reconnect(self.comboBoxOrderByAsc.currentIndexChanged, self.exemplar_search)
        self.comboBoxSearchIn.clear()
        self.comboBoxOrderBy.clear()
        self.comboBoxOrderByAsc.clear()
        self.magazineType.setText(_translate("MainWindow", "???????????????? ???????????????????? ????????"))

        sort_list = [
            _translate("MainWindow", 'ID ????????????????????'),
            _translate("MainWindow", 'ID ??????????'),
            _translate("MainWindow", 'ID ??????????-????'),
            _translate("MainWindow", '???????? ????????????'),
            _translate("MainWindow", '???????? ????????????'),
            _translate("MainWindow", '???????????????? ??????????????'),
        ]
        asc_list = [
            _translate("MainWindow", '????????.'),
            _translate("MainWindow", '????????.'),
        ]
        self.comboBoxOrderByAsc.addItems(asc_list)
        self.comboBoxOrderBy.addItems(sort_list)
        pass

    def handle_exemplarListAction(self):
        _translate = QtCore.QCoreApplication.translate
        self.magazineType.setText(_translate("MainWindow", "???????????????????? ????????"))
        self.reconnect(self.searchButton.clicked, self.null_search)
        self.reconnect(self.comboBoxSearchIn.currentIndexChanged, self.null_search)
        self.reconnect(self.comboBoxOrderBy.currentIndexChanged, self.null_search)
        self.reconnect(self.comboBoxOrderByAsc.currentIndexChanged, self.null_search)
        self.comboBoxSearchIn.clear()
        self.comboBoxOrderBy.clear()
        self.comboBoxOrderByAsc.clear()
        self.all_exemplar_search()


    def handle_alfabeticalNameListAction(self):
        _translate = QtCore.QCoreApplication.translate
        #print('handle_alfabeticalNameListAction triggered')
        self.reconnect(self.searchButton.clicked, self.name_search)
        self.reconnect(self.comboBoxSearchIn.currentIndexChanged, self.name_search)
        self.reconnect(self.comboBoxOrderBy.currentIndexChanged, self.name_search)
        self.reconnect(self.comboBoxOrderByAsc.currentIndexChanged, self.name_search)
        self.magazineType.setText(_translate("MainWindow", "??????. ?????????????? ??????????"))
        self.comboBoxSearchIn.clear()
        self.comboBoxOrderBy.clear()
        self.comboBoxOrderByAsc.clear()

        search_in_list = [
            _translate("MainWindow", '???????????????? ??????????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", 'ISBN'),
            _translate("MainWindow", '??????. ????????'),
            _translate("MainWindow", '????????????????????????'),
        ]


        sort_list = [
            _translate("MainWindow", 'ID ??????????'),
            _translate("MainWindow", '???????????????? ??????????'),
            _translate("MainWindow", '?????? ??????????????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", 'ISBN'),
            _translate("MainWindow", '??????????. ????????'),
            _translate("MainWindow", '????????. ????????????????????????????'),
            _translate("MainWindow", '?????????? ????????????????????????????'),
            _translate("MainWindow", '??????????????'),
        ]

        asc_list = [
            _translate("MainWindow", '????????.'),
            _translate("MainWindow", '????????.'),
        ]
        self.comboBoxOrderByAsc.addItems(asc_list)
        self.comboBoxSearchIn.addItems(search_in_list)
        self.comboBoxOrderBy.addItems(sort_list)
        pass

    def handle_alfabeticalAuthorListAction(self):
        _translate = QtCore.QCoreApplication.translate
        #print('handle_alfabeticalAuthorListAction triggered')
        self.reconnect(self.searchButton.clicked, self.author_search)
        self.reconnect(self.comboBoxSearchIn.currentIndexChanged, self.author_search)
        self.reconnect(self.comboBoxOrderBy.currentIndexChanged, self.author_search)
        self.reconnect(self.comboBoxOrderByAsc.currentIndexChanged, self.author_search)
        self.magazineType.setText(_translate("MainWindow", "??????. ?????????????? ????????????"))
        self.comboBoxSearchIn.clear()
        self.comboBoxOrderBy.clear()
        self.comboBoxOrderByAsc.clear()

        search_in_list = [
            _translate("MainWindow", '?????? ????????????'),

        ]

        sort_list = [
            _translate("MainWindow", 'ID ??????????'),
            _translate("MainWindow", '?????? ????????????'),
            _translate("MainWindow", '???????????????? ??????????'),
            _translate("MainWindow", '?????? ??????????????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", 'ISBN'),
            _translate("MainWindow", '????????. ????????????????????????????'),
            _translate("MainWindow", '?????????? ????????????????????????????'),
            _translate("MainWindow", '??????????????'),

        ]

        asc_list = [
            _translate("MainWindow", '????????.'),
            _translate("MainWindow", '????????.'),
        ]
        self.comboBoxOrderByAsc.addItems(asc_list)
        self.comboBoxSearchIn.addItems(search_in_list)
        self.comboBoxOrderBy.addItems(sort_list)
        pass

    def handle_subjectListAction(self):
        _translate = QtCore.QCoreApplication.translate
        self.reconnect(self.searchButton.clicked, self.genre_search)
        self.reconnect(self.comboBoxSearchIn.currentIndexChanged, self.genre_search)
        self.reconnect(self.comboBoxOrderBy.currentIndexChanged, self.genre_search)
        self.reconnect(self.comboBoxOrderByAsc.currentIndexChanged, self.genre_search)
        self.magazineType.setText(_translate("MainWindow", "????????. ?????????????? ??????????"))
        self.comboBoxSearchIn.clear()
        self.comboBoxOrderBy.clear()
        self.comboBoxOrderByAsc.clear()

        search_in_list = [
            _translate("MainWindow", '??????????????'),
            _translate("MainWindow", '????????'),

        ]

        sort_list = [
            _translate("MainWindow", 'ID ??????????'),
            _translate("MainWindow", '????????'),
            _translate("MainWindow", '?????? ??????????????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", 'ISBN'),
            _translate("MainWindow", '????????. ????????????????????????????'),
            _translate("MainWindow", '?????????? ????????????????????????????'),
            _translate("MainWindow", '??????????????'),

        ]
        asc_list = [
            _translate("MainWindow", '????????.'),
            _translate("MainWindow", '????????.'),
        ]
        self.comboBoxOrderByAsc.addItems(asc_list)
        self.comboBoxSearchIn.addItems(search_in_list)
        self.comboBoxOrderBy.addItems(sort_list)
        pass

    def handle_userListAction(self):
        _translate = QtCore.QCoreApplication.translate
        #print('handle_userListAction triggered')
        self.reconnect(self.searchButton.clicked, self.user_search)
        self.reconnect(self.comboBoxSearchIn.currentIndexChanged, self.user_search)
        self.reconnect(self.comboBoxOrderBy.currentIndexChanged, self.user_search)
        self.reconnect(self.comboBoxOrderByAsc.currentIndexChanged, self.user_search)
        self.magazineType.setText(_translate("MainWindow", "????????????????????????"))
        self.comboBoxSearchIn.clear()
        self.comboBoxOrderBy.clear()
        self.comboBoxOrderByAsc.clear()

        search_in_list = [
            _translate("MainWindow", '??????'),
        ]

        sort_list = [
            _translate("MainWindow", 'ID ??????????-????'),
            _translate("MainWindow", '??????'),
            _translate("MainWindow", '??????????????'),
            _translate("MainWindow", '????????????????'),
        ]
        asc_list = [
            _translate("MainWindow", '????????.'),
            _translate("MainWindow", '????????.'),
        ]
        self.comboBoxOrderByAsc.addItems(asc_list)
        self.comboBoxSearchIn.addItems(search_in_list)
        self.comboBoxOrderBy.addItems(sort_list)
        pass

    def handle_userInfoAction(self):
        # self.reconnect(self.searchButton.clicked, self.null_search)
        #print('handle_userInfoAction triggered')
        userID = self.integer_input('ID', '?????????????? ID ??????????????????????: ')
        if userID is None:
            return None
        info = self.pr.get_user_info(userID)
        if info is None:
            self.illegal_input_info('ID ????????????????????????')
            return None
        #print(info)
        UserInfo = QtWidgets.QDialog()
        ui = Ui_UserInfo_tagged(info)
        ui.setupUi(UserInfo)
        UserInfo.show()
        UserInfo.exec_()
        return None

    def handle_deleteExemplarAction(self):
        exemplarID = self.integer_input('ID', '?????????????? ID ????????????????????: ')
        if exemplarID is None:
            return None
        self.pr.delete_exemplar(exemplarID)
        self.del_id_info('??????????????????', bookID)
        return None

    def handle_deleteUserAction(self):
        userID = self.integer_input('ID', '?????????????? ID ????????????????????????: ')
        if userID is None:
            return None
        self.pr.delete_user(userID)
        self.del_id_info('????????????????????????', userID)
        return None

    def handle_deleteBookAction(self):
        bookID = self.integer_input('ID', '?????????????? ID ??????????: ')
        if bookID is None:
            return None
        self.pr.delete_book(bookID)
        self.del_id_info('??????????', bookID)
        return None

    def handle_bookInfoAction(self):
        # self.reconnect(self.searchButton.clicked, self.null_search)
        #print('handle_bookInfoAction triggered')
        bookID = self.integer_input('ID', '?????????????? ID ??????????: ')
        if bookID is None:
            return None
        info = self.pr.get_book_info(bookID)
        if info is None:
            self.illegal_input_info('ID ??????????')
            return None
        ## print(info)
        BookInfo = QtWidgets.QDialog()
        ui = Ui_BookInfo_tagged(info)
        ui.setupUi(BookInfo)
        BookInfo.show()
        BookInfo.exec_()
        # if BookInfo.exec_() == BookInfo.Accepted:
        #     return None
        return None

    def handle_exemplarInfoAction(self):
        # self.reconnect(self.searchButton.clicked, self.null_search)
        #print('handle_exemplarInfoAction triggered')
        exemplarID = self.integer_input('ID', '?????????????? ID ????????????????????: ')
        if exemplarID is None:
            return None
        info = self.pr.get_exemplar_info(exemplarID)
        if info is None:
            self.illegal_input_info('ID ????????????????????')
            return None
        ExemplarInfo = QtWidgets.QDialog()
        ui = Ui_ExemplarInfo_tagged(info)
        ui.setupUi(ExemplarInfo)
        ExemplarInfo.show()
        ExemplarInfo.exec_()
        return None

    def handle_exportBooksAction(self):
        file_path = self.saveFileDialog('???????????????????????????? ???????????? ????????')
        if file_path != '':
            self.pr.export_books(file_path)

    def handle_exportUsersAction(self):
        file_path = self.saveFileDialog('???????????????????????????? ???????????? ??????????????????????????')
        if file_path != '':
            self.pr.export_users(file_path)

    def null_search(self):
        pass

    def all_exemplar_search(self):
        head = ('ID ????????????????????', 'ID ??????????')
        info = self.pr.get_all_exempalr_list()
        m = self.create_table_model(info, head)
        self.table.setModel(m)

    def exemplar_search(self):
        sort_search = self.comboBoxOrderBy.currentIndex()
        asc_search = self.comboBoxOrderByAsc.currentIndex()

        head = ('ID ????????????????????', 'ID ??????????', 'ID ??????????-????',
                '???????? ????????????', '???????? ????????????', '????????????????')

        sort_list_t = [
            'id', 'book_id', 'user_id',
            'give_date', 'give_time', 'left'
        ]

        asc_list_t = [
            'asc', 'desc'
        ]

        info = self.pr.get_exemplar_list(sort_list_t[sort_search],
                                            asc_list_t[asc_search])
        m = self.create_table_model(info, head)
        self.table.setModel(m)
        pass

    def name_search(self):
        search_query = Validate_process.strip_text(self.lineEdit_search.text())
        search_in = self.comboBoxSearchIn.currentIndex()
        sort_search = self.comboBoxOrderBy.currentIndex()
        asc_search = self.comboBoxOrderByAsc.currentIndex()

        sort_list_t = [
                        'id', 'name', 'year', 'UDK',
                        'BBK', 'ISBN',
                        'author_mark', 'publisher_name',
                        'publisher_town', 'subject_name'
        ]

        head = [
            'ID',
            '????????. ??????????',
            '?????? ??????-??',
            '??????',
            '??????',
            'ISBN',
            '??????????. ????????',
            '????????. ??????-????',
            '?????????? ??????-????',
            '??????????????',
        ]

        search_in_list_t = [
            'name', 'year', 'UDK',
            'BBK', 'ISBN', 'author_mark',
            'publisher_name'
        ]

        asc_list_t = [
            'asc', 'desc'
        ]
        ## print(search_query, search_in_list_t[search_in], sort_list_t[sort_search], asc_list_t[asc_search])
        info = self.pr.get_alf_name_list(search_query,
                                            search_in_list_t[search_in],
                                            sort_list_t[sort_search],
                                            asc_list_t[asc_search]
                                            )
        # for i in info:
        ##     print(i)
        m = self.create_table_model(info, head)
        self.table.setModel(m)
        pass

    def author_search(self):
        search_query = Validate_process.strip_text(self.lineEdit_search.text())
        search_in = self.comboBoxSearchIn.currentIndex()
        sort_search = self.comboBoxOrderBy.currentIndex()
        asc_search = self.comboBoxOrderByAsc.currentIndex()
        ## print(search_query, search_in, sort_search, asc_search)

        search_in_list_t = [
            'author_name'
        ]

        sort_list_t = [
            'id', 'author', 'name', 'year',
            'UDK', 'BBK', 'ISBN', 'publisher_name',
            'publisher_town', 'subject_name'
        ]

        asc_list_t = [
            'asc', 'desc'
        ]
        
        head = [
            '?????? ????????????',
            'ID ??????????',
            '????????. ??????????',
            '?????? ??????-??',
            '??????',
            '??????',
            'ISBN',
            '????????. ??????-????',
            '?????????? ??????-????',
            '??????????????',
        ]
        #print(search_query, search_in_list_t[search_in], sort_list_t[sort_search], asc_list_t[asc_search])
        
        info = self.pr.get_alf_author_list(search_query,
                                            search_in_list_t[search_in],
                                            sort_list_t[sort_search],
                                            asc_list_t[asc_search]
                                            )
        # for i in info:
        ##     print(i)
        m = self.create_table_model(info, head)
        self.table.setModel(m)
        pass

    def genre_search(self):
        search_query = Validate_process.strip_text(self.lineEdit_search.text())
        search_in = self.comboBoxSearchIn.currentIndex()
        sort_search = self.comboBoxOrderBy.currentIndex()
        asc_search = self.comboBoxOrderByAsc.currentIndex()
        #print(search_query, search_in, sort_search, asc_search)

        search_in_list_t = [
            'subject_name', 'genre'
        ]

        sort_list_t = [
            'id', 'genre', 'name', 'year',
            'UDK', 'BBK', 'ISBN',
            'publisher_name', 'publisher_town',
            'subject_name'
        ]

        asc_list_t = [
            'asc', 'desc'
        ]
        
        head = [
            '????????',
            '??????????????',
            'ID ??????????',
            '????????. ??????????',
            '?????? ??????-??',
            '??????',
            '??????',
            'ISBN',
            '????????. ??????-????',
            '?????????? ??????-????',
        ]

        #print(search_query, search_in_list_t[search_in], sort_list_t[sort_search], asc_list_t[asc_search])
        info = self.pr.get_syst_list(search_query,
                                            search_in_list_t[search_in],
                                            sort_list_t[sort_search],
                                            asc_list_t[asc_search]
                                            )
        m = self.create_table_model(info, head)
        self.table.setModel(m)
        pass

    def user_search(self):
        search_query = Validate_process.strip_text(self.lineEdit_search.text())
        search_in = self.comboBoxSearchIn.currentIndex()
        sort_search = self.comboBoxOrderBy.currentIndex()
        asc_search = self.comboBoxOrderByAsc.currentIndex()
        #print(search_query, search_in, sort_search, asc_search)

        search_in_list_t = [
            'text'
        ]

        sort_list_t = [
            'id', 'f', 's', 'p'
        ]

        asc_list_t = [
            'asc', 'desc'
        ]

        head = [
            'ID ??????????-????',
            '??????????????',
            '??????',
            '????????????????',
            '???????? ??????-??'
        ]

        info = self.pr.get_user_list(search_query,
                                            search_in_list_t[search_in],
                                            sort_list_t[sort_search],
                                            asc_list_t[asc_search]
                                            )
        m = self.create_table_model(info, head)
        self.table.setModel(m)
        pass


    def text_input(self, windowTitle, infoText):
        window = QtWidgets.QWidget()
        text, ok = QtWidgets.QInputDialog.getText(window, windowTitle, infoText)
        if ok:
            return text
        return None

    def info_text(self, windowTitle, infoText):
        window = QtWidgets.QWidget()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(infoText)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def illegal_input_info(self, text):
        window = QtWidgets.QWidget()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(f'???????????????? ????????: "{text}"')
        msgBox.setWindowTitle('???????????????? ????????')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def book_given_info(self, userId, exemplarId, t):
        window = QtWidgets.QWidget()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(f'?????????????????? ID_{exemplarId} ?????????? ???????????????????????? ID_{userId} ???? {t} ????????.')
        msgBox.setWindowTitle('???????????? ??????????')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def book_add_time_info(self, exemplarId, t):
        window = QtWidgets.QWidget()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(f'?????????? ???????????? ???????????????????? ID_{exemplarId} ???????????????? ???? {t} ????????.')
        msgBox.setWindowTitle('????????????????')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def book_taken_info(self, exemplarId):
        window = QtWidgets.QWidget()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(f'?????????? {exemplarId} ????????????????????.')
        msgBox.setWindowTitle('?????????????????? ??????????')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def reg_id_info(self, name, i):
        window = QtWidgets.QWidget()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(name.capitalize() + ' ??????????. ???? ID: ' + str(i))
        msgBox.setWindowTitle('??????????.')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def upd_id_info(self, name, i):
        window = QtWidgets.QWidget()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(name.capitalize() + ' c ID: ' + str(i) + ' ??????????.')
        msgBox.setWindowTitle('???????????????????? ??????????????')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def del_id_info(self, name, i):
        window = QtWidgets.QWidget()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(name.capitalize() + ' ?? ID: ' + str(i) + ' ????????.')
        msgBox.setWindowTitle('???????????????? ??????????????')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def integer_input(self, windowTitle, infoText):
        window = QtWidgets.QWidget()
        text, ok = QtWidgets.QInputDialog.getText(window, windowTitle, infoText)
        if ok:
            try:
                text = int(text)
                return text
            except ValueError:
                self.info_text('???????????????? ????????', f'???????????????? ????????: "{text}"')
        return None

    def saveFileDialog(self, windowTitle):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, extention_type = QtWidgets.QFileDialog.getSaveFileName(self, windowTitle, "","*;;*.xlsx", options=options)
        
        if os.path.splitext(file_path)[1] == '':
            file_path = ''.join((file_path, extention_type[1:]))

        return file_path

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setText("???? ??????????????, ?????? ???????????? ???????????")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def reconnect(self, signal, newhandler=None, oldhandler=None):        
        try:
            if oldhandler is not None:
                while True:
                    signal.disconnect(oldhandler)
            else:
                signal.disconnect()
        except TypeError:
            pass
        if newhandler is not None:
            signal.connect(newhandler)


class Ui_BookInfo_tagged(ui_book_info.Ui_BookInfo):
    def __init__(self, info):
        self.info = info

    def setupUi(self, BookInfo):
        super().setupUi(BookInfo)
        self.table = QtWidgets.QTableView()
        m = self.create_table_model(self.info['givenExemplars'], ('ID ????????????????????', 'ID ????????????????????????', '???????? ????????????', '???????? ????????????', '????????????????'))
        self.table.setModel(m)
        self.gridLayout.addWidget(self.table, 9, 0, 1, 2)

    def create_table_model(self, data, head):
        return TableModel(data, head)

    def retranslateUi(self, BookInfo):
        super().retranslateUi(BookInfo)
        _translate = QtCore.QCoreApplication.translate
        publ = self.info['publisher']
        gens = self.info['genres']
        auth = self.info['authors']
        self.bookPages.setText(_translate("BookInfo", str(self.info['pages'])))
        self.bookGenre.setText(_translate("BookInfo", ' ,'.join(gens)))
        self.bookSubject.setText(_translate("BookInfo", self.info['subject']))
        self.bookPublisher.setText(_translate("BookInfo", publ[0] + ' ??. ' + publ[1]))
        self.bookISBN.setText(_translate("BookInfo", self.info['ISBN']))
        self.bookBBK.setText(_translate("BookInfo", self.info['BBK']))
        self.bookYear.setText(_translate("BookInfo", str(self.info['year'])))
        self.bookName.setText(_translate("BookInfo", self.info['name']))
        self.bookUDK.setText(_translate("BookInfo", self.info['UDK']))
        self.bookID.setText(_translate("BookInfo", str(self.info['id'])))
        self.bookAuthor.setText(_translate("BookInfo", ' ,'.join(auth)))
        self.exemplarList.setText(_translate("BookInfo", " , ".join(self.info['exemplars']) +
                f"\n ?????????? : {len(self.info['exemplars'])}; ???????????? : {len(self.info['givenExemplars'])}; ???? ???????????? : {len(self.info['exemplars']) - len(self.info['givenExemplars'])}"))


class Ui_UserInfo_tagged(ui_user_info.Ui_UserInfo):
    def __init__(self, info):
        self.info = info

    def setupUi(self, UserInfo):
        super().setupUi(UserInfo)
        self.table = QtWidgets.QTableView()
        self.info['readingTimeOut'] = list(map(list, self.info['readingTimeOut']))
        for i in self.info['readingTimeOut']:
            i[1] += '!!! ?????????? ??????????'
        self.info['readingTimeOut'] = list(map(tuple, self.info['readingTimeOut']))
        m = self.create_table_model(self.info['readingTimeOut'] +
                                    self.info['readingNormal'],
                                    ('ID ????????????????????', '???????? ????????????', '???????? ????????????'))
        self.table.setModel(m)
        self.gridLayout.addWidget(self.table, 7, 0, 1, 3)

    def create_table_model(self, data, head):
        return TableModel(data, head)

    def retranslateUi(self, UserInfo):
        super().retranslateUi(UserInfo)
        _translate = QtCore.QCoreApplication.translate
        self.userID.setText(_translate("UserInfo", str(self.info['id'])))
        self.sName.setText(_translate("UserInfo", self.info['sName']))
        self.fName.setText(_translate("UserInfo", self.info['fName']))
        self.pName.setText(_translate("UserInfo", self.info['pName']))
        self.regData.setText(_translate("UserInfo", self.info['regDate']))


class Ui_ExemplarInfo_tagged(ui_exemplar_info.Ui_ExemplarInfo):
    def __init__(self, info):
        self.info = info

    def retranslateUi(self, ExemplarInfo):
        super().retranslateUi(ExemplarInfo)
        _translate = QtCore.QCoreApplication.translate
        self.exemplarID.setText(_translate("ExemplarInfo", str(self.info['id'])))
        self.bookID.setText(_translate("ExemplarInfo", str(self.info['bookId'])))
        self.bookName.setText(_translate("ExemplarInfo", str(self.info['bookName'])))


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=[], head=tuple()):
        super(TableModel, self).__init__()
        self._data = data
        self._head = head

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._head)

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return None
        if orientation == QtCore.Qt.Horizontal:
            return self._head[section]
        else:
            return "{}".format(section)

def main(ctx):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = tag_Ui_MainWindow()
    process = Process_signal
    ui.setupUi(MainWindow, process, ctx)
    ui.tag_all()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    pass
