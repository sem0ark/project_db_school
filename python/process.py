import DataBase_2 as data

class Process_signal(object):
    def __init__(self,):
        self.db = data.DataBase()

    def register_user(self, fName, sName, pName):
        self.db.register_reader(fName, sName, pName)
        # return self.db.find_last_reader(fName, sName, pName)
        return self.db.get_last_id()

    def register_book(
                    self, name, year, publisher_name,
                    publisher_town, pages, subject,
                    genres, authors, UDK, BBK, ISBN, authorMark):
        self.db.add_book(name, year, publisher_name,
                    publisher_town, pages, subject,
                    genres, authors, UDK, BBK, ISBN, authorMark)
        # return self.db.c.find_book(name, year, pages, UDK, BBK, ISBN, authorMark)
        return self.db.get_last_id()

    def update_book(
                    self, bookId, name, year, publisher_name,
                    publisher_town, pages, subject,
                    genres, authors, UDK, BBK, ISBN, authorMark):
        self.db.update_book_full(name, year, publisher_name,
                                publisher_town, pages, subject,
                                genres, authors, UDK, BBK, ISBN, authorMark)
        return bookId

    def update_user(self, readerId, fName, sName, pName):
        self.db.update_reader(readerId, fName, sName, pName)

    def delete_book(self, bookId):
        self.db.delete_book_deep(bookId)

    def delete_exemplar(self, exemplarId):
        self.db.delete_exemplar_deep(exemplarId)

    def delete_user(self, readerId):
        self.db.delete_reader_deep(readerId)

    def register_exemplar(self, bookId, exemplarId):
        self.db.register_exemplar(bookId, exemplarId)
        # return self.db.find_last_exemplar(bookId)
        return self.db.get_last_id()

    def give_book(self, userId, exemplarID, givenTime):
        self.db.give_book(userId, exemplarID, givenTime)

    def take_book(self, exemplarID):
        self.db.take_book(exemplarID)

    def add_time(self, exemplarID, addTime):
        self.db.add_time_to_takeout(exemplarID, addTime)

    def get_book_info(self, bookId):
        return self.db.get_book_info(bookId)

    def get_exemplar_info(self, exemplarID):
        return self.db.get_exemplar_info(exemplarID)

    def get_user_info(self, userId):
        return self.db.get_reader_info(userId)

    def get_alf_name_list(self, text, tagSearch, tagSort, tagAsc): # process search query
        return self.db.get_book_alf_name(text, tagSearch, tagSort, tagAsc)

    def get_alf_author_list(self, text, tagSearch, tagSort, tagAsc): # process search query
        return self.db.get_book_alf_author(text, tagSearch, tagSort, tagAsc)

    def get_syst_list(self, text, tagSearch, tagSort, tagAsc): # process search query
        return self.db.get_book_syst_genre(text, tagSearch, tagSort, tagAsc)

    def get_user_list(self, text, tagSearch, tagSort, tagAsc): # process search query
        return self.db.get_reader_by_name(text, tagSearch, tagSort, tagAsc)

    def get_exemplar_list(self, tagSort, tagAsc): # get list of taken away (or not) books
        return self.db.get_exemplar_list(tagSort, tagAsc)

    def get_all_exempalr_list(self):
        return self.db.get_all_exemplars()

    def export_books(self, file_path):
        self.db.export_books(file_path)

    def export_users(self, file_path):
        self.db.export_readers(file_path)
    

    def close(self):
        self.db.close()



if __name__ == '__main__':
    test = Process_signal()
    # reg_id = test.register_user('Семен', 'Коробков', 'Сергеевичов')
    # print(reg_id)

    # name, year,
    #                 publisherId, pages, subjectId,
    #                 UDK, BBK, ISBN, authorMark
    # reg_id = test.register_book(
    #         'name', 3471, 'Piter', 'pppp', 420, 'subject',
    #         ['genre1','genre2','genre3'],
    #         ['Max L.','Пушкин А. С.'],
    #         '373.167.1: [512+517]',
    #         '22ю14я72',
    #         '5-09-015660-3',
    #         'А45'
    #     )
    # reg_id = test.register_exemplar(1)
    # test.give_book(5, 2, 10)
    # test.add_time(2, 20)
    # test.take_book(2)


    # print(reg_id)
    test.close()
