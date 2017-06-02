#encoding=utf-8

import hashlib
import models
from base import Base
import datetime

class BooksManager(Base):
    def __init__(self, logger_name):
        super(BooksManager, self).__init__(logger_name)


    def handle_results(self, instances):
        res = list()
        for instance in instances:
            d = instance.__dict__
            del(d['_sa_instance_state'])
            res.append(d)
        return res

    def spilt_books(self, books, items=4):
        response = []
        len_book = len(books)
        if len_book < items:
            response.append(books)
        else:
            for i in range(0, len_book, items):
                response.append(books[i:i+items])
        return response

    def get_popular(self, message):
        # Parser the parameter
        base_popular = 500
        base_new = 7
        leng = 0
        type = message['url_content']['type'][0]

        # Get sql handler
        instances = self.sql.get_instances(models.Book)

        if type == "popular":
            # Search
            books = self.handle_results(instances.filter(models.Book.salesVolume >= base_popular).all())
            leng = len(books)
        else: 
            base = datetime.datetime.now() - datetime.timedelta(days=base_new)
            books = self.handle_results(instances.filter(models.Book.created_at >= base).all())
            leng = len(books)

        # Split
        response = self.spilt_books(self.spilt_books(books))

        self.log.info("Get books successfully")

        # Response
        return self._response(response, success=True, len=leng)



    def get_book(self, message):
        # Parser the parameter
        book_filter = message['json_content']


        leng = 0
        
        # Get Books
        try:
            books = self.sql.query(models.Book, **book_filter)
            if not books:
                return self._response("Data Not Found")
            leng = len(books)
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))

        # Split
        response = self.spilt_books(self.spilt_books(books))

        self.log.info("Get books successfully")

        # Response
        return self._response(response, success=True, len=leng)


    def get_all_books(self, message):
        # Parser the parameter


        leng = 0
        
        # Get Books
        try:
            books = self.sql.query(models.Book)
            if not books:
                return self._response("Data Not Found")
            leng = len(books)
        except Exception as e:
            self.log.error(e)
            return self._response("%s%s" % (self.msg_failed, str(e)))


        response = self.spilt_books(books, items=10)
        self.log.info("Get books successfully")

        # Response
        return self._response(response, success=True, len=leng)
