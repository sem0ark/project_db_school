import sqlite3 as sq


class DataBase:
    """
    Main class of database operations
    Based on sqlite3
    """

    def __init__(self):
        """
        initialise database
        """
        self.db = sq.connect("data_2.db")
        self.c = self.db.cursor()

        # create book
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY,
                year INTEGER,
                name TEXT,
                publisherId INTEGER,
                pages INTEGER,
                subjectId INTEGER,
                UDK TEXT,
                BBK TEXT,
                ISBN TEXT,
                authorMark TEXT
            )
        
        """)

        # create author

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS author (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)

        # create publisher

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS publisher (
                id INTEGER PRIMARY KEY,
                name TEXT,
                town TEXT
            )
        """)

        # create genre

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS genre (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)

        # create subject

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS subject (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)

        # create book_exemplar

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS book_exemplar (
                id INTEGER PRIMARY KEY,
                exemplarId INTEGER,
                bookId INTEGER
            )
        """)

        # create relation author -> book

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS author_book (
                id INTEGER PRIMARY KEY,
                authorId INTEGER,
                bookId INTEGER
            )
        """)

        # create relation genre -> book

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS genre_book (
                id INTEGER PRIMARY KEY,
                genreId INTEGER,
                bookId INTEGER
            )
        """)

        # create reader

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS reader (
                id INTEGER PRIMARY KEY,
                fName TEXT,
                sName TEXT,
                pName TEXT,
                registrationDate TEXT
            )
        """)

        # create takeout

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS takeout (
                id INTEGER PRIMARY KEY,
                readerId INTEGER,
                bookExemplarId INTEGER,
                beginDate REAL,
                endDate REAL,
                givenTime INTEGER
            )
        """) # givenTime -> number of days

        self.db.commit()

    def register_genre(self, name):
        self.c.execute("""
            INSERT INTO genre (name)
            VALUES (:genre)
        """, {'genre': name})

        self.db.commit()

    def register_subject(self, name):
        self.c.execute("""
            INSERT INTO subject (name)
            VALUES (:subject)
        """, {'subject': name})

        self.db.commit()

    def register_publisher(self, name, town):
        self.c.execute("""
            INSERT INTO publisher (name, town)
            VALUES (:name, :town)
        """, {
            'name': name,
            'town': town
        })

        self.db.commit()

    def register_book(self, name, year, publisherId, pages, subjectId, UDK, BBK, ISBN, authorMark):
        self.c.execute("""
            INSERT INTO book (name, year, publisherId, pages, subjectId, UDK, BBK, ISBN, authorMark)
            VALUES (:name, :year, :publisherId, :pages, :subjectId, :UDK, :BBK, :ISBN, :authorMark)
        """, {
            'name': name,
            'year': year,
            'publisherId': publisherId,
            'pages': pages,
            'subjectId': subjectId,
            'UDK': UDK,
            'BBK': BBK,
            'ISBN': ISBN,
            'authorMark': authorMark
        })

        self.db.commit()

    def delete_book(self, bookId):
        """
        Remove all books with current ID.
        Don't remove that one's exeplars or aithors etc.
        """

        self.c.execute("""
            DELETE FROM book
            WHERE id = :book_id;
        """,
        {
            'book_id': bookId,
        })

        self.db.commit()

    def delete_book_author(self, bookId):
        """
        Removes all book-author rows with that book ID.
        """

        self.c.execute("""
            DELETE FROM author_book
            WHERE bookId = :book_id
        """,
        {
            'book_id': bookId,
        })

        self.db.commit()

    def delete_book_genre(self, bookId):
        """
        Removes all book-author rows with that book ID.
        """

        self.c.execute("""
            DELETE FROM genre_book
            WHERE bookId = :book_id
        """,
        {
            'book_id': bookId,
        })

        self.db.commit()

    def register_reader(self, fName, sName, pName):
        self.c.execute("""
            INSERT INTO reader (fName, sName, pName, registrationDate)
            VALUES (:fName, :sName, :pName, strftime('%d-%m-%Y', 'now'))
        """, {
            'fName': fName,
            'sName': sName,
            'pName': pName
        })

        self.db.commit()

    def delete_reader(self, readerId):
        self.c.execute("""
            DELETE FROM reader
            WHERE id=:reader_id
        """, {
            'reader_id': readerId,
        })

        self.db.commit()

    def delete_reader_history(self, readerId):
        self.c.execute("""
            DELETE FROM takeout
            WHERE readerId=:reader_id
        """, {
            'reader_id': readerId,
        })

        self.db.commit()

    def register_author(self, name):
        self.c.execute("""
            INSERT INTO author (name)
            VALUES (:name)
        """, {
            'name': name
        })

        self.db.commit()

    def register_exemplar(self, bookId, exemplarId):
        self.c.execute("""
            INSERT INTO book_exemplar (bookId, exemplarId)
            VALUES (:bookId, 
                CASE
                    WHEN :exemplarId IS NULL
                        THEN :last_id+1
                    ELSE :exemplarId
                END
            )
        """, {
            'bookId': bookId,
            'exemplarId': exemplarId,
            'last_id': self.find_last_exemplar_ins()
        })

        self.db.commit()

    def delete_exemplar(self, exemplarId):
        """
        Removes all exemplars with that ID.
        """

        self.c.execute("""
            DELETE FROM book_exemplar
            WHERE exemplarId = :exemplar_id
        """,
        {
            'exemplar_id': exemplarId,
        })

        self.db.commit()

    def delete_exemplar_history(self, exemplarId):
        """
        Removes all history records with that exemplar ID.
        """

        self.c.execute("""
            DELETE FROM takeout
            WHERE bookExemplarId = :exemplar_id
        """,
        {
            'exemplar_id': exemplarId,
        })

        self.db.commit()

    def give_book(self, readerId, bookExemplarId, givenTime):
        self.c.execute("""
            INSERT INTO takeout (readerId, bookExemplarId, beginDate, givenTime)
            VALUES (:readerId, :bookExemplarId, julianday('now'), :givenTime)
        """, {
            'readerId': readerId,
            'bookExemplarId': bookExemplarId,
            'givenTime': givenTime
        })

        self.db.commit()

    def take_book(self, bookExemplarId):
        self.c.execute("""
            UPDATE takeout
            SET endDate = julianday('now')
            WHERE
                endDate IS NULL AND
                bookExemplarId = :bookExemplarId AND
                beginDate = (
                                SELECT MAX(beginDate)
                                FROM takeout
                                WHERE bookExemplarId = :bookExemplarId
                            )
        """, {
            'bookExemplarId': bookExemplarId
        })

        self.db.commit()

    def find_genre(self, name):
        self.c.execute("""
            SELECT id FROM genre
            WHERE name = :name
        """, {'name': name})
        return self.c.fetchone()

    def find_subject(self, name):
        self.c.execute("""
            SELECT id FROM subject
            WHERE name = :name
        """, {'name': name})
        return self.c.fetchone()

    def find_author(self, name):
        self.c.execute("""
            SELECT id FROM author
            WHERE
                name = :name
        """, {
            'name': name
        })
        return self.c.fetchone()

    def find_last_reader(self, fName, sName, pName):
        self.c.execute("""
            SELECT id
            FROM reader
            WHERE
                fName = :fName AND
                sName = :sName AND
                pName = :pName
            ORDER BY registrationDate DESC
        """, {
            'fName': fName,
            'sName': sName,
            'pName': pName
        })
        return self.c.fetchone()[0]

    def find_publisher(self, name, town):
        self.c.execute("""
            SELECT id FROM publisher
            WHERE
                name = :name AND
                town = :town
        """, {
            'name': name,
            'town': town
        })
        return self.c.fetchone()

    def find_book(self, name, year, pages, UDK, BBK, ISBN, authorMark):
        self.c.execute("""
                    SELECT id FROM book
                    WHERE
                        name = :name AND
                        year = :year AND
                        pages = :pages AND
                        UDK = :UDK AND
                        BBK = :BBK AND
                        ISBN = :ISBN AND
                        authorMark = :authorMark
                """, {
            'name': name,
            'year': year,
            'pages': pages,
            'UDK': UDK,
            'BBK': BBK,
            'ISBN': ISBN,
            'authorMark': authorMark
        })

        return self.c.fetchone()[0]

    def find_last_exemplar(self, bookId):
        self.c.execute("""
            SELECT id
            FROM book_exemplar
            WHERE
                bookId = :bookId
            ORDER BY id DESC
        """, {
            'bookId': bookId
        })
        return self.c.fetchone()[0]

    def find_last_exemplar_ins(self):
        self.c.execute("""
                SELECT MAX(id) FROM book_exemplar
            """)
        return self.c.fetchone()[0]

    def weld_author_book(self, authorsId, bookId):
        # print([(i, bookId) for i in authorsId])
        self.c.executemany("""
            INSERT INTO author_book (authorId, bookId)
            VALUES (?, ?)
        """, [(i, bookId) for i in authorsId])

        self.db.commit()

    def weld_genre_book(self, genresId, bookId):
        # print([(i, bookId) for i in genresId])
        self.c.executemany("""
            INSERT INTO genre_book (genreId, bookId)
            VALUES (?, ?)
        """, [(i, bookId) for i in genresId])

        self.db.commit()

    def add_book(self, name, year, publisher_name,
                publisher_town, pages, subject, genres,
                authors, UDK, BBK, ISBN, authorMark):

        publisherId = self.find_publisher(publisher_name, publisher_town)
        if publisherId is None:
            print(f'Publisher {publisher_name} was not found, registered new one...')
            self.register_publisher(publisher_name, publisher_town)
            publisherId = self.find_publisher(publisher_name, publisher_town)

        # genreId = self.find_genre(genre_name)
        # if genreId is None:
            # print(f'Genre {genre_name} was not found, registered new one...')
        #     self.register_genre(genre_name)
        #     genreId = self.find_genre(genre_name)

        if authors is None:
            authorsId = [None]
        else:
            authorsId = []
            for i in authors:
                authorId = self.find_author(i)
                if authorId is None:
                    print(f'Author {i} was not found, registered new one...')
                    self.register_author(i)
                    authorId = self.find_author(i)
                authorsId.append(authorId[0])

        if genres is None:
            genresId = [None]
        else:
            genresId = []
            for i in genres:
                genreId = self.find_genre(i)
                if genreId is None:
                    print(f'Genre {i} was not found, registered new one...')
                    self.register_genre(i)
                    genreId = self.find_genre(i)
                genresId.append(genreId[0])

        subjectId = self.find_subject(subject)
        if subjectId is None:
            print(f'Subject {subject} was not found, registered new one...')
            self.register_subject(subject)
            subjectId = self.find_subject(subject)

        self.register_book(name, year, publisherId[0], pages, subjectId[0], UDK, BBK, ISBN, authorMark)
        # bookId = self.find_book(name, year, pages, UDK, BBK, ISBN, authorMark)
        bookId = self.get_last_id()
        self.weld_author_book(authorsId, bookId)
        self.weld_genre_book(genresId, bookId)

    def delete_book_deep(self, bookId):
        """
        Removes book and all it's exemplars.
        """
        
        self.delete_book(bookId)
        self.delete_book_author(bookId)

        exemplars = self.get_exemplar_list_raw(bookId)
        for i in exemplars:
            self.delete_exemplar(i)

    def delete_exemplar_deep(self, exemplarId):
        """
        Removes exemplar and all it's history/take out records.
        """
        
        self.delete_exemplar(exemplarId)
        self.delete_exemplar_history(bookId)

    def delete_reader_deep(self, readerId):
        """
        Removes reader and all it's history records.
        """
        
        self.delete_reader(readerId)
        self.delete_reader_history(readerId)

    def add_time_to_takeout(self, bookExemplarId, addTime):
        self.c.execute("""
                            UPDATE takeout
                            SET givenTime = givenTime + :addTime
                            WHERE
                                beginDate = (
                                    SELECT MAX(beginDate)
                                    FROM takeout
                                    WHERE bookExemplarId = :bookExemplarId
                                )
                        """, {
                            'bookExemplarId': bookExemplarId,
                            'addTime': addTime
                        })
        self.db.commit()

    def get_book_info(self, bookId):
        self.c.execute("""
                SELECT * FROM book
                WHERE id  = :bookId
            """, {'bookId': bookId})
        a1 = self.c.fetchone()
        if a1 is None:
            return None
        answer = {
            'id': a1[0],
            'year': a1[1],
            'name': a1[2],
            'publisher': '',
            'pages': a1[4],
            'subject': '',
            'UDK': a1[6],
            'BBK': a1[7],
            'ISBN': a1[8],
            'authorMark': a1[9],
            'genres': [],
            'authors': [],
            'exemplars': [],
            'givenExemplars': []
        }

        self.c.execute("""
                SELECT name, town
                FROM publisher
                WHERE id = :publisherID
            """, {'publisherID': int(a1[3])})
        publisher = self.c.fetchone()

        self.c.execute("""
                SELECT name
                FROM subject
                WHERE id = :subjectID
            """, {'subjectID': int(a1[5])})
        subject = self.c.fetchone()[0]

        answer['publisher'] = publisher
        answer['subject'] = subject

        self.c.execute("""
                SELECT author.name FROM author
                INNER JOIN author_book
                    ON author.id = author_book.authorId
                WHERE
                    author_book.bookId = :bookID
            """, {'bookID': bookId})
        for i in self.c.fetchall():
            answer['authors'].append(i[0])

        self.c.execute("""
                SELECT genre.name FROM genre
                INNER JOIN genre_book
                    ON genre.id = genre_book.genreId
                WHERE
                    genre_book.bookId = :bookID
            """, {'bookID': bookId})
        for i in self.c.fetchall():
            answer['genres'].append(i[0])

        self.c.execute("""
                SELECT exemplarId
                FROM book_exemplar
                WHERE bookId = :bookId
            """, {'bookId': bookId})
        for i in self.c.fetchall():
            answer['exemplars'].append(str(i[0]))

        self.c.execute("""
                SELECT
                    book_exemplar.exemplarId, takeout.readerId,
                    strftime('%d-%m-%Y', takeout.beginDate), takeout.givenTime,
                    CASE
                    WHEN julianday('now') - takeout.beginDate > takeout.givenTime
                        THEN '!!!Время вышло' 
                    ELSE CAST(CAST(takeout.givenTime - julianday('now') + takeout.beginDate AS INTEGER) AS TEXT)
                    END
                FROM book_exemplar
                INNER JOIN takeout
                    ON book_exemplar.exemplarId = takeout.bookExemplarId 
                WHERE
                    takeout.endDate IS NULL AND
                    book_exemplar.bookId = :bookId
            """, {'bookId': bookId})

        answer['givenExemplars'] = self.c.fetchall()

        return answer

    def get_user_info(self, userId):
        self.c.execute("""
                SELECT * FROM reader
                WHERE id = :userId
            """, {'userId': userId})
        a = self.c.fetchone()
        if a is None:
            return None
        answer = {
            'id': a[0],
            'fName': a[1],
            'sName': a[2],
            'pName': a[3],
            'regDate': a[4],
            'readingNormal': [],
            'readingTimeOut': []
        }

        self.c.execute("""
                SELECT bookExemplarId, strftime('%d-%m-%Y', beginDate), givenTime
                FROM takeout
                WHERE
                    endDate IS NULL AND
                    readerId = :userId AND
                    julianday('now') < beginDate + givenTime
            """, {'userId': userId})
        answer['readingNormal'] = self.c.fetchall()

        self.c.execute("""
                SELECT bookExemplarId, strftime('%d-%m-%Y', beginDate), givenTime
                FROM takeout
                WHERE
                    endDate IS NULL AND
                    readerId = :userId AND
                    julianday('now') >= beginDate + givenTime
            """, {'userId': userId})

        answer['readingTimeOut'] = self.c.fetchall()
        return answer

    def get_exemplar_info(self, exemplarId):
        self.c.execute("""
                SELECT book_exemplar.bookId, book.name FROM book_exemplar
                INNER JOIN book
                    ON book_exemplar.bookId = book.id
                WHERE book_exemplar.exemplarId = :exemplarId
            """, {'exemplarId': exemplarId})
        a = self.c.fetchone()
        if a is None:
            return None
        answer = {
            'id': exemplarId,
            'bookId': a[0],
            'bookName': a[1]
        }

        return answer

    def get_book_alf_name_tag_process(self, tagSearch, tagSort, tagAsc):
        searchTag = {
            'name': 'book.name',
            'year': 'book.year',
            'UDK': 'book.UDK',
            'BBK': 'book.BBK',
            'ISBN': 'book.ISBN',
            'author_mark': 'book.authorMark',
            'publisher_name': 'publisher.name',
        }

        sortTag = {
            'id': 'book.id',
            'name': 'book.name',
            'year': 'book.year',
            'UDK': 'book.UDK',
            'BBK': 'book.BBK',
            'ISBN': 'book.ISBN',
            'author_mark': 'book.authorMark',
            'publisher_name': 'publisher.name',
            'publisher_town': 'publisher.town',
            'subject_name': 'subject.name'
        }

        ascTag = {
            'asc': 'ASC',
            'desc': 'DESC'
        }

        if tagSearch not in searchTag:
            return (None, None, None)
        if tagSort not in sortTag:
            return (None, None, None)
        if tagAsc not in ascTag:
            return (None, None, None)

        tagSearch = searchTag[tagSearch]
        tagSort = sortTag[tagSort]
        tagAsc = ascTag[tagAsc]

        return tagSearch, tagSort, tagAsc



    def get_book_alf_name(self, text, tagSearch, tagSort, tagAsc):
        tagSearch, tagSort, tagAsc = self.get_book_alf_name_tag_process(tagSearch, tagSort, tagAsc)
        if tagSearch is None:
            return None
        self.c.execute("""
                            SELECT
                                book.id,
                                book.name,
                                book.year,
                                book.UDK,
                                book.BBK,
                                book.ISBN,
                                book.authorMark,
                                publisher.name,
                                publisher.town,
                                subject.name
                            FROM book
                            INNER JOIN publisher
                                ON publisher.id = book.publisherId
                            INNER JOIN subject
                                ON subject.id = book.subjectId
                            WHERE
                                (CAST({3} AS TEXT)) LIKE '%{0}%' OR
                                {3} = :t
                            ORDER BY {2} {1}
                        """.format(text, tagAsc, tagSort, tagSearch), {
                            't': text
                        })
        return self.c.fetchall()

    def get_book_alf_author_tag_process(self, tagSearch, tagSort, tagAsc):
        if tagSearch is None:
            return None
        searchTag = {
            'author_name': 'author.name'
        }

        sortTag = {
            'id': 'book.id',
            'author': 'author.name',
            'name': 'book.name',
            'year': 'book.year',
            'UDK': 'book.UDK',
            'BBK': 'book.BBK',
            'ISBN': 'book.ISBN',
            'publisher_name': 'publisher.name',
            'publisher_town': 'publisher.town',
            'subject_name': 'subject.name'
        }

        ascTag = {
            'asc': 'ASC',
            'desc': 'DESC'
        }

        if tagSearch not in searchTag:
            return (None, None, None)
        if tagSort not in sortTag:
            return (None, None, None)
        if tagAsc not in ascTag:
            return (None, None, None)

        tagSearch = searchTag[tagSearch]
        tagSort = sortTag[tagSort]
        tagAsc = ascTag[tagAsc]
        #print(tagSearch, tagSort, tagAsc)

        return tagSearch, tagSort, tagAsc

    def get_book_alf_author(self, text, tagSearch, tagSort, tagAsc):
        tagSearch, tagSort, tagAsc = self.get_book_alf_author_tag_process(tagSearch, tagSort, tagAsc)
        if tagSearch is None:
            return None
        self.c.execute("""
                            SELECT
                                author.name,
                                book.id,
                                book.name,
                                book.year,
                                book.UDK,
                                book.BBK,
                                book.ISBN,
                                publisher.name,
                                publisher.town,
                                subject.name
                            FROM author
                            INNER JOIN author_book
                                ON author.id = author_book.authorId
                            INNER JOIN book
                                ON author_book.bookId = book.id
                            INNER JOIN publisher
                                ON publisher.id = book.publisherId
                            INNER JOIN subject
                                ON subject.id = book.subjectId
                            WHERE
                                (author.name) LIKE '%{0}%'  OR
                                author.name = :t
                            ORDER BY {3} {1}
                        """.format(text, tagAsc, tagSearch, tagSort), {
                            't': text
                        })
        return self.c.fetchall()

    def get_book_syst_genre_tag_process(self, tagSearch, tagSort, tagAsc):
        searchTag = {
            'subject_name': 'subject.name',
            'genre': 'genre.name',
        }

        sortTag = {
            'id': 'book.id',
            'genre': 'genre.name',
            'name': 'book.name',
            'year': 'book.year',
            'UDK': 'book.UDK',
            'BBK': 'book.BBK',
            'ISBN': 'book.ISBN',
            'publisher_name': 'publisher.name',
            'publisher_town': 'publisher.town',
            'subject_name': 'subject.name'
        }

        ascTag = {
            'asc': 'ASC',
            'desc': 'DESC'
        }

        if tagSearch not in searchTag:
            return None, None, None
        if tagSort not in sortTag:
            return None, None, None
        if tagAsc not in ascTag:
            return None, None, None

        tagSearch = searchTag[tagSearch]
        tagSort = sortTag[tagSort]
        tagAsc = ascTag[tagAsc]

        return tagSearch, tagSort, tagAsc

    def get_book_syst_genre(self, text, tagSearch, tagSort, tagAsc):
        tagSearch, tagSort, tagAsc = self.get_book_syst_genre_tag_process(tagSearch, tagSort, tagAsc)
        if tagSearch is None:
            return None
        self.c.execute("""
                            SELECT
                                genre.name,
                                subject.name,
                                book.id,
                                book.name,
                                book.year,
                                book.UDK,
                                book.BBK,
                                book.ISBN,
                                publisher.name,
                                publisher.town
                            FROM genre
                            INNER JOIN genre_book
                                ON genre.id = genre_book.genreId
                            INNER JOIN book
                                ON genre_book.bookId = book.id
                            INNER JOIN publisher
                                ON publisher.id = book.publisherId
                            INNER JOIN subject
                                ON subject.id = book.subjectId
                            WHERE
                                (CAST({2} AS TEXT)) LIKE '%{0}%' OR
                                {2} = :t
                            ORDER BY {3} {1}
                        """.format(text, tagAsc, tagSearch, tagSort), {
                            't': text
                        })
        return self.c.fetchall()

    def get_exemplar_list_tag_process(self, tagSort, tagAsc):

        sortTag = {
            'id': 'book_exemplar.exemplarId',
            'book_id': 'book_exemplar.bookId',
            'user_id': 'takeout.readerId',
            'give_date': 'takeout.beginDate',
            'give_time': 'takeout.givenTime',
            'left': 'takeout.givenTime + takeout.beginDate - julianday("now")',
        }

        ascTag = {
            'asc': 'ASC',
            'desc': 'DESC'
        }

        if tagSort not in sortTag:
            return None, None, None
        if tagAsc not in ascTag:
            return None, None, None

        tagSort = sortTag[tagSort]
        tagAsc = ascTag[tagAsc]

        return tagSort, tagAsc

    def get_exemplar_list_raw(self, bookId):
        self.c.execute("""
                SELECT exemplarId
                FROM book_exemplar
                WHERE bookId = :bookId
            """, {'bookId': bookId})

        exemplars = []

        for i in self.c.fetchall():
            exemplars.append(str(i[0]))

        return exemplars

    def get_exemplar_list(self, tagSort, tagAsc):
        tagSort, tagAsc = self.get_exemplar_list_tag_process(tagSort, tagAsc)
        if tagSort is None:
            return None
        self.c.execute("""
                SELECT
                    book_exemplar.exemplarId, book_exemplar.bookId, 
                    takeout.readerId, strftime('%d-%m-%Y', takeout.beginDate), takeout.givenTime,
                    CASE
                    WHEN julianday('now') - takeout.beginDate > takeout.givenTime
                        THEN '!!!Время вышло' 
                    ELSE CAST(CAST(takeout.givenTime - julianday('now') + takeout.beginDate AS INTEGER) AS TEXT)
                    END
                FROM book_exemplar
                INNER JOIN takeout
                    ON book_exemplar.exemplarId = takeout.bookExemplarId 
                WHERE takeout.endDate IS NULL
                ORDER BY {0} {1}
            """.format(tagSort, tagAsc))
        answer = self.c.fetchall()
        return answer

    def get_reader_by_name_tag_process(self, tagSearch, tagSort, tagAsc):
        searchTag = {
            'text': 'text'
        }

        sortTag = {
            'id': 'reader.id',
            'f': 'reader.fName',
            's': 'reader.sName',
            'p': 'reader.pName',
        }

        ascTag = {
            'asc': 'ASC',
            'desc': 'DESC'
        }

        if tagSearch not in searchTag:
            return None, None, None
        if tagSort not in sortTag:
            return None, None, None
        if tagAsc not in ascTag:
            return None, None, None

        tagSearch = searchTag[tagSearch]
        tagSort = sortTag[tagSort]
        tagAsc = ascTag[tagAsc]

        return tagSearch, tagSort, tagAsc

    def get_reader_by_name(self, text, tagSearch, tagSort, tagAsc):
        tagSearch, tagSort, tagAsc = self.get_reader_by_name_tag_process(tagSearch, tagSort, tagAsc)
        if tagSearch is None:
            return None
        self.c.execute("""
                            SELECT
                                reader.id,
                                reader.sName,
                                reader.fName,
                                reader.pName,
                                reader.registrationDate
                            FROM reader
                            WHERE
                                (fName) LIKE '%{0}%' OR
                                (sName) LIKE '%{0}%' OR
                                (pName) LIKE '%{0}%'
                            ORDER BY {2} {1}
                        """.format(text, tagAsc, tagSort))
        return self.c.fetchall()

    def get_all_exemplars(self):
        self.c.execute("""
                            SELECT
                                exemplarId,
                                bookId
                            FROM book_exemplar
                        """)
        return self.c.fetchall()

    def get_last_id(self):
        return self.c.lastrowid

    def close(self):
        self.db.close()

    def wipe_all(self):
        self.c.execute("DROP TABLE IF EXISTS book")
        self.c.execute("DROP TABLE IF EXISTS author_book")
        self.c.execute("DROP TABLE IF EXISTS author")
        self.c.execute("DROP TABLE IF EXISTS book_exemplar")
        self.c.execute("DROP TABLE IF EXISTS genre")
        self.c.execute("DROP TABLE IF EXISTS reader")
        self.c.execute("DROP TABLE IF EXISTS takeout")
        self.c.execute("DROP TABLE IF EXISTS publisher")
        self.c.execute("DROP TABLE IF EXISTS genre_book")
        self.c.execute("DROP TABLE IF EXISTS subject")
        self.db.commit()

    def wipe_books(self):
        self.c.execute("DROP TABLE IF EXISTS book")
        self.db.commit()

if __name__ == '__main__':
    test = DataBase()
    # test.register_reader('A', 'S', 'D')
    # test.wipe_all()
    # test.register_genre('physics')
    # test.give_book(20, 1248, 10
    # test.add_time_to_takeout(1248, 2)
    # test.take_book(20, 1268)
    # test.add_book('Physics 10 garde', 2001, 'Питер', 'москва', 200, 'physics',
    #     ['study','study2','study3'],
    #     ['zxczxc dasd xcvx','zhhxczxc dassdd xggdcvx','zxffczxc dassdd xcvx'],
    #     '121kbf12l', '23780=-+-[]:врловл', '23798-231-1231-11', 'К48'
    # )
    # for i in test.get_reader_by_name('A'):
        # print(i)
    # print(test.get_book_info(1))
    # print(test.get_user_info(2))
    # print(test.get_exemplar_info(2))
    # def get_book_syst_genre(self, text, tagSearch, tagSort, tagAsc):
    # print(test.get_book_syst_genre('genre', 'genre', 'id', 'asc'))
    # print(test.get_book_alf_name('', 'name', 'id', 'asc'))
    # print(test.get_book_alf_author('', 'author_name', 'name', 'asc'))

    # test.register_exemplar(1, None)
    test.close()
